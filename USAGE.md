HADES Offensive Attack Simulator
A modular Red Team simulation framework for training, testing, and detection engineering.

⚙️ Prerequisites
Python 3.8+

OS: Windows/Linux

Installed dependencies from requirements.txt

✅ Install Requirements
 
pip install -r requirements.txt
🚀 Start the Simulation UI
 
streamlit run hades_gui.py
This launches a web-based interface (Streamlit) where you can select which cyber attack to simulate.

🧪 Simulate an Attack
Open the Streamlit app

Select an attack (e.g. Credential Dump)

Click "Run Attack Simulation"

✅ This generates a JSON log file called event_log.json, e.g.:

 
{
  "attack": "Credential Dumping",
  "tool": "Mimikatz",
  "technique": "T1003.001",
  "timestamp": "2025-07-23 14:00:00"
}
📁 Generate Fake Logs for Blue Team Testing
Once event_log.json is created, use it to generate detection artifacts.

📄 CSV Log
 
python log_simulator.py event_log.json
📄 Sysmon-style Log
 
python sysmon_simulator.py event_log.json
📄 Windows EVTX Log
 
python evt_generator.py event_log.json
🎯 Use Cases
Red Team simulation environments

Blue Team detection rule testing (Sigma, Splunk, ELK)

Threat hunting practice

Cyber range lab development

🧩 Modular Design
Easily extend core/ modules to simulate other ATT&CK techniques:

Add new .json templates

Extend script logic to simulate tools like Empire, Cobalt Strike, etc.

🤝 Contributing
Feedback, PRs, and suggestions welcome!
Submit an issue or contact the author via LinkedIn.

🔐 License
MIT License – see LICENSE file.

📌 Quick Commands Summary
Task	Command
Install deps	pip install -r requirements.txt
Run web GUI	streamlit run hades_gui.py
Generate logs	python log_simulator.py event_log.json
Generate EVTX	python evt_generator.py event_log.json
Generate Sysmon logs	python sysmon_simulator.py event_log.json
