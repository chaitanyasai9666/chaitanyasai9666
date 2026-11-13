<div align="center">
  <img src="./assets/hero.svg" alt="Boda Chaitanya Sai. I learned to break in. Now I build what catches it. Cyber Security, VAPT, detection tooling in Python. 5 security projects, 63 security checks, 14 ATT&CK techniques, 70 tests in CI." width="100%" />
</div>

<br />

I'm a final-year **B.Tech CSE (Cyber Security)** student at **SRM Institute of Science and Technology**. As a **VAPT intern at Dhara Global Solutions** I spent a summer attacking enterprise networks with Nmap, Nessus, Burp Suite and Metasploit, and writing the reports that explained each finding.

That taught me what attacks look like from the inside. Now I write the tools that spot them: small, tested Python programs where every finding carries its MITRE ATT&CK ID.

<br />

## 🎯 What my tools can detect

<img src="./assets/attack-map.svg" alt="MITRE ATT&CK coverage map: 14 techniques across 6 tactics (Reconnaissance, Initial Access, Persistence, Defense Evasion, Credential Access, Discovery), colour-coded by the tool that detects each one." width="100%" />

<br />

## 🚀 Flagship: mini-siem

<a href="https://github.com/chaitanyasai9666/mini-siem"><img src="https://raw.githubusercontent.com/chaitanyasai9666/mini-siem/main/docs/dashboard.png" alt="The mini-siem dashboard after the lab's attack chain: 60 events analysed, 14 alerts, an ATT&CK coverage map with every technique lit, and an alert feed ending in a critical 'successful login after brute force'." width="100%" /></a>

**[mini-siem](https://github.com/chaitanyasai9666/mini-siem)** is a SIEM I built from scratch in Python, with no third-party packages. Agents ship logs from monitored machines, a rule engine analyses every event as it arrives, and alerts land on this live dashboard. It comes with a Docker attack lab: an attacker container runs Nmap, Hydra and web attacks against a weak server on an isolated network, and all 11 detection rules fire within seconds.

<br />

## 🛠️ What else I've built

Real output from each tool. Click a card to open the repo.

<p align="center">
  <a href="https://github.com/chaitanyasai9666/mini-siem"><img src="./assets/card-siem.svg" alt="mini-siem: a SIEM built from scratch with a Docker attack lab. Sample output: 60 events analysed, 14 alerts, 11 of 11 rules fired." width="49%" /></a>
  <a href="https://github.com/chaitanyasai9666/vle-9"><img src="./assets/card-devsecops.svg" alt="Secure DevSecOps Pipeline for a healthcare API: commit, SonarQube SAST, Trivy image scan, OWASP ZAP DAST, Kubernetes deploy, Prometheus monitoring." width="49%" /></a>
</p>
<p align="center">
  <a href="https://github.com/chaitanyasai9666/phishing-email-analyzer"><img src="./assets/card-phish.svg" alt="Phishing Email Analyzer: triage a reported email in one command. Sample output shows a LIKELY PHISHING verdict with SPF failure, brand impersonation, a mismatched link and a double-extension attachment." width="49%" /></a>
  <a href="https://github.com/chaitanyasai9666/log-threat-analyzer"><img src="./assets/card-logs.svg" alt="Log Threat Analyzer: a mini SIEM rule engine for SSH and web logs. Sample output shows a login after brute force, password spraying, SQL injection and a directory scan." width="49%" /></a>
</p>
<p align="center">
  <a href="https://github.com/chaitanyasai9666/nmap-recon-reporter"><img src="./assets/card-recon.svg" alt="Nmap Recon Reporter: from a raw scan to a report someone can act on. Sample output shows two backdoored services, cleartext telnet and an exposed database." width="49%" /></a>
  <a href="https://github.com/chaitanyasai9666/web-header-auditor"><img src="./assets/card-headers.svg" alt="Web Header Auditor: grade a site's security configuration from A to F. Sample output shows a careless site graded F for reflected CORS, plain HTTP, clickjacking and weak cookies." width="49%" /></a>
</p>

<p align="center">
  <a href="https://github.com/chaitanyasai9666/mini-siem/actions"><img src="https://img.shields.io/github/actions/workflow/status/chaitanyasai9666/mini-siem/ci.yml?style=flat-square&label=mini-siem%20tests" alt="mini-siem tests" /></a>
  <a href="https://github.com/chaitanyasai9666/phishing-email-analyzer/actions"><img src="https://img.shields.io/github/actions/workflow/status/chaitanyasai9666/phishing-email-analyzer/ci.yml?style=flat-square&label=phishing%20analyzer%20tests" alt="Phishing analyzer tests" /></a>
  <a href="https://github.com/chaitanyasai9666/log-threat-analyzer/actions"><img src="https://img.shields.io/github/actions/workflow/status/chaitanyasai9666/log-threat-analyzer/ci.yml?style=flat-square&label=log%20analyzer%20tests" alt="Log analyzer tests" /></a>
  <a href="https://github.com/chaitanyasai9666/nmap-recon-reporter/actions"><img src="https://img.shields.io/github/actions/workflow/status/chaitanyasai9666/nmap-recon-reporter/ci.yml?style=flat-square&label=recon%20reporter%20tests" alt="Recon reporter tests" /></a>
  <a href="https://github.com/chaitanyasai9666/web-header-auditor/actions"><img src="https://img.shields.io/github/actions/workflow/status/chaitanyasai9666/web-header-auditor/ci.yml?style=flat-square&label=header%20auditor%20tests" alt="Header auditor tests" /></a>
</p>

**Also on my GitHub**

- [**Devops-project**](https://github.com/chaitanyasai9666/Devops-project) — a Spring Boot NLP API that deploys itself on every push: Jenkins, Docker, k3s, Terraform and Ansible on AWS EC2, with Trivy scans and Prometheus/Grafana monitoring.
- [**vle-8**](https://github.com/chaitanyasai9666/vle-8) — blue-green deployment with instant traffic switch and rollback on Kubernetes.
- [**calorie-tracker**](https://github.com/chaitanyasai9666/calorie-tracker) — Plate Count, a calorie and fiber tracker with tests and a CI deploy to GitHub Pages.

<br />

## 🧭 How I got here

<img src="./assets/journey.svg" alt="Journey: 2023 started B.Tech CSE (Cyber Security) at SRMIST; May to August 2026 VAPT intern at Dhara Global Solutions; November 2026 built a SIEM and 4 security tools; May 2027 graduating, open to security roles." width="100%" />

<br />

## 🧰 Toolbox

<img src="./assets/toolbox.svg" alt="I test with Nmap, Nessus, Burp Suite, Metasploit, Wireshark, OWASP Top 10. I detect with Python, C, MITRE ATT&CK, OWASP mapping, log analysis, phishing triage, IOC extraction. I deploy with Linux, AWS, Docker, Kubernetes, Terraform, Ansible, Jenkins, GitHub Actions, SQLite." width="100%" />

<br />

## 📫 Say hello

Graduating **May 2027** and open to SOC analyst, VAPT and security engineering roles.
Find me on **[LinkedIn](https://www.linkedin.com/in/chaitanya-sai-63b216350/)**.

<img src="./assets/wave.svg" alt="" width="100%" />

<div align="center">
  <sub>Everything here is tested on synthetic data or systems I own. Scan only what you are authorised to scan.</sub>
</div>
