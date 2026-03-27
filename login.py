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

# 🔥 FUNCTION: Background + Strong Glass UI
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

        /* 🔮 MAIN GLASS CARD (STRONG BLUR) */
        .login-box {{
            background: rgba(30, 60, 120, 0.5);  /* almost solid */

            backdrop-filter: blur(55px) saturate(180%);
            -webkit-backdrop-filter: blur(55px) saturate(180%);

            padding: 45px;
            border-radius: 22px;

            border: 1px solid rgba(255, 255, 255, 0.35);

            box-shadow: 
                0 12px 45px rgba(0,0,0,0.45),
                inset 0 1px 0 rgba(255,255,255,0.4);

            color: white;
        }}

        /* ✨ INPUT FIELDS */
        .stTextInput > div > div > input {{
            background: rgba(255, 255, 255, 0.35);
            backdrop-filter: blur(25px);
            -webkit-backdrop-filter: blur(25px);

            border: 1px solid rgba(255,255,255,0.5);
            border-radius: 12px;

            padding: 12px;
            color: #ffffff;
            font-weight: 500;
        }}

        /* ✨ INPUT FOCUS */
        .stTextInput > div > div > input:focus {{
            outline: none;
            border: 1px solid rgba(255,255,255,0.7);
            box-shadow: 
                0 0 0 2px rgba(255,255,255,0.25);
        }}

        /* 👁 Placeholder */
        .stTextInput input::placeholder {{
            color: rgba(255,255,255,0.9);
        }}

        /* fix password icon bg */
        .stTextInput div[data-baseweb="input"] {{
            background: transparent;
        }}

        /* 🚀 BUTTON */
        .stButton button {{
            background: rgba(255,255,255,0.25);
            backdrop-filter: blur(15px);

            border: 1px solid rgba(255,255,255,0.4);
            border-radius: 12px;

            color: white;
            font-weight: 600;
            height: 3em;
            width: 100%;

            transition: 0.3s ease;
        }}

        .stButton button:hover {{
            background: rgba(255,255,255,0.4);
            transform: translateY(-2px);
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

# 📸 Add background
add_bg_from_local("background.jpg")

# 🧾 Layout
st.markdown("<br><br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown('<div class="login-box">', unsafe_allow_html=True)

    st.markdown("### 🔐 Smart Energy Login")
    st.caption("AI Digital Twin Dashboard")

    username = st.text_input("👤 Username", placeholder="Enter your username")
    password = st.text_input("🔑 Password", type="password", placeholder="Enter your password")

    VALID_USERNAME = "admin"
    VALID_PASSWORD = "1234"

    if st.button("🚀 Sign in"):
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            st.session_state["logged_in"] = True
            st.success("Login successful!")
            st.switch_page("app.py")
        else:
            st.error("Invalid credentials")

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.caption("⚡ Smart Energy Monitoring System | AI Powered")
