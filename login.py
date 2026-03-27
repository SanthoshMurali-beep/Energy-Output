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

# 🔥 FUNCTION: Add background + premium glass UI
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

        /* 🔮 MAIN GLASS CARD */
        .login-box {{
            background: rgba(255, 255, 255, 0.12);
            backdrop-filter: blur(25px) saturate(160%);
            -webkit-backdrop-filter: blur(25px) saturate(160%);

            border-radius: 20px;
            padding: 40px;

            border: 1px solid rgba(255, 255, 255, 0.25);

            box-shadow: 
                0 8px 32px rgba(0,0,0,0.25),
                inset 0 1px 0 rgba(255,255,255,0.3);

            color: white;
        }}

        /* ✨ INPUT FIELDS */
        .stTextInput > div > div > input {{
            background: rgba(255, 255, 255, 0.25);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);

            border: 1px solid rgba(255,255,255,0.35);
            border-radius: 10px;

            padding: 12px;
            color: #ffffff;
            font-weight: 500;

            box-shadow: inset 0 1px 2px rgba(0,0,0,0.1);
        }}

        /* ✨ INPUT FOCUS EFFECT */
        .stTextInput > div > div > input:focus {{
            outline: none;
            border: 1px solid rgba(255,255,255,0.6);
            box-shadow: 
                0 0 0 2px rgba(255,255,255,0.2),
                inset 0 1px 2px rgba(0,0,0,0.1);
        }}

        /* 👁 Placeholder */
        .stTextInput input::placeholder {{
            color: rgba(255,255,255,0.85);
        }}

        /* fix password icon background */
        .stTextInput div[data-baseweb="input"] {{
            background: transparent;
        }}

        /* 🚀 BUTTON */
        .stButton button {{
            background: rgba(255,255,255,0.2);
            backdrop-filter: blur(10px);

            border: 1px solid rgba(255,255,255,0.3);
            border-radius: 10px;

            color: white;
            font-weight: 600;
            height: 3em;
            width: 100%;

            transition: 0.3s ease;
        }}

        .stButton button:hover {{
            background: rgba(255,255,255,0.3);
            transform: translateY(-1px);
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

# 📸 Add background image
add_bg_from_local("background.jpg")

# 🧾 Layout spacing
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
