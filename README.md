# Cybersecurity Engineering Portfolio

A hands-on home lab that works through the full stack of a modern cybersecurity engineer role — red teaming, application & API security, cloud security, DevSecOps, detection & incident response, and security automation with a touch of ML.

Each project is self-contained, builds on the one before it, and uses **free or free-tier tooling** so the whole thing can be built on a single laptop plus a cloud free account.

> **Why this repo exists:** I'm learning these skills by building them, not just reading about them. Every folder documents what I built, how, what broke, and what I'd do differently. The write-ups matter as much as the labs.

---

## ⚠️ Ethics & scope

Everything here is done against **systems I own or am explicitly authorized to test** — local VMs, deliberately-vulnerable training apps, and my own cloud accounts. Never run these techniques against systems you don't own or have written permission to test. That's the line between a security engineer and a crime.

---

## The projects

| # | Project | Core skills | Status |
|---|---------|-------------|--------|
| 1 | [Home Lab Foundation](./01-home-lab-foundation) | Active Directory, GPO, PKI, firewalls, VLAN segmentation, DNS | 🔲 Not started |
| 2 | [Web & API Penetration Testing](./02-web-api-pentest) | OWASP Top 10, Burp, Nmap, Nessus, API security, reporting | 🔲 Not started |
| 3 | [Cloud Security Lab](./03-cloud-security-lab) | AWS/Azure security, CSPM, IAM least-privilege, Zero Trust | 🔲 Not started |
| 4 | [DevSecOps Pipeline](./04-devsecops-pipeline) | CI/CD security, SAST/DAST, container & IaC scanning, Terraform | 🔲 Not started |
| 5 | [SIEM, Detection & Incident Response](./05-siem-detection-ir) | SIEM, log analysis, detection rules, IR, EDR concepts | 🔲 Not started |
| 6 | [Red Team Automation + ML](./06-red-team-automation-ml) | MITRE ATT&CK, adversary emulation, Python/PowerShell automation, anomaly detection | 🔲 Not started |

Plus a [compliance mapping exercise](./docs/compliance-mapping.md) that ties the labs back to NIST 800-53 and ISO 27001 controls.

Update the status column as you go: 🔲 Not started → 🚧 In progress → ✅ Done.

---

## Suggested order & time budget

Do them `1 → 6`. Projects 5 and 6 pair up — you generate attacks in 6 and detect them in 5.

| Project | Rough effort (part-time) |
|---------|--------------------------|
| 1. Home Lab Foundation | 1–2 weeks |
| 2. Web & API Pentest | 2–3 weeks |
| 3. Cloud Security Lab | 2 weeks |
| 4. DevSecOps Pipeline | 1–2 weeks |
| 5. SIEM & IR | 2 weeks |
| 6. Red Team + ML | 2–3 weeks |

Total: roughly **3–4 months** of steady part-time work if you go deep. That's a feature, not a bug — depth is what shows.

---

## How each project folder is organized

```
0X-project-name/
├── README.md        # the step-by-step guide + write-up (start here)
├── notes.md         # your running log: what broke, what you learned
├── evidence/        # screenshots, scan outputs, redacted reports
└── src/             # scripts, configs, IaC, detection rules
```

Keep secrets, real IPs, and credentials **out** of the repo. See [`.gitignore`](./.gitignore) and the redaction note in each project.

---

## Skills → projects map

Mapped against a real cybersecurity engineer job description:

- **Red Teaming & VAPT** → Projects 2, 6
- **Application & API Security** → Projects 2, 4
- **Cloud Security (CSPM, IAM, Zero Trust)** → Projects 3, 1
- **DevSecOps & IaC** → Project 4
- **Detection & Incident Response (SIEM)** → Project 5
- **Security Automation (Python/PowerShell/Bash)** → Projects 4, 6
- **AI/ML Security** → Project 6
- **IAM, Network & Endpoint Security** → Projects 1, 3, 5
- **Compliance & Governance** → [compliance-mapping.md](./docs/compliance-mapping.md)

---


