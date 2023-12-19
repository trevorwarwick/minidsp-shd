# minidsp-shd
Simple Python script for controlling input, preset and volume on a MiniDSP-SHD device via the Volumio API.

For full control of many MiniDSP devices, https://github.com/mrene/minidsp-rs, which interfaces via USB 
is recommended, but this script gives a simple way of controlling some aspects of the SHD only, which 
has an IP based API via the embedded Volumio server.

Some examples:

```
python3 minidsp-shd.py hostname-or-ipv4 SPDIF
python3 minidsp-shd.py hostname-or-ipv4 PRESET4
python3 minidsp-shd.py hostname-or-ipv4 VOLUME 70
```

This can be used in Home Assistant using the Shell command integration, and then used in automations.
For example in HA's configuration.yaml:

```
shell_command:
      minidsp_rca: python3 custom_components/minidsp-shd.py minidsp-shd.lan RCA
      minidsp_spdif: python3 custom_components/minidsp-shd.py minidsp-shd.lan SPDIF
      minidsp_usb: python3 custom_components/minidsp-shd.py minidsp-shd.lan USB
      minidsp_toslink: python3 custom_components/minidsp-shd.py minidsp-shd.lan TOSLINK
```
