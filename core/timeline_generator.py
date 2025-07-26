import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta

def generate_timeline(events):
    timeline_data = []

    for event in events:
        # Извличане на валиден ISO 8601 timestamp
        ts_raw = event.get("timestamp") or event.get("sysmon", {}).get("time_generated")
        try:
            ts_start = datetime.fromisoformat(ts_raw)
        except:
            continue  # пропускай съмнителни записи

        ts_end = ts_start + timedelta(seconds=1)  # добави минимална продължителност

        timeline_data.append({
            "Start": ts_start,
            "End": ts_end,
            "Attack Type": event.get("attack", "Unknown"),
            "MITRE ID": event.get("technique", ""),
            "Detection": "✅ Detected" if event.get("sysmon", {}).get("detected", False) else "❌ Not Detected"
        })

    df = pd.DataFrame(timeline_data)

    fig = px.timeline(
        df,
        x_start="Start",
        x_end="End",
        y="Attack Type",
        color="Detection",
        hover_data=["MITRE ID"]
    )
    fig.update_yaxes(autorange="reversed")
    fig.update_layout(title="📊 Attack Timeline Visualization")

    return fig
