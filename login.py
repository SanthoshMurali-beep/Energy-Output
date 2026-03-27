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

# 🔥 FUNCTION: Add background image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}

        /* Glass effect login box */
        .login-box {{
            background: rgba(0, 0, 0, 0.6);
            padding: 40px;
            border-radius: 15px;
            color: white;
        }}

        .stTextInput > div > div > input {{
            background-color: rgba(255,255,255,0.9);
            color: black;
        }}

        .stButton button {{
            background-color: #00c6ff;
            color: white;
            border-radius: 10px;
            height: 3em;
            width: 100%;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# 📸 Add your background image here
add_bg_from_local("background.jpg")   # Put image in same folder

# 🧾 UI Layout
st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.markdown('<div class="login-box">', unsafe_allow_html=True)

    st.title("🔐 Smart Energy Login")
    st.caption("AI Digital Twin Dashboard")

    username = st.text_input("👤 Username")
    password = st.text_input("🔑 Password", type="password")

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
