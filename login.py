import streamlit as st
import base64

st.set_page_config(page_title="Login", layout="centered")

# 🔐 Session state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if st.session_state["logged_in"]:
    st.switch_page("app.py")
    st.stop()

# Apply background and styling
st.markdown(
    """
    <style>
    /* Hide Streamlit default elements */
    header, footer, .stDeployButton {
        visibility: hidden;
    }
    
    /* Main container styling */
    .stApp {
        background: linear-gradient(135deg, #1a2b4a 0%, #2c3e50 100%);
        position: relative;
        overflow: hidden;
    }
    
    /* Background image layer */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: url('https://picsum.photos/seed/energy/1920/1080.jpg');
        background-size: cover;
        background-position: center;
        z-index: 0;
        opacity: 0.8;
    }
    
    /* Blur layer */
    .stApp::after {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        background: rgba(20, 40, 80, 0.5);
        z-index: 1;
    }
    
    /* Content layer */
    .main .block-container {
        position: relative;
        z-index: 2;
        padding-top: 2rem;
    }
    
    /* Login card */
    .login-box {
        background: rgba(255,255,255,0.15);
        backdrop-filter: blur(25px);
        padding: 45px;
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.3);
        box-shadow:
            0 10px 40px rgba(0,0,0,0.4),
            inset 0 1px 0 rgba(255,255,255,0.3);
        color: white;
        margin: 0 auto;
        max-width: 500px;
    }
    
    /* Input styling */
    .stTextInput > div > div > input {
        background: rgba(255,255,255,0.3);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255,255,255,0.5);
        border-radius: 12px;
        color: white;
    }
    
    .stTextInput input::placeholder {
        color: rgba(255,255,255,0.9);
    }
    
    .stTextInput div[data-baseweb="input"] {
        background: transparent;
    }
    
    /* Button styling */
    .stButton button {
        background: rgba(255,255,255,0.25);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.4);
        border-radius: 12px;
        color: white;
        font-weight: 600;
        transition: 0.3s;
        width: 100%;
    }
    
    .stButton button:hover {
        background: rgba(255,255,255,0.4);
        transform: translateY(-2px);
    }
    
    /* Center the content */
    .element-container {
        display: flex;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🧾 Layout
st.markdown("<br><br><br>", unsafe_allow_html=True)

# Center the login form
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

st.markdown("<br>")
st.markdown('<div style="text-align: center; color: white;">⚡ Smart Energy Monitoring System | AI Powered</div>', unsafe_allow_html=True)
