# 🛡️ HADES - Offensive Attack Simulator

**HADES** is an interactive tool for simulating offensive cyberattacks and generating forensic logs in multiple formats. It is designed for red team labs, detection engineering, SIEM testing, and DFIR training.

---

## 🔧 Key Features

- 🎯 **Attack Simulation**
  - Credential Dump (Mimikatz-like)
  - Reverse Shell (Obfuscated PowerShell)

- 📄 **Log Generation**
  - `JSON` – base log of the attack
  - `CSV` – table-formatted logs
  - `Sysmon XML` – simulated Sysmon 4688 event
  - `EVTX` – PowerShell script for injecting fake events

- 📤 **External JSON Import**
  - Upload your own `event_log.json` and generate custom logs

---

## ▶️ Run the Simulator

```bash
pip install -r requirements.txt
streamlit run hades_gui.py

## 📁 Project Structure

HADES/
├── core/ # Core simulation logic (attack, log, export modules)
│ ├── attack_engine.py
│ ├── log_simulator.py
│ ├── sysmon_simulator.py
│ ├── evtx_generator.py
│ └── exporter.py
├── logs/ # Exported logs (JSON, CSV, EVTX)
│ ├── event_log.json
│ ├── export.csv
│ └── generate_event.ps1
├── hades_gui.py # Streamlit web interface
├── run.py # Entrypoint script (optional)
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── USAGE.md # Step-by-step usage instructions


---

## 🚀 How to Use

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt


Run the GUI
streamlit run hades_gui.py

Select and run an attack simulation

Choose between Credential Dump or Reverse Shell (Obfuscated).

View the simulated event.

Download the event as event_log.json.

Generate log files

Upload a JSON event file.

Generate logs in .csv, Sysmon .xml, or .ps1 (EVTX script) formats.

Inject into Event Viewer (optional)

Run the generated PowerShell script as Administrator.




