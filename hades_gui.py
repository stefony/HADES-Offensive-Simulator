import streamlit as st
from core.attack_engine import simulate_credential_dump, simulate_reverse_shell
from core.log_simulator import generate_log
from core.exporter import export_to_csv
from core.evtx_generator import generate_evtx_script

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
