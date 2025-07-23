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

Project Structure
 core/
  attack_engine.py       # Attack simulation logic
  log_simulator.py       # JSON/CSV log writer
  sysmon_simulator.py    # Sysmon 4688 event generation
  evtx_generator.py      # PowerShell EVTX script generation
logs/
  event_log.json         # Last generated attack log
  export.csv             # Exported CSV file
  generate_event.ps1     # EVTX injection script
  
How to Use
Select an attack scenario from the dropdown

Click "Run Attack Simulation"

View and download the JSON event log

Re-upload the log and generate CSV / Sysmon / EVTX
