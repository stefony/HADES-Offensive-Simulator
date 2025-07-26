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

 


 
 

<img width="1893" height="580" alt="Екранна снимка 2025-07-26 133617" src="https://github.com/user-attachments/assets/1f3ac5cb-e282-4243-a03a-f299ce137a38" />
<img width="1860" height="570" alt="Екранна снимка 2025-07-26 133606" src="https://github.com/user-attachments/assets/f309a515-ee00-40a8-9f01-bdcc4c9c9b2e" />
<img width="1579" height="446" alt="Екранна снимка 2025-07-26 133551" src="https://github.com/user-attachments/assets/a8b959cc-f046-4acb-9457-8d124b25ee28" />
<img width="1845" height="688" alt="Екранна снимка 2025-07-26 133537" src="https://github.com/user-attachments/assets/8d21e115-342c-4007-9658-91f1bbf3e771" />
