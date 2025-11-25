# RF-Link Quick Setup Guide (FreePBX 17 Only!)

This guide shows how to configure FreePBX 17 to connect and monitor a FreeSTAR Everywhere RF-Link node using IAX2.

---

## 1. PBX Admin: Assign RF-Link Credentials

When a new RF-Link owner signs up, the RF Link owner  provides:
- **Username** (e.g. `rfnode12345`)
- **Password/Secret** (e.g. `YourStrongPassword`)
- **IAX Port** (4569 is default)
Upon acceptence we provide steering to the documentation for setup
  
The RF-Link owner uses these to configure their node. Negotiate the ticket to assign these credetials 

---

## 2. Add IAX2 Trunk (PBX Side)

**Navigation:**  
Connectivity > Trunks > Add IAX2 Trunk

### Trunk Settings:

Trunk Name: `gb3nm`

**Incoming:**
```ini
username = rfnode12345              ; Assigned by RF-Link owner
secret = YourStrongPassword         ; Assigned by RF-Link owner
host = 1234.nodes.allstarlink.org   ; IP or DNS of RF-Link node
port = 4580                         ; IAX Port assigned by RF-Link owner
type = peer
context = from-internal
disallow = all
allow = ulaw
qualify = yes                       ; Enables status monitoring (online/offline)
```
(*No register string needed on FreePBX. Registration, if used, is configured by RF-Link node owner.*)

---

## 3. Assign Extension for RF-Link (with Custom Dial String)

**Navigation:**  
Applications > Extensions > Add Custom Extension

- **User Extension:** `8001`               ; Assigned by PBX admin
- **Display Name:** `GB3NM-Link`           ; Optional
- **Dial:** `IAX2/gb3nm/8001`              ; This makes PBX dial out via trunk "gb3nm" to this node

> **IMPORTANT:**  
> By default, a "Custom Extension" will not route calls anywhere unless you specify a destination using the "Dial" field.
> The **Dial** field tells FreePBX how to route calls for this extension.  
> Replace `gb3nm` with your trunk’s actual name if different, and `8001` with the correct node extension if needed.
>
> **Example:**  
> ```
> Dial: IAX2/gb3nm/8001
> ```
> 
> If you skip this step, calls to `8001` will not go anywhere!

---

## 4. Outbound Route (Optional)

For easy dialing of the RF-Link node:  
Connectivity > Outbound Routes > Add Outbound Route

- **Route Name:** `RFLink`
- **Dial Patterns:** `8001`
- **Trunk Sequence:** `gb3nm`

---

## 5. Node Online Status Monitoring

**How it works:**  
- `qualify = yes` enables PBX to send periodic IAX pings to the RF-Link node.
- If the node responds: shows as `OK` in dashboard/CLI.
- If not: shows as `UNREACHABLE`.
- BLF keys, dashboards, and phonebook monitor this status automatically.

**Manual status check:**  
```bash
asterisk -rx "iax2 show peers"
```
Look for:
```
Name/Username  Host               Status
gb3nm          203.0.113.30       OK (10 ms)
```

---

## 6. Testing

- Dial extension `8001` from any FreePBX-connected phone.
- Call should ring through to RF-Link node.
- Node owner should see caller info on their node/monitoring panel.

---

## 7. Troubleshooting

- Ensure UDP port 4569 is open between PBX and node.
- Extension, username, password must match on both sides.
- If status is not `OK`, check firewall/NAT, Asterisk logs, credential match.

---

## 8. Onboarding Flow Summary

1. **RF-Link owner signs up for service.**
2. **PBX admin allocates username, password, and PBX server address.**
3. **RF-Link owner configures node with provided details.**

---

## Support

Contact M0VUB
