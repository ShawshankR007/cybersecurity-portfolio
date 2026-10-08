# Project 4 — DevSecOps Pipeline

> A CI/CD pipeline that automatically blocks insecure code and infrastructure before it ships. Few students build this, it's all over the resume, and it's genuinely impressive to employers because it's what real teams do.

**Resume skills covered:** CI/CD security · SAST · DAST · container scanning · IaC security · Terraform · Ansible · secure SDLC · GitHub Actions · pipeline security reviews

---

## The idea

Build a small app, wire it to **GitHub Actions**, and add security gates that **fail the build** when a high-severity issue appears:

```
  push / PR
     │
     ▼
 ┌─────────────────────────────────────────────┐
 │ GitHub Actions pipeline                       │
 │  1. SAST      (Semgrep)      — code flaws      │
 │  2. Secrets   (Gitleaks)     — leaked keys     │
 │  3. SCA       (Trivy/Grype)  — vuln deps       │
 │  4. IaC scan  (Checkov/tfsec)— bad Terraform   │
 │  5. Container (Trivy)        — image CVEs       │
 │  6. DAST      (OWASP ZAP)    — running app      │
 └─────────────────────────────────────────────┘
     │  any HIGH/CRITICAL → ❌ build fails
     ▼
  deploy (only if clean)
```

---

## Toolkit (all free / open source)

- **GitHub** + **GitHub Actions** (free for public repos)
- **Semgrep** — SAST
- **Gitleaks** — secret scanning
- **Trivy** — dependency + container + IaC scanning (one tool, does a lot)
- **Checkov** / **tfsec** — Terraform/IaC security
- **OWASP ZAP** — DAST (baseline scan action)
- **Terraform** — the infra to scan
- **Docker** — to containerize the app

---

## Step-by-step

### Step 1 — Create the sample app
1. A deliberately-imperfect small app is ideal (Python Flask or Node). Add a couple of known issues: an outdated dependency, a hardcoded secret in a branch, a weak SQL query.
2. Containerize it with a `Dockerfile`.
3. **Commit:** the app + Dockerfile.

### Step 2 — Add SAST (Semgrep)
1. Add a GitHub Actions workflow `.github/workflows/security.yml`.
2. Add a Semgrep job using the registry rules (`p/ci`, `p/owasp-top-ten`).
3. Push and watch it flag your intentional code flaw.
4. **Evidence:** screenshot the failing check.

### Step 3 — Add secret scanning (Gitleaks)
1. Add a Gitleaks job.
2. Commit a fake secret on a test branch → confirm the pipeline catches it.
3. Remove it, confirm the pipeline passes.

### Step 4 — Add dependency/SCA scanning (Trivy)
1. Add a Trivy `fs` scan for vulnerable dependencies.
2. Confirm it flags the outdated package. Bump the version, confirm it clears.

### Step 5 — Add IaC scanning (Checkov / tfsec)
1. Write a small **Terraform** config (reuse the misconfigs from Project 3 — public S3, open SG).
2. Add a Checkov job that scans the Terraform.
3. Confirm it flags the insecure resources; fix them; confirm it passes.
4. **This directly connects Projects 3 and 4** — call that out in your write-up.

### Step 6 — Add container image scanning (Trivy)
1. Build the Docker image in the pipeline.
2. Run `trivy image` against it.
3. Fail on HIGH/CRITICAL CVEs. Note how base-image choice changes results (try `alpine` vs a full OS).

### Step 7 — Add DAST (OWASP ZAP)
1. In the pipeline, spin up the app, then run the **ZAP baseline scan** action against it.
2. Review the alerts it produces.

### Step 8 — Set the gates & document
1. Configure each job so **HIGH/CRITICAL fails the build** but lower severities warn.
2. Add **branch protection** requiring the security checks to pass before merge.
3. Write up the full pipeline in the README with a before/after: "insecure PR blocked" screenshots.

---

## Deliverables to commit

- [ ] The sample app + Dockerfile
- [ ] `.github/workflows/security.yml` with all stages
- [ ] Terraform config (with the fixed, secure version committed)
- [ ] Screenshots: a PR **blocked** by the pipeline, and a clean PR passing
- [ ] A short "secure SDLC" write-up explaining each gate
- [ ] `notes.md`

## Verification checklist

- [ ] A PR introducing a known flaw is **automatically blocked**
- [ ] Each tool (SAST, secrets, SCA, IaC, container, DAST) has a visible pass/fail
- [ ] Branch protection prevents merging a failing PR
- [ ] No real secrets anywhere in the repo or its history

## Stretch goals

- Add **Ansible** to configure/harden the deploy target, scanned with `ansible-lint`.
- Push findings to GitHub's **Security tab** via SARIF upload.
- Add a manual approval gate to simulate a change-control step.

---

## Reflection (fill in when done)

*Which gate caught the most? How would you tune it to avoid annoying developers with false positives?*
