# Getting this onto your GitHub

A one-time setup so the whole portfolio lives in a repo you can show employers.

## 1. Create the repo
- On GitHub, create a new **public** repo named `cybersecurity-portfolio` (public so it's part of your visible work).
- Don't initialize it with a README — you already have one.

## 2. Push from your machine
From inside the unzipped `cybersecurity-portfolio/` folder:

```bash
git init
git add .
git commit -m "Initial portfolio scaffold: 6 security engineering projects"
git branch -M main
git remote add origin https://github.com/<your-username>/cybersecurity-portfolio.git
git push -u origin main
```

Replace `<your-username>`.

## 3. Work in branches (good habit + shows process)
For each project, work on a branch and open a PR to `main`:

```bash
git checkout -b project-1-home-lab
# ... do the work, add evidence and notes ...
git add .
git commit -m "Project 1: AD domain, GPO hardening, PKI, pfSense segmentation"
git push -u origin project-1-home-lab
```

Open the PR on GitHub, write a short description of what you did, and merge it. Your commit history then *tells the story* of your learning — recruiters notice that.

## 4. Before every commit — the safety check
- [ ] No real credentials, API keys, or `.pem`/`.env` files (the `.gitignore` guards the common ones, but double-check).
- [ ] No real public IPs from any system that isn't yours.
- [ ] Screenshots redacted of anything sensitive.

> If you ever commit a secret by accident, assume it's compromised: **rotate it immediately**, don't just delete the file — it stays in git history.

## 5. Make it look finished
- Pin this repo on your GitHub profile.
- Add topics/tags: `cybersecurity`, `devsecops`, `pentesting`, `cloud-security`, `siem`.
- As each project completes, flip its status in the main README and add a screenshot or two.
