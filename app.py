import streamlit as st
import pandas as pd
import numpy as np

# 🔷 PAGE CONFIG
st.set_page_config(page_title="Smart Energy AI", layout="wide")

# 🎨 DARK UI
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
</style>
""", unsafe_allow_html=True)

# 🔷 HEADER
st.title("⚡ AI Smart Energy Command Center")
st.markdown("---")

# 🔷 SIDEBAR
st.sidebar.title("📂 Upload Dataset")

uploaded_file = st.sidebar.file_uploader(
    "Upload Dataset", type=["csv", "xlsx"]
)

# 🔷 DATA LOADING
if uploaded_file is not None:

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)

    elif uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file, engine="openpyxl")

else:
    st.warning("Upload dataset to continue")
    st.stop()

# ✅ COLUMN CHECK
if 'MW' not in df.columns:
    st.error("Dataset must contain 'MW' column")
    st.stop()

# 🔁 SIMULATED LIVE DATA
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

# 🔷 RISK FUNCTION
def check_risk(x):
    if x > 1.0:
        return "CRITICAL"
    elif x > 0.7:
        return "WARNING"
    else:
        return "SAFE"

for t in ['T1','T2','T3','T4','T5']:
    df[t + '_status'] = df[t].apply(check_risk)

# 🔷 METRICS
st.subheader("📊 System Overview")

col1, col2, col3 = st.columns(3)
col1.metric("Avg Load", round(df['MW'].mean(), 2))
col2.metric("Max Load", round(df['MW'].max(), 2))
col3.metric("Min Load", round(df['MW'].min(), 2))

st.markdown("---")

# 🔷 GRAPH
st.subheader("📈 Energy Trend")
st.line_chart(df['MW'])

st.markdown("---")

# 🔷 ALERTS
st.subheader("🚨 Alerts")

critical_count = (df[[t+'_status' for t in ['T1','T2','T3','T4','T5']]] == "CRITICAL").sum().sum()
warning_count = (df[[t+'_status' for t in ['T1','T2','T3','T4','T5']]] == "WARNING").sum().sum()

if critical_count > 5:
    st.error("HIGH RISK GRID")
elif warning_count > 5:
    st.warning("MODERATE RISK")
else:
    st.success("SYSTEM STABLE")

st.markdown("---")

# 🔷 TRANSFORMERS
st.subheader("⚡ Transformer Data")

col1, col2 = st.columns(2)

with col1:
    st.dataframe(df[['T1','T2','T3','T4','T5']])

with col2:
    st.dataframe(df[['T1_status','T2_status','T3_status','T4_status','T5_status']])

st.markdown("---")

# 🔷 AI INSIGHTS
st.subheader("🧠 AI Insights")

avg = df['MW'].mean()
maxv = df['MW'].max()

if maxv > 4.5:
    st.error("Heatwave Condition")
elif avg > 3.5:
    st.warning("Peak Demand")
else:
    st.success("Normal Condition")

# 🔷 ANOMALY
spikes = df[df['MW'] > (avg + 2*df['MW'].std())]

if not spikes.empty:
    st.warning(f"{len(spikes)} anomalies detected")
else:
    st.success("No anomalies")

st.markdown("---")

# 🔷 DECISION SUPPORT
st.subheader("🧠 Decision Support")

if critical_count > 0:
    st.write("✔ Reduce load immediately")
    st.write("✔ Maintenance required")
elif warning_count > 0:
    st.write("✔ Monitor closely")
else:
    st.write("✔ System stable")

st.markdown("---")

# 🔷 CONTROL CENTER
st.subheader("🏙️ Grid Status")

if critical_count > 0:
    st.error("HIGH RISK")
elif warning_count > 0:
    st.warning("MEDIUM RISK")
else:
    st.success("LOW RISK")

st.markdown("---")

st.caption("🚀 AI Smart Energy Monitoring System")
