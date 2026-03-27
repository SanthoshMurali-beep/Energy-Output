import streamlit as st
import base64

st.set_page_config(page_title="Login", layout="centered")

# 🔐 Session state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if st.session_state["logged_in"]:
    st.switch_page("app.py")
    st.stop()

# 🔥 Background + Proper Blur Layer
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
            position: relative;
            z-index: 0;
        }}

        /* 🔥 BLUR LAYER (BETWEEN BG & CONTENT) */
        .blur-layer {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;

            backdrop-filter: blur(35px);
            -webkit-backdrop-filter: blur(35px);

            background: rgba(20, 40, 80, 0.25);

            z-index: 1;
        }}

        /* 🧾 CONTENT ABOVE BLUR */
        .content {{
            position: relative;
            z-index: 2;
        }}

        /* 🔮 LOGIN BOX */
        .login-box {{
            background: rgba(255, 255, 255, 0.12);
            backdrop-filter: blur(25px);

            padding: 45px;
            border-radius: 20px;

            border: 1px solid rgba(255,255,255,0.25);

            box-shadow:
                0 10px 40px rgba(0,0,0,0.4),
                inset 0 1px 0 rgba(255,255,255,0.2);

            color: white;
        }}

        /* ✨ INPUT FIELDS */
        .stTextInput > div > div > input {{
            background: rgba(255,255,255,0.25);
            backdrop-filter: blur(15px);

            border: 1px solid rgba(255,255,255,0.4);
            border-radius: 12px;

            color: white;
        }}

        .stTextInput input::placeholder {{
            color: rgba(255,255,255,0.85);
        }}

        .stTextInput div[data-baseweb="input"] {{
            background: transparent;
        }}

        /* 🚀 BUTTON */
        .stButton button {{
            background: rgba(255,255,255,0.25);
            backdrop-filter: blur(10px);

            border: 1px solid rgba(255,255,255,0.4);
            border-radius: 12px;

            color: white;
            font-weight: 600;

            transition: 0.3s;
        }}

        .stButton button:hover {{
            background: rgba(255,255,255,0.4);
            transform: translateY(-2px);
        }}

        </style>

        <!-- ✅ BLUR LAYER -->
        <div class="blur-layer"></div>

        <!-- ✅ CONTENT -->
        <div class="content">
        """,
        unsafe_allow_html=True
    )

# 📸 Apply background
add_bg_from_local("background.jpg")

# 🧾 Layout spacing
st.markdown("<br><br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.markdown('<div class="login-box">', unsafe_allow_html=True)

    st.markdown("### 🔐 Smart Energy Login")
    st.caption("AI Digital Twin Dashboard")

    username = st.text_input("👤 Username", placeholder="Enter your username")
    password = st.text_input("🔑 Password", type="password", placeholder="Enter your password")

    if st.button("🚀 Sign in"):
        if username == "admin" and password == "1234":
            st.session_state["logged_in"] = True
            st.success("Login successful!")
            st.switch_page("app.py")
        else:
            st.error("Invalid credentials")

    st.markdown("</div>", unsafe_allow_html=True)

# ✅ Close content wrapper
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br>")
st.caption("⚡ Smart Energy Monitoring System | AI Powered")
