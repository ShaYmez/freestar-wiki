# FreeSTAR Everywhere RF-Link Node Owner Quick Setup Guide

Connect your RF-Link node to FreeSTAR Everywhere using the details provided by the PBX admin.

---

## 1. IAX2 Trunk Setup (`/etc/asterisk/iax.conf`)

```ini
[freestar]
type=user
secret=YourStrongPassword         ; Provided by PBX admin
context=radio-secure
disallow=all
allow=ulaw

; Optional, if instructed:
; register => rfnode12345:YourStrongPassword@PBX_IP/8001
```

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
[radio-secure]
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

## 4. Reload

```bash
asterisk -rx "dialplan reload"
asterisk -rx "iax2 reload"
```
Or use the HamVoIP GUI "Reload."

---

## 5. Testing & Notes

- Dial your assigned extension (e.g. 8001) from FreeSTAR Everywhere.
- Your node’s callsign (FS-CALLSIGN) will appear in AllMon3/monitoring.
- EXTEN, username, password, and PBX IP must match PBX admin info.
- NODE is your own RF node number.

---

## Support

[https://support.freestareverywhere.com](https://support.freestareverywhere.com)
