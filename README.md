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
