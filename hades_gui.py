import json
import streamlit as st
from core.attack_engine import simulate_credential_dump, simulate_reverse_shell
from core.log_simulator import generate_log
from core.exporter import export_to_csv
from core.evtx_generator import generate_evtx_script

from core.log_simulator import generate_csv_log
from core.sysmon_simulator import generate_sysmon_log


st.set_page_config(page_title="HADES - Offensive Simulation", layout="wide")
st.title("🎯 HADES Offensive Attack Simulator")

attack_type = st.selectbox("Select Attack to Simulate:", ["Credential Dump", "Reverse Shell (Obfuscated)"])

if st.button("Run Attack Simulation"):

    if attack_type == "Credential Dump":
        event = simulate_credential_dump()
    else:
        event = simulate_reverse_shell()

    generate_log(event)
    export_to_csv(event)
    generate_evtx_script(event)

    st.success("✅ Attack simulated and logs generated.")

    st.subheader("🔍 Event Details:")
    st.json(event)

    st.download_button("📄 Download JSON", data=str(event), file_name="event_log.json")
    
    st.markdown("## 🔁 Log Generation from Uploaded File")

uploaded_file = st.file_uploader("Upload event_log.json", type="json")

if uploaded_file is not None:
    attack_data = json.load(uploaded_file)

    st.write("Loaded Event:")
    st.json(attack_data)

    log_type = st.radio("Select Log Type", ["CSV", "Sysmon XML", "EVTX"])

    if st.button("Generate Log File"):
        if log_type == "CSV":
            generate_csv_log(attack_data)
            st.success("✅ CSV log generated!")
        elif log_type == "Sysmon XML":
            generate_sysmon_log(attack_data)
            st.success("✅ Sysmon log generated!")
        elif log_type == "EVTX":
            generate_evtx_script(attack_data)
            st.success("✅ EVTX log generated!")

