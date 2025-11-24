# RF-Link Quick Setup Guide (FreePBX 17 Only!)

This guide shows how to configure FreePBX 17 to connect and monitor a FreeSTAR Everywhere RF-Link node using IAX2.

---

## 1. PBX Admin: Assign RF-Link Credentials

When a new RF-Link owner signs up, the PBX admin provides:
- **Extension number** (e.g. `8001`)
- **Username** (e.g. `rfnode12345`)
- **Password/Secret** (e.g. `YourStrongPassword`)
- **PBX Public IP or DNS** (e.g. `linkpbx.freestar.org`)
  
The RF-Link owner uses these to configure their node.

---

## 2. Add IAX2 Trunk (PBX Side)

**Navigation:**  
Connectivity > Trunks > Add IAX2 Trunk

### Trunk Settings:

Trunk Name: `freestar`

**Incoming:**
```ini
username = rfnode12345              ; Assigned by PBX admin
secret = YourStrongPassword         ; Assigned by PBX admin
host = Node_IP_or_DNS               ; IP or DNS of RF-Link node
type = peer
context = from-internal
disallow = all
allow = ulaw
qualify = yes                       ; Enables status monitoring (online/offline)
```
(*No register string needed on FreePBX. Registration, if used, is configured by RF-Link node owner.*)

---

## 3. Assign Extension for RF-Link

**Navigation:**  
Applications > Extensions > Add Custom Extension

- **User Extension:** `8001`               ; Assigned by PBX admin
- **Display Name:** `FS-RFNode`            ; Optional (e.g. FS-KM4UTR)

---

## 4. Outbound Route (Optional)

For easy dialing of the RF-Link node:  
Connectivity > Outbound Routes > Add Outbound Route

- **Route Name:** `RFLink`
- **Dial Patterns:** `8001`
- **Trunk Sequence:** `freestar`

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
freestar       203.0.113.30       OK (10 ms)
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
2. **PBX admin allocates extension, username, password, and PBX server address.**
3. **RF-Link owner configures node with provided details.**

---

## Support

Contact M0VUB
