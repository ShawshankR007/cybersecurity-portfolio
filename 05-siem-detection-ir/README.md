# Project 5 — SIEM, Detection & Incident Response

> The blue-team half. Stand up a SIEM, feed it logs from your lab, write detection rules, then generate malicious activity and investigate it end-to-end as an incident. Pairs directly with Project 6 — you attack there, you catch it here.

**Resume skills covered:** SIEM · log analysis · threat intelligence · incident response · EDR/XDR concepts · detection engineering · MITRE ATT&CK mapping

---

## Toolkit (free)

- **Wazuh** — free SIEM + host-based EDR in one (recommended starting point)
- *or* the **ELK Stack** (Elasticsearch, Logstash, Kibana) for a build-it-yourself approach
- *or* **Splunk Free** (small daily ingest limit — check current cap)
- **Sysmon** (Windows) — rich endpoint telemetry; pair with a good config (e.g., SwiftOnSecurity's)
- **Atomic Red Team** — to generate benign-but-realistic attack telemetry (also used in Project 6)

---

## Step-by-step

### Step 1 — Deploy the SIEM
1. Stand up a **Wazuh** server VM on your lab network (single-node is fine for learning).
2. Access the dashboard and confirm it's healthy.
3. **Notes:** sketch your logging architecture — what sends logs where.

### Step 2 — Onboard log sources
1. Install the **Wazuh agent** on `DC01` and the `WIN11` client from Project 1.
2. Install **Sysmon** with a solid config on the Windows hosts.
3. Forward **pfSense** firewall logs (syslog) to the SIEM.
4. (Stretch) Ship **AWS CloudTrail** logs from Project 3.
5. **Verify:** confirm events from each source land in the dashboard.
6. **Evidence:** screenshot the connected agents and a live event feed.

### Step 3 — Baseline & explore
1. Browse normal activity: logons, process creation, network connections.
2. Learn the key event IDs (e.g., Windows 4624/4625 logon success/failure, 4688 process creation, Sysmon Event ID 1 process create, 3 network connect).
3. **Notes:** build a cheat-sheet of the event IDs that matter and why.

### Step 4 — Generate attacks & detect them
1. From Kali (or with **Atomic Red Team**), perform some noisy activity:
   - Brute-force a login (generates 4625s)
   - Run a suspicious PowerShell command
   - Do some port scanning against a host
2. Find each in the SIEM.
3. **Map each to MITRE ATT&CK** (e.g., T1110 Brute Force, T1059 Command & Scripting).

### Step 5 — Write detection rules
1. Write at least **three custom detection rules** (Wazuh rules, or Sigma rules you convert):
   - Multiple failed logons from one source in a short window
   - Suspicious PowerShell (encoded commands, `IEX`, download cradles)
   - A new local admin account created
2. Trigger each one and confirm it fires.
3. **Commit:** the rule files in `src/detections/`.

### Step 6 — Run a full incident response
Pick one attack and work the whole **IR lifecycle** (NIST 800-61):
1. **Detection & analysis** — what fired, what's the scope?
2. **Containment** — how would you isolate the host?
3. **Eradication & recovery** — remove the threat, restore.
4. **Lessons learned** — what detection gap did this reveal?
5. **Commit:** a written **incident report** in `src/incident-report.md`.

---

## Deliverables to commit

- [ ] Logging architecture diagram
- [ ] Event-ID cheat sheet
- [ ] 3+ custom detection rules that demonstrably fire
- [ ] Attack → ATT&CK technique mapping table
- [ ] A full incident report following the NIST IR lifecycle
- [ ] `notes.md`

## Verification checklist

- [ ] Logs flow from Windows, firewall, and (stretch) cloud into the SIEM
- [ ] Each custom rule fires on the intended activity and not on noise
- [ ] The incident report could be handed to someone else to act on

## Stretch goals

- Build a **detection dashboard** in Kibana/Wazuh for your top techniques.
- Integrate a **threat-intel feed** (e.g., abuse.ch) and enrich alerts.
- Measure **MTTD** (mean time to detect) before/after tuning — a real metric for your resume.

---

## Reflection (fill in when done)

*Which attack was surprisingly loud? Which was surprisingly quiet? What detection would you add next?*
