"""Control the input, preset and volume on a MiniDSP-SHD device using the Volumio API"""
#
# I'm basically a C programmer, so I'm sure there are "more Python" ways of
# doing some of this.
#
# The message format was obtained from looking at browser traffic on V1.125,
# so it may or may not work with Volumio 3.
#
import sys
import socketio

# Limit volume to 90% of maximum - increase this at your own risk...
VOL_LIMIT=90

def main():
    """Control the input, preset and volume on a MiniDSP-SHD device using the Volumio API"""
    dbg = False
    icmds = ["TOSLINK", "SPDIF", "AES-XBU", "RCA", "XLR", "USB"]
    pcmds = ["PRESET1", "PRESET2", "PRESET3", "PRESET4"]
    vcmds = ["VOLUME", "MUTE", "UNMUTE"]
    cmds = icmds + pcmds + vcmds
    args = sys.argv[1:]
    host = args[0]
    cmd = args[1].upper()
    if (len(args) < 2) or not cmd in cmds :
        print ("Usage: " + sys.argv[0] + " host " + '|'.join(cmds)+ " [vol%]" )
        return 1

    sio = socketio.Client()

    # Handle interesting socketio events
    @sio.event
    def connect():
        if dbg :
            print("Connected")
    @sio.event
    def closeAllModals(data):
        if dbg:
            print("closeAllModals")
    @sio.event
    def pushBrowseLibrary(data):
        # Some response to our command, so just disconnect
        if dbg :
            print("pushBrowseLibrary")
        sio.disconnect()
    @sio.event
    def pushState(data):
        # Some response to our command, so just disconnect
        if dbg :
            print("pushState")
        sio.disconnect()

    # connect and send the appropriate command
    url = "http://" + host + ":3000"
    sio.connect(url, transports=['websocket'])
    if dbg :
        print ("Sid is ", sio.sid)
    if cmd in pcmds :
        # change the Preset
        pno = pcmds.index(cmd) + 1
        pid = "presets/id/" + str(pno)
        sio.emit("browseLibrary", {"uri":pid,"prevUri":"presets"})
    elif cmd in icmds :
        # change the input
        ino = icmds.index(cmd) + 1
        iid = "inputs/id/" + str(ino)
        sio.emit("browseLibrary", {"uri":iid,"prevUri":"inputs"})
    elif cmd == "MUTE" :
        sio.emit("mute", "")
    elif cmd == "UNMUTE" :
        sio.emit("unmute", "")
    else :
        # volume - for safety limit to 90% by default
        if len(args) == 3 and args[2].isnumeric() :
            vol = int(args[2])
            if vol > VOL_LIMIT :
                vol = VOL_LIMIT
            sio.emit("volume", vol)

    sio.wait()
    return 0

if __name__ == '__main__':
    sys.exit(main())
