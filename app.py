import streamlit as st
import pandas as pd
import numpy as np

# 🔷 PAGE CONFIG
st.set_page_config(page_title="Smart Energy AI", layout="wide")

# 🎨 DARK PREMIUM THEME
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}
.stMetric {
    background-color: #1c1f26;
    padding: 15px;
    border-radius: 10px;
}
.block-container {
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# 🔷 HEADER
st.title("⚡ AI Smart Energy Command Center")
st.markdown("### 🟣 Intelligent | Scalable | Social Impact Enabled")

st.markdown("---")

# 🔷 SIDEBAR
st.sidebar.title("⚙️ Control Panel")
uploaded_file = st.sidebar.file_uploader("Upload Dataset", type=["csv", "xlsx"])

# DATA LOAD
if uploaded_file is not None:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file, engine="openpyxl")
else:
    st.warning("Upload dataset to continue")
    st.stop()

if 'MW' not in df.columns:
    st.error("Dataset must contain 'MW' column")
    st.stop()

# 🔁 SIMULATED LIVE
new_row = df.iloc[-1].copy()
new_row['MW'] += np.random.uniform(-0.5, 0.5)
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
df = df.tail(50)

# 🔷 DIGITAL TWIN
df['T1'] = df['MW'] * 0.20
df['T2'] = df['MW'] * 0.25
df['T3'] = df['MW'] * 0.15
df['T4'] = df['MW'] * 0.20
df['T5'] = df['MW'] * 0.20

# 🔷 RISK
def check_risk(x):
    if x > 1.0:
        return "CRITICAL"
    elif x > 0.7:
        return "WARNING"
    else:
        return "SAFE"

for t in ['T1','T2','T3','T4','T5']:
    df[t + '_status'] = df[t].apply(check_risk)

# 🔷 METRICS (CARD STYLE)
st.markdown("## 📊 System Overview")

col1, col2, col3 = st.columns(3)
col1.metric("⚡ Avg Load", round(df['MW'].mean(), 2))
col2.metric("🔺 Peak Load", round(df['MW'].max(), 2))
col3.metric("🔻 Min Load", round(df['MW'].min(), 2))

st.markdown("---")

# 🔷 GRAPH
st.markdown("## 📈 Live Energy Trend")
st.line_chart(df['MW'])

st.markdown("---")

# 🔷 ALERT PANEL
st.markdown("## 🚨 System Alerts")

critical_count = (df[[t+'_status' for t in ['T1','T2','T3','T4','T5']]] == "CRITICAL").sum().sum()
warning_count = (df[[t+'_status' for t in ['T1','T2','T3','T4','T5']]] == "WARNING").sum().sum()

if critical_count > 5:
    st.error("🚨 HIGH RISK GRID CONDITION")
    st.markdown("👩 Impact: Critical care zones like hospitals & maternity units may be affected")
elif warning_count > 5:
    st.warning("⚡ MODERATE GRID STRESS")
else:
    st.success("✅ SYSTEM STABLE")

st.markdown("---")

# 🔷 TRANSFORMER DASHBOARD
st.markdown("## ⚡ Transformer Intelligence")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Load Distribution")
    st.dataframe(df[['T1','T2','T3','T4','T5']])

with col2:
    st.subheader("Risk Status")
    st.dataframe(df[['T1_status','T2_status','T3_status','T4_status','T5_status']])

st.markdown("---")

# 🔷 AI INSIGHTS
st.markdown("## 🧠 AI Insights")

avg = df['MW'].mean()
maxv = df['MW'].max()

if maxv > 4.5:
    st.error("🔥 Extreme Demand (Heatwave Scenario)")
elif avg > 3.5:
    st.warning("⚡ Peak Demand Pattern")
else:
    st.success("✅ Normal Usage Pattern")

# 🔷 ANOMALY
spikes = df[df['MW'] > (avg + 2*df['MW'].std())]

if not spikes.empty:
    st.warning(f"⚠️ {len(spikes)} anomalies detected")
else:
    st.success("No anomalies detected")

st.markdown("---")

# 🔷 DECISION SUPPORT
st.markdown("## 🧠 Smart Decision Support")

if critical_count > 0:
    st.write("✔ Immediate load balancing required")
    st.write("✔ Emergency response recommended")
    st.write("✔ Ensure uninterrupted supply to critical infrastructure")
elif warning_count > 0:
    st.write("✔ Monitor closely")
else:
    st.write("✔ System operating normally")

st.markdown("---")

# 🔷 SOCIAL IMPACT
st.markdown("## 👩 Social Impact Layer")

st.info("""
This system enhances energy reliability for critical infrastructure such as hospitals, 
women healthcare facilities, and maternity wards, ensuring safety during grid stress.
""")

st.markdown("---")

# 🔷 CONTROL CENTER
st.markdown("## 🏙️ Smart Grid Control Center")

if critical_count > 0:
    st.error("GRID STATUS: HIGH RISK")
elif warning_count > 0:
    st.warning("GRID STATUS: MEDIUM RISK")
else:
    st.success("GRID STATUS: STABLE")

st.markdown("---")

st.caption("🚀 AI Smart Energy Platform | Government-Ready Infrastructure Monitoring System")
