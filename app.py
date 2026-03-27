import streamlit as st
import pandas as pd
import numpy as np

# 🔷 PAGE CONFIG
st.set_page_config(page_title="Smart Energy AI", layout="wide")

# 🎨 PREMIUM UI CSS
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}

/* Center login box */
.login-box {
    background: rgba(255, 255, 255, 0.05);
    padding: 40px;
    border-radius: 15px;
    width: 350px;
    margin: auto;
    margin-top: 100px;
    box-shadow: 0 0 25px rgba(0,0,0,0.5);
}

/* Inputs */
input {
    background-color: #1e1e2f !important;
    color: white !important;
    border-radius: 8px !important;
}

/* Button */
.stButton>button {
    width: 100%;
    border-radius: 10px;
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    font-weight: bold;
}

/* Title */
.title {
    text-align: center;
    font-size: 30px;
    font-weight: bold;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# 🔐 LOGIN FUNCTION
def login():
    st.markdown('<div class="login-box">', unsafe_allow_html=True)

    st.markdown('<div class="title">⚡ Smart Energy Login</div>', unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state["logged_in"] = True
            st.success("Login successful ✅")
            st.rerun()
        else:
            st.error("Invalid credentials ❌")

    st.markdown('</div>', unsafe_allow_html=True)


# 🔑 SESSION STATE
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# 🚫 STOP IF NOT LOGGED IN
if not st.session_state["logged_in"]:
    login()
    st.stop()

# 🔷 DASHBOARD STARTS
st.title("⚡ AI Smart Energy Command Center")
st.markdown("---")

# 📂 FILE UPLOAD
st.sidebar.title("📂 Upload Dataset")

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV or Excel file", type=["csv", "xlsx"]
)

# 📥 LOAD DATA
if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file, engine="openpyxl")
    except Exception as e:
        st.error(f"Error: {e}")
        st.stop()
else:
    st.warning("Upload dataset to continue")
    st.stop()

# ✅ CHECK
if 'MW' not in df.columns:
    st.error("Dataset must contain 'MW'")
    st.stop()

# 🔁 SIMULATION
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

# 📊 METRICS
col1, col2, col3 = st.columns(3)
col1.metric("Avg Load", round(df['MW'].mean(), 2))
col2.metric("Max Load", round(df['MW'].max(), 2))
col3.metric("Min Load", round(df['MW'].min(), 2))

st.markdown("---")

# 📈 GRAPH
st.line_chart(df['MW'])

# 🚨 ALERT
critical = (df[[t+'_status' for t in ['T1','T2','T3','T4','T5']]] == "CRITICAL").sum().sum()

if critical > 5:
    st.error("🚨 HIGH RISK")
else:
    st.success("✅ STABLE")

st.markdown("---")

# ⚠️ PROBLEMS + SOLUTIONS
st.subheader("⚠️ Problems & Solutions")

for t in ['T1','T2','T3','T4','T5']:
    status = df[t + '_status'].iloc[-1]

    if status == "CRITICAL":
        st.error(f"{t}: Overload → Reduce load immediately")
    elif status == "WARNING":
        st.warning(f"{t}: Risk → Monitor closely")
    else:
        st.success(f"{t}: Normal")

st.markdown("---")

st.caption("🚀 Premium Smart Energy System")
