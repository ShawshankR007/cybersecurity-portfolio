# Project 6 — Red Team Automation + ML

> The capstone. Emulate real adversary behavior with MITRE ATT&CK, automate it with your own Python/PowerShell (your "SOAR-lite"), and train a simple ML model to flag anomalies in the logs. This ties together red-teaming, automation, and AI/ML — and feeds detections straight into Project 5.

**Resume skills covered:** adversary emulation · MITRE ATT&CK · exploit simulation · security automation (Python/PowerShell/Bash) · SOAR concepts · AI/ML-driven threat detection · anomaly detection

---

## Toolkit (free)

- **MITRE Caldera** — automated adversary emulation framework
- **Atomic Red Team** — small, documented ATT&CK test cases
- **Python** (`scikit-learn`, `pandas`) — for the ML component
- **PowerShell / Bash** — for automation scripts
- Your **Project 1 lab** as the target and **Project 5 SIEM** as the detector

---

## Part A — Adversary emulation

### Step 1 — Run Atomic Red Team tests
1. Install Atomic Red Team on a Windows lab host.
2. Run a handful of atomics across the kill chain, e.g.:
   - **T1059** Command & Scripting Interpreter
   - **T1003** Credential Dumping (benign simulation)
   - **T1053** Scheduled Task
   - **T1021** Remote Services / lateral movement
3. For each, confirm whether Project 5 **detected it**. Log the gaps.

### Step 2 — Automated emulation with Caldera
1. Stand up the Caldera server.
2. Deploy an agent to a lab host.
3. Run an **operation** using a built-in adversary profile.
4. **Commit:** the operation report + which steps your SIEM caught.

---

## Part B — Automation ("SOAR-lite")

### Step 3 — Build an emulation + reporting script
1. Write a **Python or PowerShell** script that:
   - Runs a chosen set of ATT&CK techniques in sequence
   - Logs what it did, when, to a structured file (JSON/CSV)
   - Optionally cleans up after itself
2. This is your reusable **red-team simulation framework** — mirrors the resume's "Automated Red-Team Simulation Framework" project.
3. **Commit:** the script in `src/` with a clear README section.

### Step 4 — Automate a response action
1. Write a small script that reacts to a detection — e.g., reads an alert, then (in the lab) disables an account or blocks an IP in pfSense via its API.
2. This demonstrates **SOAR / workflow automation** without expensive tooling.

---

## Part C — ML anomaly detection

### Step 5 — Collect & prepare data
1. Export authentication logs from Project 5 (e.g., Windows logon events) to CSV.
2. Use **pandas** to engineer features: logon hour, source IP, account, success/failure, logons-per-hour, etc.
3. **Notes:** describe your features and why each might signal anomalous behavior.

### Step 6 — Train an anomaly detector
1. Use **scikit-learn's Isolation Forest** (the standard starter for unsupervised anomaly detection) to model "normal" logon behavior.
2. Feed in your red-team activity from Parts A/B and see if the model flags it as anomalous.
3. Tune and measure: how many real anomalies caught, how many false positives?
4. **Commit:** the notebook/script in `src/`, plus a short results write-up with a chart.

### Step 7 — Close the loop
1. Document the full pipeline: **emulate attack → log to SIEM → export → ML flags anomaly**.
2. Compare the ML approach to your hand-written rules from Project 5 — where does each win?

---

## Deliverables to commit

- [ ] Atomic Red Team + Caldera operation reports
- [ ] Attack → ATT&CK → "detected? y/n" coverage table
- [ ] The automated emulation script ("red-team framework")
- [ ] A SOAR-lite response-automation script
- [ ] The ML anomaly-detection script/notebook + results write-up
- [ ] `notes.md`

## Verification checklist

- [ ] Your emulation script runs repeatably and logs its actions
- [ ] The ML model flags at least some injected attack activity
- [ ] You can articulate the trade-off between rules and ML detection
- [ ] Nothing here was run outside your own lab

## Stretch goals

- Add a **purple-team report**: side-by-side of techniques run vs. detected, with detection improvements you made.
- Try a second ML approach and compare (e.g., clustering, or a supervised model if you label data).
- Wire the whole thing into a single `make`-style command.

---

## ⚠️ Safety

Caldera, Atomic Red Team, and credential-dumping simulations are **offensive tools**. Run them **only** inside your isolated lab, never on a network you don't own. Keep the VULN segment firewalled off (Project 1).

---

## Reflection (fill in when done)

*Did the ML model earn its keep versus simple rules? What would you need to make it production-worthy?*
