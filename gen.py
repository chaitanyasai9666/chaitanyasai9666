"""Generate the profile's SVG artwork: python gen.py  (edit the data below, re-run, commit)."""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).parent / "assets"
PANEL, LINE = "#0a0f1c", "#1e3a5f"
CYAN, GREEN, AMBER, RED, ORANGE = "#22d3ee", "#34d399", "#fbbf24", "#f87171", "#fb923c"
TEXT, MUTED, DIM = "#f1f5f9", "#cbd5e1", "#64748b"
SANS = "'Segoe UI', Inter, Helvetica, Arial, sans-serif"
MONO = "'JetBrains Mono', 'Cascadia Code', Consolas, Menlo, monospace"

# ---- data: update these when a project is added --------------------------------------------
STATS = [("3", "security tools"), ("34", "detection checks"), ("13", "ATT&CK techniques"), ("34", "tests in CI")]
TOOLS = {"phish": ("Phishing Email Analyzer", CYAN), "logs": ("Log Threat Analyzer", GREEN), "recon": ("Nmap Recon Reporter", AMBER)}
COVERAGE = [   # tactic, [(technique id, name, tool)]
    ("Reconnaissance", [("T1595.002", "Vulnerability Scanning", "logs"), ("T1595.003", "Wordlist Scanning", "logs")]),
    ("Initial Access", [("T1566", "Phishing", "phish"), ("T1566.001", "Spearphishing Attachment", "phish"),
                        ("T1566.002", "Spearphishing Link", "phish"), ("T1190", "Exploit Public-Facing App", "logs"),
                        ("T1078", "Valid Accounts", "logs")]),
    ("Persistence", [("T1136.001", "Create Local Account", "logs")]),
    ("Defense Evasion", [("T1036.007", "Double File Extension", "phish"), ("T1656", "Impersonation", "phish")]),
    ("Credential Access", [("T1110.001", "Password Guessing", "logs"), ("T1110.003", "Password Spraying", "logs")]),
    ("Discovery", [("T1046", "Network Service Discovery", "recon")]),
]
TERMINALS = [  # file, title, tagline, command, [(severity or None, text)]
    ("card-phish", "Phishing Email Analyzer", "Triage a reported email in one command",
     "python phish_analyzer.py reported.eml",
     [(None, "Verdict: LIKELY PHISHING (score 25)"), ("HIGH", "T1566      SPF fail, DMARC fail"),
      ("HIGH", "T1656      claims 'paypal', sent by paypa1"), ("HIGH", "T1566.002  link text ≠ destination"),
      ("HIGH", "T1036.007  invoice.pdf.exe"), ("IOC ", "hxxp://203[.]0[.]113[.]9/login")]),
    ("card-logs", "Log Threat Analyzer", "A mini SIEM rule engine for SSH and web logs",
     "python log_analyzer.py auth.log access.log",
     [(None, "57 log lines analyzed, 8 findings"), ("CRIT", "T1078      login after brute force"),
      ("HIGH", "T1110.001  SSH brute force"), ("HIGH", "T1110.003  password spraying"),
      ("HIGH", "T1190      SQL injection attempt"), ("MED ", "T1595.003  web directory scan")]),
    ("card-recon", "Nmap Recon Reporter", "From a raw scan to a report someone can act on",
     "python recon_report.py 192.168.56.101",
     [(None, "2 hosts, 12 open ports, 10 findings"), ("CRIT", "21/ftp      vsftpd 2.3.4 backdoor"),
      ("CRIT", "6667/irc    UnrealIRCd backdoor"), ("HIGH", "23/telnet   cleartext remote login"),
      ("HIGH", "3306/mysql  database exposed"), ("LOW ", "80/http     unencrypted web")]),
]
PIPELINE = [("Commit", "git push"), ("SonarQube", "SAST"), ("Trivy", "image scan"),
            ("OWASP ZAP", "DAST"), ("Kubernetes", "deploy"), ("Prometheus", "monitor + alert")]
JOURNEY = [("2023", "Started B.Tech", "CSE (Cyber Security), SRMIST"),
           ("May – Aug 2026", "VAPT Intern", "Dhara Global Solutions"),
           ("Nov 2026", "Shipped 3 detection tools", "tested, in CI, mapped to ATT&CK"),
           ("May 2027", "Graduating", "open to security roles")]
TOOLBOX = [("I TEST WITH", ORANGE, ["Nmap", "Nessus", "Burp Suite", "Metasploit", "Wireshark", "OWASP Top 10"]),
           ("I DETECT WITH", CYAN, ["Python", "C", "MITRE ATT&CK", "Log analysis", "Phishing triage", "IOC extraction"]),
           ("I DEPLOY WITH", GREEN, ["Linux", "AWS", "Docker", "Kubernetes", "Terraform", "Ansible", "Jenkins", "GitHub Actions"])]
SEV = {"CRIT": RED, "HIGH": ORANGE, "MED ": AMBER, "LOW ": DIM, "IOC ": CYAN}
# ---------------------------------------------------------------------------------------------

DEFS = f"""<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0b1220"/><stop offset="1" stop-color="#0f1f3d"/></linearGradient>
<linearGradient id="accent" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{CYAN}"/><stop offset="1" stop-color="{GREEN}"/></linearGradient>
<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="{LINE}" stroke-width="1" opacity="0.3"/></pattern>
<style>
.cursor {{ animation: blink 1.1s steps(1) infinite; }}
.pulse {{ animation: pulse 2.6s ease-in-out infinite; }}
.row {{ animation: show 10s steps(1) infinite backwards; }}  /* visible by default if animation is off */
.scan {{ animation: sweep 7s linear infinite; }}
@keyframes blink {{ 50% {{ opacity: 0; }} }}
@keyframes pulse {{ 0%, 100% {{ opacity: 0.45; }} 50% {{ opacity: 1; }} }}
@keyframes show {{ 0% {{ opacity: 0; }} 3% {{ opacity: 1; }} 97% {{ opacity: 1; }} 100% {{ opacity: 0; }} }}
@keyframes sweep {{ from {{ transform: translateX(-200px); }} to {{ transform: translateX(1400px); }} }}
@media (prefers-reduced-motion: reduce) {{ .cursor, .pulse, .row, .scan {{ animation: none; opacity: 1; }} }}
</style></defs>"""


def t(x, y, s, size=16, fill=TEXT, font=SANS, weight=400, anchor="start", extra=""):
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}" xml:space="preserve" {extra}>{escape(s)}</text>')


def svg(name, w, h, label, body):
    doc = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" '
           f'aria-label="{escape(label, {chr(34): "&quot;"})}">{DEFS}'
           f'<clipPath id="clip"><rect width="{w}" height="{h}" rx="18"/></clipPath><g clip-path="url(#clip)">'
           f'<rect width="{w}" height="{h}" fill="url(#bg)"/><rect width="{w}" height="{h}" fill="url(#grid)"/>'
           f'{body}</g><rect x="0.75" y="0.75" width="{w - 1.5}" height="{h - 1.5}" rx="18" fill="none" stroke="{LINE}" stroke-width="1.5"/></svg>')
    (OUT / f"{name}.svg").write_text(doc, encoding="utf-8")


def window(x, y, w, h, title):
    """Terminal window chrome."""
    return (f'<g transform="translate({x} {y})"><rect width="{w}" height="{h}" rx="12" fill="{PANEL}" stroke="{LINE}" stroke-width="1.5"/>'
            f'<circle cx="22" cy="20" r="5.5" fill="{RED}"/><circle cx="42" cy="20" r="5.5" fill="{AMBER}"/><circle cx="62" cy="20" r="5.5" fill="{GREEN}"/>'
            + t(w / 2, 25, title, 12, DIM, MONO, anchor="middle") + f'<line x1="0" y1="38" x2="{w}" y2="38" stroke="{LINE}"/>')


def finding(x, y, sev, text, i, size=15):
    tag = (f'<tspan fill="{SEV[sev]}">[{sev}]</tspan><tspan fill="{MUTED}"> {escape(text)}</tspan>' if sev
           else f'<tspan fill="{TEXT}" font-weight="700">{escape(text)}</tspan>')
    return (f'<text class="row" style="animation-delay:{0.6 + i * 0.7:.1f}s" x="{x}" y="{y}" font-family="{MONO}" '
            f'font-size="{size}" xml:space="preserve">{tag}</text>')


def hero():
    b = f'<rect class="scan" width="160" height="340" fill="{CYAN}" opacity="0.05"/><rect width="1200" height="4" fill="url(#accent)"/>'
    b += t(60, 76, "$ whoami", 17, GREEN, MONO)
    b += t(60, 132, "Boda Chaitanya Sai", 52, TEXT, weight=700, extra='letter-spacing="1"')
    b += '<rect x="60" y="150" width="250" height="4" rx="2" fill="url(#accent)"/>'
    b += t(60, 190, "I learned to break in. Now I build what catches it.", 23, MUTED)
    b += (f'<text x="60" y="228" font-family="{MONO}" font-size="15.5" fill="#94a3b8">Cyber Security  ·  VAPT  ·  Detection tooling in Python'
          f'<tspan class="cursor" fill="{CYAN}"> ▍</tspan></text>')
    b += window(770, 36, 380, 212, "detections.log")
    rows = [("CRIT", "T1078  login after brute force"), ("HIGH", "T1190  SQL injection attempt"),
            ("HIGH", "T1566  link text mismatch"), ("MED ", "T1595  directory scan")]
    b += "".join(finding(20, 70 + i * 30, s, x, i, 14) for i, (s, x) in enumerate(rows))
    b += (f'<text x="20" y="192" font-family="{MONO}" font-size="14" fill="{GREEN}">$<tspan class="cursor" fill="{CYAN}"> ▍</tspan></text>'
          f'<circle class="pulse" cx="356" cy="20" r="4" fill="{GREEN}"/></g>')
    for i, (num, label) in enumerate(STATS):
        x = 60 + i * 274
        b += (f'<rect x="{x}" y="270" width="258" height="46" rx="10" fill="{PANEL}" stroke="{LINE}" stroke-width="1.5"/>'
              + t(x + 20, 301, num, 24, "url(#accent)", weight=700) + t(x + 28 + len(num) * 14, 300, label, 16, MUTED))
    svg("hero", 1200, 340, "Boda Chaitanya Sai. Cyber Security, VAPT, detection tooling in Python. "
        + ", ".join(f"{n} {l}" for n, l in STATS), b)


def attack_map():
    col_w, gap, top = 185, 12, 118
    b = t(30, 48, "ATT&CK COVERAGE", 22, TEXT, weight=700, extra='letter-spacing="2"')
    b += t(30, 76, "Every chip is a technique one of my tools detects today.", 16, MUTED)
    for c, (tactic, techs) in enumerate(COVERAGE):
        x = 15 + c * (col_w + gap)
        b += (f'<rect x="{x}" y="{top - 22}" width="{col_w}" height="32" rx="8" fill="{LINE}" opacity="0.55"/>'
              + t(x + col_w / 2, top, tactic.upper(), 13, TEXT, MONO, 700, "middle"))
        for r, (tid, name, tool) in enumerate(techs):
            y, color = top + 24 + r * 60, TOOLS[tool][1]
            b += (f'<g class="pulse" style="animation-delay:{(c + r) * 0.35:.2f}s"><rect x="{x}" y="{y}" width="{col_w}" height="50" rx="8" '
                  f'fill="{PANEL}" stroke="{color}" stroke-width="1.5"/><rect x="{x}" y="{y}" width="5" height="50" rx="2" fill="{color}"/></g>'
                  + t(x + 16, y + 21, tid, 14.5, color, MONO, 700) + t(x + 16, y + 40, name, 12, MUTED))
    x = 30
    for name, color in TOOLS.values():
        b += f'<circle cx="{x + 6}" cy="462" r="6" fill="{color}"/>' + t(x + 20, 467, name, 14, MUTED)
        x += 60 + len(name) * 8
    b += t(1170, 467, f"{sum(len(v) for _, v in COVERAGE)} techniques · {len(COVERAGE)} tactics", 14, DIM, MONO, anchor="end")
    svg("attack-map", 1200, 490, "MITRE ATT&CK coverage: " + "; ".join(
        f"{tac}: {', '.join(i for i, _, _ in techs)}" for tac, techs in COVERAGE), b)


def terminal_cards():
    for name, title, tagline, cmd, lines in TERMINALS:
        b = t(30, 50, title, 25, TEXT, weight=700) + t(30, 78, tagline, 15.5, MUTED)
        b += '<rect x="30" y="92" width="60" height="3" rx="1.5" fill="url(#accent)"/>'
        b += window(30, 112, 530, 228, name.replace("card-", "") + ".sh")
        b += (f'<text x="20" y="66" font-family="{MONO}" font-size="14" xml:space="preserve"><tspan fill="{GREEN}">$</tspan>'
              f'<tspan fill="{TEXT}"> {escape(cmd)}</tspan></text>')
        b += "".join(finding(20, 92 + i * 24, s, x, i, 14) for i, (s, x) in enumerate(lines)) + "</g>"
        svg(name, 590, 360, f"{title}: {tagline}. Sample output: " + "; ".join(x for _, x in lines), b)


def pipeline_card():
    b = t(30, 50, "Secure DevSecOps Pipeline", 25, TEXT, weight=700)
    b += t(30, 78, "A healthcare API with a security gate at every stage", 15.5, MUTED)
    b += '<rect x="30" y="92" width="60" height="3" rx="1.5" fill="url(#accent)"/>'
    xs = [30, 215, 400]
    for i, (stage, role) in enumerate(PIPELINE):
        row = i // 3
        x, y = (xs[i % 3] if row == 0 else xs[2 - i % 3]), 128 + row * 108   # second row runs right to left
        gate = stage in ("SonarQube", "Trivy", "OWASP ZAP")
        b += (f'<g class="pulse" style="animation-delay:{i * 0.4:.1f}s"><rect x="{x}" y="{y}" width="160" height="70" rx="10" fill="{PANEL}" '
              f'stroke="{ORANGE if gate else CYAN}" stroke-width="1.5"/></g>'
              + t(x + 80, y + 31, stage, 16.5, TEXT, weight=700, anchor="middle")
              + t(x + 80, y + 53, role, 12.5, ORANGE if gate else MUTED, MONO, anchor="middle"))
    arrow = lambda x, y, g: t(x, y, g, 22, MUTED, anchor="middle")
    b += arrow(202.5, 170, "→") + arrow(387.5, 170, "→") + arrow(480, 224, "↓") + arrow(387.5, 278, "←") + arrow(202.5, 278, "←")
    b += f'<circle cx="36" cy="334" r="5" fill="{ORANGE}"/>' + t(50, 339, "security gate", 13, MUTED)
    b += t(560, 339, "Jenkins · Docker · AWS EC2", 13, DIM, MONO, anchor="end")
    svg("card-devsecops", 590, 360, "Secure DevSecOps pipeline: " + " then ".join(f"{s} ({r})" for s, r in PIPELINE), b)


def journey():
    xs = [130, 443, 757, 1070]
    b = t(30, 44, "JOURNEY", 18, TEXT, weight=700, extra='letter-spacing="2"')
    b += f'<line x1="{xs[0]}" y1="110" x2="{xs[-1]}" y2="110" stroke="url(#accent)" stroke-width="3"/>'
    for i, (x, (when, what, where)) in enumerate(zip(xs, JOURNEY)):
        b += (f'<circle cx="{x}" cy="110" r="14" fill="{PANEL}" stroke="{CYAN}" stroke-width="2"/>'
              f'<circle class="pulse" style="animation-delay:{i * 0.6:.1f}s" cx="{x}" cy="110" r="7" fill="url(#accent)"/>'
              + t(x, 82, when, 14.5, CYAN, MONO, 700, "middle") + t(x, 150, what, 17.5, TEXT, weight=700, anchor="middle")
              + t(x, 174, where, 14, MUTED, anchor="middle"))
    svg("journey", 1200, 205, "Journey: " + "; ".join(f"{a}: {b_} ({c})" for a, b_, c in JOURNEY), b)


def toolbox():
    b = ""
    for r, (label, color, items) in enumerate(TOOLBOX):
        y, x = 30 + r * 62, 220
        b += t(30, y + 27, label, 14, color, MONO, 700, extra='letter-spacing="1"')
        for item in items:
            w = 30 + len(item) * 9.2
            b += (f'<rect x="{x}" y="{y}" width="{w:.0f}" height="42" rx="21" fill="{PANEL}" stroke="{color}" stroke-width="1.5"/>'
                  + t(x + w / 2, y + 27, item, 16, TEXT, anchor="middle"))
            x += w + 12
    svg("toolbox", 1200, 216, "Toolbox. " + ". ".join(f"{l.capitalize()}: {', '.join(i)}" for l, _, i in TOOLBOX), b)


if __name__ == "__main__":
    for make in (hero, attack_map, terminal_cards, pipeline_card, journey, toolbox):
        make()
    print("wrote", ", ".join(sorted(p.name for p in OUT.glob("*.svg"))))
