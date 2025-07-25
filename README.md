# 🎯 HADES-Offensive-Simulator

HADES (Highly Automated Detection Evasion Simulator) is a red team attack simulation tool designed to generate realistic offensive events for training, log analysis, and SOC detection pipelines.

---

## 🚀 Features

- ✅ Web GUI interface using **Streamlit**
- 🎭 Simulates common offensive techniques
- 📁 Generates realistic logs:
  - JSON (`event_log.json`)
  - CSV (`export.csv`)
  - EVTX via PowerShell (`generate_event.ps1`)
  - Sysmon-compatible XML (coming soon)
- 📤 Upload and process custom `.json` events
- 🧪 Educational tool for detection engineers and students

---

## ⚔️ Simulated Attacks

| Attack Type             | Technique Description                | MITRE ATT&CK ID  |
|-------------------------|--------------------------------------|------------------|
| Credential Dump         | `mimikatz → logonpasswords`          | `T1003.001`      |
| Reverse Shell (Obf.)    | `base64-encoded PowerShell`          | `T1059.001`      |
| Command Injection       | `ping + whoami` (OS injection)       | `T1059`          |
| SQL Injection           | `' OR '1'='1';--` Auth Bypass        | `T1505.001`      |
| XSS (Reflected)         | `<script>alert()</script>`           | `T1059.007`      |
| Lateral Movement (PsExec)| `Remote exec with credentials`      | `T1021.002`      |

---

## 🖥️ Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Launch GUI
streamlit run hades_gui.py


Project Structure
 ├── core/                   # Attack engine and log generation logic
│   ├── attack_engine.py
│   ├── exporter.py
│   ├── evtx_generator.py
│   ├── log_simulator.py
│   └── sysmon_simulator.py
├── logs/                  # All output logs (json/csv/evtx)
│   ├── event_log.json
│   ├── export.csv
│   └── generate_event.ps1
├── hades_gui.py           # Streamlit GUI interface
├── run.py                 # Optional CLI runner
├── requirements.txt       # Python dependencies
├── README.md              # This file
└── USAGE.md               # Full usage instructions


License
MIT License. See LICENSE file for details.

Disclaimer
This tool is intended for educational, training, and detection engineering purposes only. Use responsibly and never on unauthorized systems.


