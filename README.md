# HADES-Offensive-Simulator

**HADES** is a Red Team simulation framework built with Python and Streamlit.  
It provides offensive cybersecurity operators with a modular attack simulation environment.

## Features

- 📁 Modular core: attacks, payloads, and logging
- 🕸️ Web-based GUI (Streamlit)
- 🧪 Offline analysis with `.csv` and `.evtx` support
- 🧠 Designed for malware testing, C2, and post-exploitation simulation

## Components

- `core/` – core simulation engine
- `logs/` – exported data from simulations
- `hades_gui.py` – GUI front-end (Streamlit)
- `run.py` – main execution script

## Setup

```bash
pip install -r requirements.txt
python run.py

