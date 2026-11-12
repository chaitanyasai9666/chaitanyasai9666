<div align="center">

<img src="./assets/banner.svg" alt="Boda Chaitanya Sai — Cyber Security, VAPT, Detection Tooling in Python" width="100%" />

<br />

<a href="https://github.com/chaitanyasai9666">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=18&duration=3000&pause=900&color=22D3EE&center=true&vCenter=true&width=820&lines=Final-year+B.Tech+CSE+(Cyber+Security)+%40+SRMIST;VAPT+Intern+%E2%86%92+building+tools+that+catch+what+I+used+to+scan+for;Every+finding+mapped+to+MITRE+ATT%26CK;Tests+and+CI+on+every+project" alt="Final-year B.Tech CSE (Cyber Security) at SRMIST. VAPT intern. Every finding mapped to MITRE ATT&CK." />
</a>

<br />

<p>
  <a href="https://www.linkedin.com/in/chaitanya-sai-63b216350/">
    <img src="https://img.shields.io/badge/LinkedIn-Chaitanya_Sai-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="https://github.com/chaitanyasai9666?tab=repositories">
    <img src="https://img.shields.io/badge/Focus-Blue_Team_%26_VAPT-22D3EE?style=for-the-badge" alt="Focus: Blue Team and VAPT" />
  </a>
  <img src="https://img.shields.io/badge/Open_to-Security_Roles_2027-34D399?style=for-the-badge" alt="Open to security roles, 2027 graduate" />
</p>

</div>

---

### 👋 About me

I'm a final-year **B.Tech CSE (Cyber Security)** student at **SRM Institute of Science and Technology**, graduating in May 2027.
During my **VAPT internship at Dhara Global Solutions** I tested enterprise networks with Nmap, Nessus, Burp Suite and Metasploit and wrote the reports that explained each finding.

Now I build the other side: small, tested Python tools that **detect** the attacks I learned to run. Each one maps its findings to MITRE ATT&CK, ships with unit tests, and runs in CI.

<div align="center">
  <img src="./assets/stats.svg" alt="3 security tools shipped, 34 detection checks, 13 MITRE ATT&CK techniques, 34 unit tests in CI" width="100%" />
</div>

---

### 🛡️ Security tooling

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>📧 <a href="https://github.com/chaitanyasai9666/phishing-email-analyzer">Phishing Email Analyzer</a></h3>
      <p>
        <img src="https://img.shields.io/github/actions/workflow/status/chaitanyasai9666/phishing-email-analyzer/ci.yml?style=flat-square&label=CI" alt="CI status" />
        <img src="https://img.shields.io/badge/indicators-12-22d3ee?style=flat-square" alt="12 indicators" />
        <img src="https://img.shields.io/badge/ATT%26CK-5_techniques-34d399?style=flat-square" alt="5 ATT&CK techniques" />
      </p>
      <p><b>Triage a reported email in one command.</b> Give it a saved <code>.eml</code> and it answers the four questions an analyst asks: who really sent it, where the links really go, what is attached, and whether it is pressuring the reader.</p>
      <ul>
        <li>Checks SPF/DKIM/DMARC failures, brand impersonation, mismatched link text, raw-IP and look-alike links, and disguised attachments.</li>
        <li>Outputs a verdict plus <b>defanged URLs and SHA-256 hashes</b> ready to paste into a ticket.</li>
      </ul>
      <p><code>Python</code> <code>email</code> <code>IOC extraction</code> <code>T1566</code></p>
    </td>
    <td width="50%" valign="top">
      <h3>📜 <a href="https://github.com/chaitanyasai9666/log-threat-analyzer">Log Threat Analyzer</a></h3>
      <p>
        <img src="https://img.shields.io/github/actions/workflow/status/chaitanyasai9666/log-threat-analyzer/ci.yml?style=flat-square&label=CI" alt="CI status" />
        <img src="https://img.shields.io/badge/rules-8-22d3ee?style=flat-square" alt="8 rules" />
        <img src="https://img.shields.io/badge/ATT%26CK-7_techniques-34d399?style=flat-square" alt="7 ATT&CK techniques" />
      </p>
      <p><b>A mini SIEM rule engine for SSH and web logs.</b> It finds brute force, password spraying, a successful login after brute force, SQL injection, path traversal and directory scans.</p>
      <ul>
        <li><b>Time-window burst detection</b> separates an attack from a forgetful user.</li>
        <li>Decodes URLs before matching, and resists <b>log injection</b> through attacker-controlled usernames.</li>
      </ul>
      <p><code>Python</code> <code>regex</code> <code>detection rules</code> <code>T1110</code> <code>T1190</code></p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>🔎 <a href="https://github.com/chaitanyasai9666/nmap-recon-reporter">Nmap Recon Reporter</a></h3>
      <p>
        <img src="https://img.shields.io/github/actions/workflow/status/chaitanyasai9666/nmap-recon-reporter/ci.yml?style=flat-square&label=CI" alt="CI status" />
        <img src="https://img.shields.io/badge/risky_services-12-22d3ee?style=flat-square" alt="12 risky services" />
        <img src="https://img.shields.io/badge/CVEs-2_backdoors-f87171?style=flat-square" alt="2 backdoor CVEs" />
      </p>
      <p><b>From raw scan to a report someone can act on.</b> Runs an Nmap service scan (or reads a saved one) and writes a severity-ranked risk report with a plain-language reason and a fix for every finding.</p>
      <ul>
        <li>Rules match the <b>detected service, not the port</b>, so telnet on port 2323 is still caught.</li>
        <li>Blocks <b>command injection</b> with allow-list target validation and shell-free execution.</li>
      </ul>
      <p><code>Python</code> <code>Nmap</code> <code>XML</code> <code>T1046</code></p>
    </td>
    <td width="50%" valign="top">
      <h3>🏥 <a href="https://github.com/chaitanyasai9666/vle-9">Secure DevSecOps for a Healthcare App</a></h3>
      <p>
        <img src="https://img.shields.io/badge/SAST-SonarQube-4E9BCD?style=flat-square&logo=sonarqubeserver&logoColor=white" alt="SAST: SonarQube" />
        <img src="https://img.shields.io/badge/DAST-OWASP_ZAP-00549E?style=flat-square" alt="DAST: OWASP ZAP" />
        <img src="https://img.shields.io/badge/Images-Trivy-1904DA?style=flat-square" alt="Image scanning: Trivy" />
      </p>
      <p><b>Security gates in a delivery pipeline.</b> A patient-records API taken through Jenkins, Docker and Kubernetes on AWS EC2 with scanning at every stage.</p>
      <ul>
        <li>Static analysis, container image scanning and dynamic scanning before deploy.</li>
        <li>Prometheus and Grafana for monitoring and alerting on the running app.</li>
      </ul>
      <p><code>Jenkins</code> <code>Docker</code> <code>Kubernetes</code> <code>Trivy</code> <code>OWASP ZAP</code></p>
    </td>
  </tr>
</table>

---

### ⚙️ Cloud & DevOps

| Project | What it does | Stack |
|---|---|---|
| [Devops-project](https://github.com/chaitanyasai9666/Devops-project) | A Spring Boot NLP API deployed automatically on every push, scanned by Trivy and monitored with Prometheus, Grafana and Alertmanager | Jenkins · Docker · k3s · Terraform · Ansible · AWS EC2 |
| [vle-8](https://github.com/chaitanyasai9666/vle-8) | Blue-green deployment with traffic switch and rollback through a Kubernetes Service selector | Terraform · Ansible · Docker · Minikube · Jenkins |
| [calorie-tracker](https://github.com/chaitanyasai9666/calorie-tracker) | Plate Count, a calorie and fiber tracker with tests and a CI deploy to GitHub Pages | HTML · JavaScript · GitHub Actions |

---

### 🧰 Toolbox

**Security**

<p>
  <img src="https://img.shields.io/badge/Nmap-0E83CD?style=for-the-badge" alt="Nmap" />
  <img src="https://img.shields.io/badge/Nessus-00C176?style=for-the-badge" alt="Nessus" />
  <img src="https://img.shields.io/badge/Burp_Suite-FF6633?style=for-the-badge&logo=burpsuite&logoColor=white" alt="Burp Suite" />
  <img src="https://img.shields.io/badge/Metasploit-2596CD?style=for-the-badge&logo=metasploit&logoColor=white" alt="Metasploit" />
  <img src="https://img.shields.io/badge/Wireshark-1679A7?style=for-the-badge&logo=wireshark&logoColor=white" alt="Wireshark" />
  <img src="https://img.shields.io/badge/OWASP_Top_10-000000?style=for-the-badge&logo=owasp&logoColor=white" alt="OWASP Top 10" />
  <img src="https://img.shields.io/badge/MITRE_ATT%26CK-C8102E?style=for-the-badge" alt="MITRE ATT&CK" />
</p>

**Languages & platforms**

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=black" alt="C" />
  <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux" />
  <img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge" alt="AWS" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white" alt="Kubernetes" />
  <img src="https://img.shields.io/badge/Terraform-844FBA?style=for-the-badge&logo=terraform&logoColor=white" alt="Terraform" />
  <img src="https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white" alt="Jenkins" />
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" alt="GitHub Actions" />
</p>

---

<div align="center">
  <sub>Everything here is tested on synthetic data or systems I own. Scan only what you are authorised to scan.</sub>
</div>
