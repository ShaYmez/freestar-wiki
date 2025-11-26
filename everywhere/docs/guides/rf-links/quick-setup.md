# RF-Link Node Quick Setup Guide (IAX Extension Method)

Register your RF-Link node as an IAX2 extension on FreeSTAR Everywhere. No trunk or outbound routes needed!

---

## 1. Supply Your Credentials

Open a ticket with [https://support.freestareverywhere.com](https://support.freestareverywhere.com) and supply the PBX admin with the following information:
- **Callsign:** The callsign of the idividual or club of the RF-link owner. 
- **Username:** The identifier you wish to use for your RF-Link node IAX extension. Normally the callsign.
- **Password:** The secret/password for this extension. At least 10 digits. STRONG PASSWORD!
- **IAX Port:** The UDP port you wish to use for IAX (usually 4569, or specify a custom port if required).
- **IAX String:** The string you need to provide the PBX admin to confugure your extension. [IAX2 String generator](https://freestareverywhere.com/apps/iax2-generator)

The PBX admin will use these details to create your IAX extension.

---

## 2. Configure RF-Link Node (`/etc/asterisk/iax.conf`)

```ini
[GB1ABC]                   ; <--- Replace with your IAX username/callsign, must match USERNAME, UPPERCASE  
username = USERNAME        ; <--- Replace with your IAX username/callsign, must match USERNAME, UPPERCASE
secret = PASSWORD          ; <--- Replace with your password for this RF-Link, STRONG PASSWORD
type = user
context = fsphone
disallow = all
allow = ulaw
transfer = no
```

---

## 3. Dialplan Setup (`/etc/asterisk/extensions.conf`)

```ini
[fsphone]
exten => ${NODE},1,answer()
exten => ${NODE},n,Playback(rpt/Connecting)
exten => ${NODE},n,Playback(rpt/connected)
exten => ${NODE},n,Set(CALLSIGN=FS-${CALLERID(name)})
exten => ${NODE},n,rpt(${NODE}|P|${CALLSIGN})
exten => ${NODE},n,Hangup
```

---

## 4. Port Forwarding

Forward UDP port 4569 (or your custom port) to your node’s IP address if needed.

---

## 5. Reload Asterisk

```bash
asterisk -rx "dialplan reload"
asterisk -rx "iax2 reload"
```
Or use your control GUI’s "Reload" function.

---

## 6. Testing

- Dial your assigned extension from FreeSTAR Everywhere .
- Check monitoring for callsign display on your Allmon/supermon dashboard.
- Ensure credentials match PBX settings.

---

## Dial IAX String Generator
With Love! [IAX2 String generator](https://freestareverywhere.com/apps/iax2-generator)

## Support

[https://support.freestareverywhere.com](https://support.freestareverywhere.com)
