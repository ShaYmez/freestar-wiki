# FreeSTAR Everywhere RF-Link Node Owner Quick Setup Guide

Connect your RF-Link node to FreeSTAR Everywhere using details provided by the PBX admin.

---

## 1. IAX2 Trunk Setup (`/etc/asterisk/iax.conf`)

```ini
[freestar]
type=user
secret=YourStrongPassword         ; Provided by PBX admin
context=fsphone
disallow=all
allow=ulaw

; Optional: Custom port example, if instructed by admin (default is 4569)
bindport=4570

; Optional, if instructed:
; register => rfnode12345:YourStrongPassword@PBX_IP/8001
```
- **Default IAX2 port is UDP 4569.** Only set `bindport` if you and the PBX admin agree to use a custom port (e.g. 4570).

---

## 2. Globals (`/etc/asterisk/extensions.conf`)

```ini
[globals]
NODE = 12345        ; Your RF node number
EXTEN = 8001        ; Provided by PBX admin
```

---

## 3. Dialplan (`/etc/asterisk/extensions.conf` or HamVoIP GUI)

```ini
[fsphone]
exten => ${EXTEN},1,Set(CALLSIGN=FS-${CALLERID(name)})
exten => ${EXTEN},2,Ringing
exten => ${EXTEN},3,Wait(2)
exten => ${EXTEN},4,Answer
exten => ${EXTEN},5,Set(REMOTE=${CALLSIGN})
exten => ${EXTEN},6,NoOp(Connected: ${CALLSIGN})
exten => ${EXTEN},7,Rpt,${NODE}|P
exten => ${EXTEN},8,Hangup
```

---

> **IMPORTANT:**  
> - Forward UDP port 4569 (default) on your router/firewall to your RF-Link node’s IP address.  
> If using a custom port (e.g. 4570), forward **that** UDP port instead.
> - If using a custom port, notify the PBX admin—they must configure the trunk for a different IAX port.

---

## 4. Reload

```bash
asterisk -rx "dialplan reload"
asterisk -rx "iax2 reload"
```
Or use the HamVoIP GUI "Reload."

---

## 5. Testing & Notes

- Dial your assigned extension (e.g. 8001) from FreeSTAR Everywhere.
- Callsign (FS-CALLSIGN) appears in AllMon3/monitoring.
- EXTEN, username, password, and PBX IP (and port) must match admin info.
- NODE is your RF node number.

---

## Support

[https://support.freestareverywhere.com](https://support.freestareverywhere.com)
