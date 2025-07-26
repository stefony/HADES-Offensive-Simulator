import json
import streamlit as st
import os
from core.attack_engine import (
    simulate_credential_dump,
    simulate_reverse_shell,
    simulate_command_injection,
    simulate_sql_injection,
    simulate_xss,
    simulate_lateral_movement,
)
from core.log_simulator import generate_log, generate_csv_log
from core.exporter import export_to_csv
from core.evtx_generator import generate_evtx_script
from core.sysmon_simulator import generate_sysmon_log
from core.timeline_generator import generate_timeline
from core.apt_loader import get_profiles, load_profile
from ui_malware_emulation import run_malware_emulation_ui  # ✅ fix

# Setup
os.makedirs("logs", exist_ok=True)
st.set_page_config(page_title="HADES - Offensive Simulation", layout="wide")
st.title("🎯 HADES Offensive Attack Simulator")

if "event_log" not in st.session_state:
    st.session_state["event_log"] = []

# Attack Descriptions
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

# Sidebar Navigation
mode = st.sidebar.radio("🧭 Navigation", ["Attack Simulation", "Malware Emulation", "APT Profile", "Log Upload"])

# =======================
# 🧨 1. ATTACK SIMULATION
# =======================
if mode == "Attack Simulation":
    attack_type = st.selectbox("Select Attack to Simulate:", list(attack_descriptions.keys()))
    st.markdown(f"""
    🧾 **Description:** {attack_descriptions[attack_type]["desc"]}  
    🧬 **MITRE ID:** `{attack_descriptions[attack_type]["mitre"]}`
    """)

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

        st.session_state["event_log"].append(event)

        st.success("✅ Attack simulated and logs generated.")
        st.subheader("🔍 Event Details:")
        st.json(event)

        st.download_button("📥 Download JSON", data=json.dumps(event, indent=4), file_name="event_log.json")

# =======================
# 🧬 2. MALWARE EMULATION
# =======================
elif mode == "Malware Emulation":
    run_malware_emulation_ui()

# ==============================
# 🛰️ 3. APT PROFILE SIMULATION
# ==============================
elif mode == "APT Profile":
    st.subheader("🛰️ APT TTP Profile Simulation")

    apt_profile = st.selectbox("Select APT Profile:", get_profiles())

    if st.button("🚀 Run APT Simulation"):
        events = []
        for step in load_profile(apt_profile):
            attack = step["attack"]
            technique = step["technique"]
            st.write(f"🔹 Simulating: {attack} ({technique})")

            if attack == "Credential Dump":
                event = simulate_credential_dump()
            elif attack == "Reverse Shell (Obfuscated)":
                event = simulate_reverse_shell()
            elif attack == "Command Injection":
                event = simulate_command_injection()
            elif attack == "SQL Injection":
                event = simulate_sql_injection()
            elif attack == "XSS (Reflected)":
                event = simulate_xss()
            elif attack == "Lateral Movement (PsExec)":
                event = simulate_lateral_movement()
            else:
                continue

            generate_log(event)
            export_to_csv(event)
            generate_evtx_script(event)
            events.append(event)

        st.session_state["event_log"].extend(events)

        st.success("✅ APT simulation complete!")
        st.subheader("📦 APT Event Chain:")
        st.json(events)

        fig = generate_timeline(events)
        st.plotly_chart(fig, use_container_width=True)

# ===============================
# 📤 4. LOG UPLOAD AND CONVERSION
# ===============================
elif mode == "Log Upload":
    st.subheader("📤 Upload & Convert Event Log")

    uploaded_file = st.file_uploader("Upload event_log.json", type=["json"])
    if uploaded_file is not None:
        try:
            event = json.load(uploaded_file)
        except json.JSONDecodeError as e:
            st.error(f"❌ Invalid JSON file: {e}")
            st.stop()

        st.json(event)
        log_type = st.radio("Select Log Format", ["CSV", "Sysmon XML", "EVTX"])

        if st.button("🛠 Generate Log"):
            if log_type == "CSV":
                generate_csv_log(event)
                st.success("✅ CSV log created!")
            elif log_type == "Sysmon XML":
                generate_sysmon_log(event)
                st.success("✅ Sysmon log created!")
            elif log_type == "EVTX":
                generate_evtx_script(event)
                st.success("✅ EVTX script created!")

# ===============================
# 📊 Optional: Timeline Preview
# ===============================
if st.session_state["event_log"]:
    st.markdown("---")
    st.subheader("📈 Attack Timeline Visualization")

    fig = generate_timeline(st.session_state["event_log"])
    st.plotly_chart(fig, use_container_width=True)
