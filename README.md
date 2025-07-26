# 🎯 HADES-Offensive-Simulator v1.2.0

**HADES** (Highly Automated Detection Evasion Simulator) is a Red Team simulation tool built to generate offensive attack logs for training, SOC pipelines, and adversary emulation.

---

## 🚀 Features

- ✅ **Modern Streamlit Web UI**
- 🧰 Simulates offensive techniques and malware behavior
- 🧬 MITRE ATT&CK techniques mapped
- 🧪 **Malware Emulation Mode** (T1055.001, Registry, C2, Mutex, etc.)
- 🛰️ **APT TTP Simulation** with profiles (e.g., APT29)
- 🗃️ Exports logs in:
  - `JSON` (`event_log.json`)
  - `CSV` (`export.csv`)
  - `Sysmon XML` (`sysmon_log.xml`)
  - `PowerShell` log scripts (`generate_event.ps1`)
- 📥 Accepts uploaded custom `.json` logs for conversion
- 📊 Timeline chart generation with Plotly
- 🧠 Educational use for SOC analysts, blue teams, and students

---

## 🔬 Simulated Techniques

| Technique                | MITRE ID      |
|--------------------------|---------------|
| Credential Dump          | `T1003.001`   |
| Reverse Shell (PS obf)   | `T1059.001`   |
| Command Injection        | `T1059`       |
| SQL Injection            | `T1505.001`   |
| Reflected XSS            | `T1059.007`   |
| Lateral Movement (PsExec)| `T1021.002`   |

---

## 🧪 Malware Emulation

Simulates behaviors including:
- Registry persistence
- Temp file drop
- Mutex creation
- C2 beaconing (HTTP)
- Process injection (`T1055.001`)

---

## 🛰️ APT Simulation

Select from built-in profiles (e.g., APT29 - Cozy Bear).  
Steps are replayed using realistic offensive TTPs and logs are auto-generated.

---

## 📂 Output Files

All logs are saved to the `logs/` folder:

- `event_log.json`
- `export.csv`
- `sysmon_log.xml`
- `generate_event.ps1`
- `malware_emulation.json` (new)

---

## 🛠️ Installation

```bash
git clone https://github.com/your-user/HADES-Offensive-Simulator.git
cd HADES-Offensive-Simulator
pip install -r requirements.txt
streamlit run hades_gui.py

 

<img width="1819" height="494" alt="image" src="https://github.com/user-attachments/assets/6f8e2b74-5979-4eba-9c83-70e944026df8" />


