# 🧪 HADES Offensive Simulator - Usage Guide

This guide will walk you through using the HADES Red Team simulation tool via its web interface (Streamlit).

---

## ✅ Step-by-Step Instructions

### 1. Setup

Install the required dependencies:

```bash
pip install -r requirements.txt

Run the Streamlit GUI:
streamlit run hades_gui.py

2.Simulate Offensive Attacks
From the GUI:

Choose an attack type:

Credential Dump

Reverse Shell (Obfuscated)

Click Run Attack Simulation

The event will be:

Displayed in JSON format

Saved to logs/event_log.json

Exported to:

export.csv

generate_event.ps1 (PowerShell script)

You can download the simulated event as a JSON file.

3. Log Generation from Custom Event
Upload your own event_log.json

Choose the log type to generate:

CSV

Sysmon XML

EVTX (PowerShell)

Click Generate Log File

Logs will be saved to the logs/ directory

4. Optional: Inject Event into Event Viewer
To test detection pipelines, you can inject the event using the generated PowerShell script:
# Run from PowerShell as Administrator
.\logs\generate_event.ps1

 Make sure PowerShell execution policy allows running scripts:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

Troubleshooting
Make sure logs/ folder exists or is auto-created
If generate_event.ps1 doesn't run, check PowerShell script permissions
For Streamlit errors, try refreshing the browser or restarting the app

 Cleanup
To clear all logs:
rm -rf logs/*.*

HADES is designed for educational and testing purposes only. Use responsibly.


