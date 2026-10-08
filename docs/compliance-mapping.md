# Compliance Mapping Exercise — NIST 800-53 & ISO 27001

> You can't license a GRC platform as a student, but you *can* do the actual work GRC analysts do: map the technical controls you built in the labs back to formal framework controls. This short written exercise covers the resume's **compliance & governance** section (NIST 800-53, ISO 27001, GDPR/HIPAA awareness, audit reporting).

## How to use this

Pick controls you genuinely implemented across Projects 1–6 and fill in the evidence column with a link to the project folder / screenshot that proves it. That evidence-to-control linkage *is* audit preparation.

## Example mapping

| Control (NIST 800-53) | ISO 27001 (A-control) | What I built | Evidence |
|-----------------------|----------------------|--------------|----------|
| **AC-2** Account Management | A.5.16 Identity management | AD users/OUs, IAM users with least privilege | Projects 1, 3 |
| **AC-6** Least Privilege | A.8.2 Privileged access | Scoped IAM policy; PAM concepts | Project 3 |
| **IA-2** Identification & Authentication | A.5.17 Authentication info | MFA enforcement, SSO | Projects 1, 3 |
| **AC-4** Information Flow Enforcement | A.8.22 Segregation of networks | pfSense VLAN micro-segmentation | Project 1 |
| **SC-7** Boundary Protection | A.8.20 Network security | Firewall rules, IDS/IPS | Projects 1, 5 |
| **SI-2** Flaw Remediation | A.8.8 Mgmt of technical vulnerabilities | VAPT + remediation; patch GPOs | Projects 2, 1 |
| **SI-4** System Monitoring | A.8.16 Monitoring activities | SIEM, detection rules | Project 5 |
| **RA-5** Vulnerability Scanning | A.8.8 | Nessus, Prowler, Trivy | Projects 2, 3, 4 |
| **CM-6** Configuration Settings | A.8.9 Configuration mgmt | GPO/CIS baselines, IaC scanning | Projects 1, 4 |
| **IR-4** Incident Handling | A.5.24–5.27 Incident mgmt | Full IR lifecycle write-up | Project 5 |
| **SA-11** Developer Testing | A.8.25 Secure development | SAST/DAST in CI/CD | Project 4 |
| **SA-15** Development Process | A.8.28 Secure coding | Secure SDLC pipeline | Project 4 |

## Deliverable

- [ ] Complete this table with **your** evidence links once each project is done.
- [ ] Write one paragraph: "If an auditor asked me to prove we enforce least privilege, here's what I'd show them." Do that for 3 controls. That paragraph is exactly what GRC interviews probe.

## A note on GDPR / HIPAA

These are **regulations**, not technical control sets — you demonstrate awareness by explaining *which* of your controls support their requirements (e.g., encryption + access control + logging support both). A short write-up mapping 3–4 of your controls to a GDPR principle (e.g., "integrity and confidentiality") is enough to speak to it credibly.

> **Disclaimer:** This is a learning exercise. Real compliance work involves formal scoping, risk assessments, and often legal review — this demonstrates the *concepts*, not a certification.
