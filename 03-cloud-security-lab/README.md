# Project 3 — Cloud Security Lab

> Deliberately misconfigure a cloud account, detect it with a CSPM scanner, fix it, and enforce least-privilege IAM. Then practice real cloud attack paths against purpose-built vulnerable environments.

**Resume skills covered:** AWS / Azure security · Cloud Security Posture Management (CSPM) · IAM enforcement · Zero Trust · adaptive MFA / SSO · least privilege

---

## ⚠️ Cost safety first

Cloud bills are the #1 way students get burned. Before anything else:
- Use the **AWS Free Tier** (and/or Azure free credits).
- Set a **billing alarm / budget** at a low threshold (e.g., $5) **on day one**.
- **Tear down** resources when you're done each session (`terraform destroy` or delete manually).
- Never commit access keys — they get scraped from GitHub within minutes. See `.gitignore`.

---

## Toolkit (free)

- **AWS Free Tier account** (primary); **Azure** free account (optional, for multi-cloud)
- **Prowler** — open-source AWS/Azure/GCP CSPM scanner
- **ScoutSuite** — multi-cloud security auditing
- **AWS CLI** + **aws-vault** for safe credential handling
- **CloudGoat** (Rhino Security Labs) — vulnerable-by-design AWS environments
- **flaws.cloud** / **flaws2.cloud** — free guided AWS CTF (nothing to deploy)

---

## Step-by-step

### Step 1 — Account setup done safely
1. Create the AWS account; enable **MFA on the root user** immediately and then stop using root.
2. Create an **IAM admin user** for yourself with MFA; use that.
3. Set a **budget alert**.
4. Install and configure the AWS CLI. Store keys with `aws-vault`, not in plaintext.
5. **Notes:** write down the root-account hardening steps — this is CIS Benchmark material.

### Step 2 — Baseline scan (before)
1. Run **Prowler** against your fresh account:
   ```bash
   prowler aws -M html -o evidence/prowler-before
   ```
2. Run **ScoutSuite** too and compare.
3. **Commit:** the "before" report. Even a clean-ish account has findings — note them.

### Step 3 — Build intentional misconfigurations (then detect them)
Create these, then confirm the scanners catch them:
1. An **S3 bucket set to public** with a file in it.
2. An **over-permissive IAM policy** (`*:*` on a role).
3. A **security group open to 0.0.0.0/0** on port 22.
4. An **unencrypted** EBS volume or RDS instance.
5. Re-run Prowler → confirm each misconfig appears as a finding.
6. **Evidence:** before/after scan screenshots showing the new findings.

### Step 4 — Remediate & re-scan
1. Fix each misconfiguration (block public access, scope IAM down, restrict the SG, enable encryption).
2. Re-run Prowler → findings should drop.
3. **Notes:** record the delta — "X findings → Y findings." This is your metric, mirroring real CSPM work.

### Step 5 — IAM least-privilege exercise
1. Create a role that can do exactly one job (e.g., read one S3 bucket) and nothing more.
2. Use **IAM Access Analyzer** to validate.
3. Document the difference between the lazy `*` policy and the scoped one.
4. **Notes:** explain least privilege and why `*` policies are dangerous.

### Step 6 — Zero Trust & identity
1. Enforce **MFA** via an IAM policy that denies actions without MFA.
2. (Optional) Set up **AWS IAM Identity Center (SSO)** to demonstrate centralized access + SSO concepts.
3. Write up how this maps to **Zero Trust** principles (verify explicitly, least privilege, assume breach).

### Step 7 — Attack paths (offensive cloud)
1. Deploy a **CloudGoat** scenario (e.g., `iam_privesc_by_rollback`).
2. Work through the privilege-escalation path as the attacker.
3. Do **flaws.cloud** end-to-end (nothing to deploy, pure learning).
4. **Commit:** a write-up of one full attack path — recon → exploit → escalation — with the defensive lesson.

---

## Deliverables to commit

- [ ] Prowler/ScoutSuite **before & after** reports (redacted)
- [ ] Misconfiguration catalog with detection evidence
- [ ] Least-privilege IAM policy (the scoped JSON) in `src/`
- [ ] MFA-enforcement policy
- [ ] A cloud attack-path write-up (CloudGoat or flaws.cloud)
- [ ] `notes.md`

## Verification checklist

- [ ] Root account has MFA and is unused for daily work
- [ ] Billing alarm is active
- [ ] Re-scan shows measurably fewer findings after remediation
- [ ] All lab resources torn down at the end (check the billing console)

## Stretch goals

- Write the misconfigurations as **Terraform** (ties directly into Project 4).
- Enable **CloudTrail** and ship logs to Project 5's SIEM.
- Repeat the S3/IAM exercise on **Azure** for multi-cloud coverage.

---

## Reflection (fill in when done)

*What's the scariest misconfiguration you created? How quickly did the scanner catch it?*
