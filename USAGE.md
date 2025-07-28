# 🧪 HADES Offensive Simulator - Usage Guide
> A step-by-step guide to using the HADES Red Team simulation toolkit through its interactive Streamlit GUI.
---

## ✅ 1. Setup

### 📦 Install requirements

```bash
pip install -r requirements.txt

 Run the Streamlit GUI:
streamlit run hades_gui.py

2. Attack Simulation
From the left sidebar panel "Attack Simulation":

Choose from the following attacks:
Credential Dump (Mimikatz)
Reverse Shell (Base64 PowerShell)
Command Injection
SQL Injection
XSS (Reflected)
Lateral Movement (PsExec)
Phishing (Credential Harvesting)
Insecure Deserialization
Click ▶️ Run Attack Simulation

The result:

✅ Displayed as formatted JSON
📝 Saved as logs/event_log.json
📤 Exported to:
logs/export.csv
logs/generate_event.ps1 (PowerShell script for EVTX)
Optional:
📥 Download JSON via button
🔐 Phishing simulation shows captured email and password
💣 Insecure Deserialization shows payload and impact


3. Malware Emulation
From the "Malware Emulation" tab:
Click 🧪 Emulate Malware Behavior
The tool will simulate beaconing and malware activity and log it.

4. APT Profile Simulation
From the "APT Profile" tab:

Select a predefined APT profile
Click 🚀 Run APT Simulation

For each step:
The tool will simulate the corresponding attack
All logs will be exported (JSON, CSV, PS1)
📈 Timeline graph will show a visual sequence of events

5. Log Generation from Custom Event
From the "Log Upload" tab:
Upload a custom event_log.json

Choose log format to generate:
📄 CSV
🛡️ Sysmon XML
🗂️ EVTX (via PowerShell)

Click 🛠 Generate Log File
Results are saved in the /logs directory.

6. Event Injection (Optional)
You can inject logs into the Windows Event Viewer (EVTX simulation):
# Run in PowerShell (as Administrator)
.\logs\generate_event.ps1
If blocked:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

Troubleshooting
✅ Make sure logs/ directory exists (created automatically)
⚠️ If PowerShell script fails to run: check execution policy
🔄 If Streamlit fails to load: restart browser or use Ctrl+C and rerun
💡 Event timestamps use current time; adjust if needed

Educational Use
HADES is an excellent tool for:
🧪 Blue team & SOC training
📊 SIEM rule testing
👨‍💻 Security researchers and students

7. Phishing & Insecure Deserialization

🧪 From the "Attack Simulation" tab, select either:
- **Phishing (Credential Harvesting)** – simulates a phishing page and logs stolen credentials
- **Insecure Deserialization** – simulates insecure object handling and log tampering or deletion

📌 Logs are saved with relevant MITRE IDs (`T1566.001` and `T1539`)
📊 Visualized on the attack timeline with detection flags



