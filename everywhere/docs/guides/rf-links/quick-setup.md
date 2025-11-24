# FreeSTAR Everywhere RF Link Owner Quick Setup (ASL3 & HamVoIP)

Copy/paste, then set your own EXTEN and NODE numbers in globals below.

---

## 1. IAX2 Trunk Setup

In `/etc/asterisk/iax.conf`:

```ini
[freestar]
type=user
secret=YourStrongPassword      ; Provided by FreeSTAR admin
context=fsphone
disallow=all
allow=ulaw
```
; Registration string for FreeSTAR Everywhere, edit the string below with the credentials:
; Format: register => extension:password@PBX_IP/extension
register => 8001:YourStrongPassword@PBX_IP/8001
```

---

## 2. Globals

In `/etc/asterisk/extensions.conf`:

```ini
[globals]
NODE = 12345        ; Your node number
EXTEN = 8001        ; Your RF-Link extension number provided by FreeSTAR Support
```

---

## 3. Dialplan

Put this in `/etc/asterisk/extensions.conf` or via HamVoIP GUI:

```ini
[fsphone]
exten => ${EXTEN},1,Set(CALLSIGN=FS-${CALLERID(name)})
exten => ${EXTEN},2,Ringing
exten => ${EXTEN},3,Wait(2)
exten => ${EXTEN},4,Answer
exten => ${EXTEN},5,Set(REMOTE=${CALLSIGN})
exten => ${EXTEN},6,NoOp(Connected: ${CALLSIGN})
exten => ${EXTEN},7,Rpt,${NODE}|P      ; Use |Pv if using VOX
exten => ${EXTEN},8,Hangup
```
*Change ${EXTEN} in globals only!*

---

## 4. Reload

```bash
asterisk -rx "dialplan reload"
asterisk -rx "iax2 reload"
```
Or use HamVoIP GUI "Reload".

---

## 5. Testing

Dial your RF-Link EXTEN that FreeSTAR support provided you with, and test.
- Callsign shows as `FS-CALLSIGN` in AllMon3.
- PTT by defalt with |P is *99 #. If using VOX |Pv, then use the MUTE for saftey PTT

---

## Support

Open a ticket at [https://support.freestareverywhere.com](https://support.freestareverywhere.com)
