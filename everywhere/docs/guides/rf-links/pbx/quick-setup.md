# PBX Admin Guide: Connecting to a Remote RF-Link Node (IAX Extension, FreePBX 17)

This guide explains how to create an IAX2 extension in FreePBX 17 so your PBX can connect to a remote RF-Link node (where the node acts as the Asterisk server).

---

## 1. Gather Required Information

Ensure you have the following details from the RF-Link node owner:
- **Username** (for the IAX extension)
- **Password/Secret** (for the IAX extension)
- **Node’s Public IP or DNS name** (where your PBX will connect)
- **IAX Port** (usually 4569, confirm if custom)

---

## 2. Create an IAX2 Extension in FreePBX

1. Go to **Applications > Extensions**.
2. Click **Add Extension** > **Add IAX2 Extension**.

**Basic Settings:**
- **User Extension:** (e.g. `8001`)  
  Unique number for this extension (choose any unused number).
- **Display Name:** (e.g. `RF-Link Node`)
- **Secret:** Enter the password supplied by the RF-Link node owner.
- **Port:** Leave as default (4569), change if needed.
- **Context:** `fsphone` (must match node's dialplan context).
- **CallerID:** Set as desired.
- **Dial:** `IAX2/USERNAME:PASSWORD@NODE-HOSTNAME:PORT/NODE

3. Click **Submit** and then **Apply Config**.

---

## 3. Example Dial String

To dial the RF-Link node from FreePBX, use a dial string in the following format:

```text
IAX2/USERNAME:PASSWORD@NODE-HOSTNAME:PORT/NODE
```
**For example:**
```text
IAX2/freestar:passw0rd@40071.nodes.allstarlink.org:4580/40071
```
- Replace `freestar` with the **username**.
- Replace `passw0rd` with the **password/secret**.
- Replace `40071.nodes.allstarlink.org` with the **node’s public DNS** or IP.
- Replace `4580` with the **IAX port** (if not the default `4569`).
- Replace the final `/40071` with the **desired extension** on the RF-Link node (typically its node number).

You can use this dial string wherever you configure outbound routes, custom extensions, or follow-me destinations in FreePBX to reach the RF-Link node.

---

## 4. Configure PBX to Connect to RF-Link Node

**Optional if NAT/firewall is present:**  
If your PBX is behind a firewall, ensure outbound UDP traffic to the node’s IP and IAX port is permitted.

---

## 5. Test the Connection

1. Use the Asterisk CLI:
   ```bash
   asterisk -rx "iax2 show peers"
   ```
   - Look for your new RF-Link extension in the list.
   - Status should show "Unmonitored" or "OK" if the node is reachable.

2. Try calling the new extension using the dial string above, or from a SIP phone or another extension.
   - The call should route to the RF-Link node and trigger its dialplan.

---

## 6. Troubleshooting

- Double-check username, password, port, hostname, and extension; must match the node configuration.
- Ensure your PBX can reach the RF-Link node’s public IP/DNS (check firewall/NAT).
- Use Asterisk logs for further debugging:
  ```bash
  asterisk -rvv
  ```
- If you see “no authority” or “authentication failed,” credentials are likely mismatched.

---

## 7. Support

For further help, contact: M0VUB
