import streamlit as st
import base64

st.set_page_config(page_title="Login", layout="centered")

# 🔐 Session state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# 🎯 Redirect if already logged in
if st.session_state["logged_in"]:
    st.switch_page("app.py")
    st.stop()

# 🔥 FUNCTION: Add background image with glassmorphism styling
def add_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        /* 🌆 Background */
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}

        /* 🌙 Dark overlay for readability */
        .stApp::before {{
            content: "";
            position: fixed;
            inset: 0;
            background: rgba(0,0,0,0.35);
            z-index: -1;
        }}

        /* 🔮 Glass login container */
        .login-box {{
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            padding: 40px;
            border-radius: 20px;
            border: 1px solid rgba(255,255,255,0.2);
            box-shadow: 0 8px 32px rgba(0,0,0,0.4);
            color: white;
        }}

        /* ✨ Glass input fields */
        .stTextInput > div > div > input {{
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.3);
            border-radius: 12px;
            padding: 12px;
            color: white;
            font-weight: 500;
        }}

        /* 👁 Placeholder styling */
        .stTextInput input::placeholder {{
            color: rgba(255,255,255,0.7);
        }}

        /* 🔑 Remove weird background behind password icon */
        .stTextInput div[data-baseweb="input"] {{
            background: transparent;
        }}

        /* 🚀 Button styling */
        .stButton button {{
            background: linear-gradient(135deg, #00c6ff, #0072ff);
            color: white;
            border-radius: 12px;
            height: 3em;
            width: 100%;
            border: none;
            font-weight: 600;
            box-shadow: 0 4px 15px rgba(0, 114, 255, 0.4);
            transition: all 0.3s ease;
        }}

        .stButton button:hover {{
            transform: scale(1.05);
            box-shadow: 0 6px 25px rgba(0, 114, 255, 0.6);
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

# 📸 Add background image
add_bg_from_local("background.jpg")

# 🧾 UI Layout
st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown('<div class="login-box">', unsafe_allow_html=True)

    st.title("🔐 Smart Energy Login")
    st.caption("AI Digital Twin Dashboard")

    username = st.text_input("👤 Username", placeholder="Enter your username")
    password = st.text_input("🔑 Password", type="password", placeholder="Enter your password")

    VALID_USERNAME = "admin"
    VALID_PASSWORD = "1234"

    if st.button("🚀 Login"):
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            st.session_state["logged_in"] = True
            st.success("Login successful!")
            st.switch_page("app.py")
        else:
            st.error("Invalid credentials")

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.caption("⚡ Smart Energy Monitoring System | AI Powered")
