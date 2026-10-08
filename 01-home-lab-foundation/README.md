# Project 1 — Home Lab Foundation

> The base layer everything else sits on. A small Windows Active Directory domain, segmented behind a firewall, with its own certificate authority. This is where IAM, endpoint, and network fundamentals live.

**Resume skills covered:** Active Directory · Group Policy · PKI / certificate management · firewalls · VPNs · micro-segmentation · system hardening · TCP/IP · DNS

---

## What you'll build

```
                 ┌─────────────────────────────┐
                 │        pfSense firewall       │
                 │   (router + VLAN segmentation)│
                 └──────┬───────────────┬────────┘
                        │ LAN (10.0.1.0)│ DMZ/VULN (10.0.2.0)
            ┌───────────┴───┐      ┌────┴──────────┐
            │ DC01 (AD/DNS/CA)│    │ Kali (attacker)│
            │ Windows Server  │    └────────────────┘
            └───────┬─────────┘
                    │
            ┌───────┴────────┐
            │ WIN11 (client) │
            └────────────────┘
```

---

## Prerequisites

- A host machine with **16 GB RAM minimum** (32 GB is much more comfortable), ~150 GB free disk.
- A free hypervisor: **VirtualBox** (fully free) or **VMware Workstation** (free for personal use). Either is fine.
- ISOs (all free evaluation downloads):
  - Windows Server 2022 **Evaluation** (180 days) — from the Microsoft Evaluation Center
  - Windows 11 **Enterprise Evaluation**
  - **Kali Linux** (pre-built VM image is easiest)
  - **pfSense CE** (Community Edition) ISO

> Eval ISOs expire. That's fine for a lab — snapshot the VM after each milestone so you can roll back.

---

## Step-by-step

### Step 1 — Install the hypervisor and create an internal network
1. Install VirtualBox/VMware.
2. Create two **host-only / internal networks** so your lab is isolated from your real home network:
   - `LAN` → 10.0.1.0/24
   - `VULN` → 10.0.2.0/24
3. **Commit:** a short `notes.md` entry describing your network layout and an exported diagram (draw.io is free).

### Step 2 — Stand up pfSense as the firewall/router
1. Create a VM with **two NICs**: one on `LAN`, one on `VULN` (and optionally a WAN NIC bridged for internet).
2. Install pfSense from the ISO. Assign interfaces: WAN, LAN (10.0.1.1), OPT1/VULN (10.0.2.1).
3. From a client on the LAN, open the pfSense web UI (`https://10.0.1.1`).
4. **Create firewall rules** that enforce segmentation — e.g., LAN can reach VULN, but VULN **cannot** initiate connections back to LAN. This is your first taste of micro-segmentation.
5. **Evidence:** screenshot your interface assignments and firewall rule table into `evidence/`.

### Step 3 — Build the Domain Controller (AD + DNS)
1. Create the Windows Server 2022 VM on the `LAN` network, static IP `10.0.1.10`.
2. Rename it `DC01`, set the DNS server to itself.
3. Install the **Active Directory Domain Services** role (Server Manager → Add Roles).
4. Promote it to a Domain Controller, creating a new forest — e.g. `lab.local`.
5. After reboot, confirm DNS is working: `nslookup lab.local` should resolve.
6. **Create OUs and users:** make an Organizational Unit structure (e.g., `Corp > IT`, `Corp > HR`), add 5–10 test users and a couple of groups.
7. **Notes:** write up *why* DNS and AD are joined at the hip — this is a common interview question.

### Step 4 — Join a Windows 11 client to the domain
1. Create the Win11 VM on `LAN`, point its DNS at `10.0.1.10`.
2. Join it to `lab.local`. Log in as a domain user.
3. **Evidence:** screenshot `systeminfo` showing domain membership.

### Step 5 — Group Policy (GPO) hardening
Create and link at least three GPOs, then verify they apply:
1. **Password policy** — enforce length/complexity/lockout.
2. **Disable SMBv1** and legacy protocols.
3. **A security baseline** — download the free **Microsoft Security Compliance Toolkit** and import a Windows baseline GPO.
4. Run `gpresult /h report.html` on the client to prove policies applied.
5. **Notes:** list which hardening settings you applied and the risk each mitigates.

### Step 6 — Stand up a Certificate Authority (PKI)
1. On a member server (or DC for the lab), install the **Active Directory Certificate Services** role.
2. Configure an Enterprise Root CA.
3. Issue a certificate (e.g., for LDAPS or a web server) and confirm the client trusts it.
4. **Notes:** explain the cert chain of trust in your own words — root → issuing → leaf.

### Step 7 — VPN (stretch)
1. In pfSense, configure an **OpenVPN** server.
2. Connect from a client and confirm you can reach the LAN through the tunnel.
3. **Evidence:** screenshot the connected tunnel + a successful ping across it.

---

## Deliverables to commit

- [ ] Network diagram (`evidence/network-diagram.png`)
- [ ] pfSense interface + firewall rule screenshots
- [ ] AD OU/user structure screenshot
- [ ] `gpresult` report showing GPOs applied
- [ ] CA / certificate chain screenshot
- [ ] `notes.md` with what broke and what you learned

## Verification checklist

- [ ] Client resolves `lab.local` via the DC's DNS
- [ ] A domain user can log into the Win11 client
- [ ] VULN network **cannot** reach LAN (test with `ping`/`nc` — it should fail)
- [ ] A GPO change (e.g., desktop background or password rule) visibly applies after `gpupdate /force`

## Stretch goals

- Add a second DC and set up replication.
- Deploy **LAPS** (Local Administrator Password Solution).
- Add Wazuh/Sysmon agents now so they're ready for Project 5.

---

## Reflection (fill in when done)

*What surprised you? What's the one thing you understand now that you didn't before?*
