import streamlit as st
import pandas as pd
import numpy as np
import time

# Page config
st.set_page_config(page_title="Smart Energy Dashboard", layout="wide")

st.title("⚡ AI Digital Twin Smart Energy Command Center")
st.markdown("---")

# 🔁 SIMULATE LIVE DATA
@st.cache_data
def load_data():
    df = pd.read_csv("final_output.csv")
    return df

df = load_data()

# Simulate new incoming data (LIVE effect)
new_row = df.iloc[-1].copy()

new_row['MW'] = new_row['MW'] + np.random.uniform(-0.5, 0.5)
new_row['HZ'] = new_row['HZ'] + np.random.uniform(-0.05, 0.05)

df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

# 🔹 DIGITAL TWIN
df['T1'] = df['MW'] * 0.20
df['T2'] = df['MW'] * 0.25
df['T3'] = df['MW'] * 0.15
df['T4'] = df['MW'] * 0.20
df['T5'] = df['MW'] * 0.20

# 🔹 AI RISK FUNCTION
def check_risk(x):
    if x > 1.0:
        return "CRITICAL"
    elif x > 0.7:
        return "WARNING"
    else:
        return "SAFE"

for t in ['T1','T2','T3','T4','T5']:
    df[t + '_status'] = df[t].apply(check_risk)

# 🔹 METRICS
col1, col2, col3 = st.columns(3)
col1.metric("⚡ Avg Load (MW)", round(df['MW'].mean(), 2))
col2.metric("🔺 Max Load (MW)", round(df['MW'].max(), 2))
col3.metric("🔻 Min Load (MW)", round(df['MW'].min(), 2))

st.markdown("---")

# 🔹 SYSTEM STATUS
st.subheader("🚨 Live System Status")

critical_count = (df[['T1_status','T2_status','T3_status','T4_status','T5_status']] == "CRITICAL").sum().sum()
warning_count = (df[['T1_status','T2_status','T3_status','T4_status','T5_status']] == "WARNING").sum().sum()

if critical_count > 5:
    st.error(f"⚠️ CRITICAL: {critical_count} overload events detected!")
elif warning_count > 5:
    st.warning(f"⚡ WARNING: {warning_count} stress events detected")
else:
    st.success("✅ System Stable")

# 🔹 LIVE GRAPH
st.subheader("📊 Live Energy Load")
st.line_chart(df['MW'])

st.markdown("---")

# 🔹 TRANSFORMER MONITORING
st.subheader("⚡ Transformer Monitoring")

col1, col2 = st.columns(2)

with col1:
    st.dataframe(df[['T1','T2','T3','T4','T5']].tail())

with col2:
    st.dataframe(df[['T1_status','T2_status','T3_status','T4_status','T5_status']].tail())

st.markdown("---")

# 🔥 AI SCENARIO DETECTION
st.subheader("🔥 AI Scenario Detection")

avg_load = df['MW'].mean()
max_load = df['MW'].max()

if max_load > 4.5:
    st.error("🔥 Heatwave Condition Detected")
elif avg_load > 3.5:
    st.warning("⚡ Peak Demand Period")
else:
    st.success("✅ Normal Condition")

# 🧠 ANOMALY DETECTION
st.subheader("🧠 Anomaly Detection")

spikes = df[df['MW'] > (df['MW'].mean() + 2*df['MW'].std())]

if not spikes.empty:
    st.warning(f"⚡ {len(spikes)} abnormal spikes detected")
else:
    st.success("✅ No anomalies")

# 🧠 DECISION SUPPORT
st.subheader("🧠 Decision Support")

if critical_count > 0:
    st.write("✔ Immediate load redistribution")
    st.write("✔ Emergency maintenance required")
elif warning_count > 0:
    st.write("✔ Monitor system closely")
else:
    st.write("✔ System stable")

# 🏙️ CONTROL CENTER
st.subheader("🏙️ Smart City Control Center")

if critical_count > 0:
    st.error("🚨 Grid Risk: HIGH")
elif warning_count > 0:
    st.warning("⚡ Grid Risk: MEDIUM")
else:
    st.success("✅ Grid Risk: LOW")

st.markdown("---")

st.caption("AI-Driven Digital Twin | Live Smart Energy Monitoring 🚀")

# 🔁 AUTO REFRESH (LIVE EFFECT)
time.sleep(8)
st.rerun()
