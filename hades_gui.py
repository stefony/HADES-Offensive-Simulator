import json 
import streamlit as st
import uuid
import os
from random import randint
from datetime import datetime

from core.attack_engine import (
    simulate_credential_dump,
    simulate_reverse_shell,
    simulate_command_injection,
    simulate_sql_injection,
    simulate_xss,
    simulate_lateral_movement
)

from core.log_simulator import generate_log, generate_csv_log
from core.exporter import export_to_csv
from core.evtx_generator import generate_evtx_script
from core.sysmon_simulator import generate_sysmon_log

# Ensure logs/ directory exists
os.makedirs("logs", exist_ok=True)

# Page configuration
st.set_page_config(page_title="HADES - Offensive Simulation", layout="wide")
st.title("🎯 HADES Offensive Attack Simulator")

# Descriptions and MITRE IDs
attack_descriptions = {
    "Credential Dump": {
        "desc": "Simulates Mimikatz to dump user credentials from LSASS.",
        "mitre": "T1003.001"
    },
    "Reverse Shell (Obfuscated)": {
        "desc": "Base64-encoded PowerShell reverse shell payload.",
        "mitre": "T1059.001"
    },
    "Command Injection": {
        "desc": "Command injection via OS calls (e.g., `ping + whoami`).",
        "mitre": "T1059"
    },
    "SQL Injection": {
        "desc": "Classic `' OR '1'='1` authentication bypass attack.",
        "mitre": "T1505.001"
    },
    "XSS (Reflected)": {
        "desc": "Injects a `<script>alert()</script>` reflected XSS payload.",
        "mitre": "T1059.007"
    },
    "Lateral Movement (PsExec)": {
        "desc": "Simulates remote execution with stolen credentials via PsExec.",
        "mitre": "T1021.002"
    }
}

# Attack selection
attack_type = st.selectbox("Select Attack to Simulate:", list(attack_descriptions.keys()))

st.markdown(f"""
🧾 **Description:** {attack_descriptions[attack_type]["desc"]}  
🧬 **MITRE ID:** `{attack_descriptions[attack_type]["mitre"]}`
""")

# Attack simulation logic
if st.button("▶️ Run Attack Simulation"):

    if attack_type == "Credential Dump":
        event = simulate_credential_dump()
    elif attack_type == "Reverse Shell (Obfuscated)":
        event = simulate_reverse_shell()
    elif attack_type == "Command Injection":
        event = simulate_command_injection()
    elif attack_type == "SQL Injection":
        event = simulate_sql_injection()
    elif attack_type == "XSS (Reflected)":
        event = simulate_xss()
    elif attack_type == "Lateral Movement (PsExec)":
        event = simulate_lateral_movement()

    generate_log(event)
    export_to_csv(event)
    generate_evtx_script(event)

    st.success("✅ Attack simulated and logs generated.")
    st.subheader("🔍 Event Details:")
    st.json(event)
    st.download_button("📥 Download JSON", data=json.dumps(event, indent=4), file_name="event_log.json")

# Log file upload & generation
st.markdown("## 🔁 Log Generation from Uploaded File")
uploaded_file = st.file_uploader("Upload event_log.json", type=["json"])

if uploaded_file is not None:
    try:
        attack_data = json.load(uploaded_file)
    except json.JSONDecodeError as e:
        st.error(f"❌ Invalid JSON file: {e}")
        st.stop()

    st.write("Loaded Event:")
    st.json(attack_data)

    log_type = st.radio("Select Log Type", ["CSV", "Sysmon XML", "EVTX"])

    if st.button("🛠 Generate Log File"):
        if log_type == "CSV":
            generate_csv_log(attack_data)
            st.success("✅ CSV log generated!")
        elif log_type == "Sysmon XML":
            generate_sysmon_log(attack_data)
            st.success("✅ Sysmon log generated!")
        elif log_type == "EVTX":
            generate_evtx_script(attack_data)
            st.success("✅ EVTX log generated!")
