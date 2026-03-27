import streamlit as st
import base64
import os

st.set_page_config(page_title="Login", layout="centered")

# 🔐 Session state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if st.session_state["logged_in"]:
    st.switch_page("app.py")
    st.stop()

# 🔥 Background + Proper Blur Layer
def add_bg_from_local(image_file):
    # Check if the file exists
    if not os.path.exists(image_file):
        st.error(f"Background image {image_file} not found. Using fallback background.")
        return False
    
    try:
        with open(image_file, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
        
        st.markdown(
            f"""
            <style>
            /* 🌆 Background (z-index: 0) */
            .stApp {{
                background-image: url("data:image/jpg;base64,{encoded}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                position: relative;
                z-index: 0;
            }}

            /* Fallback background color */
            body {{
                background-color: #1a2b4a;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
        return True
    except Exception as e:
        st.error(f"Error loading background image: {str(e)}")
        return False

# Apply background or fallback
if not add_bg_from_local("background.jpg"):
    # Apply fallback CSS if image loading fails
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, #1a2b4a 0%, #2c3e50 100%);
            position: relative;
            z-index: 0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Apply the rest of the styling
st.markdown(
    """
    <style>
    /* 🔥 BLUR LAYER (z-index: 1) - Between background and content */
    .blur-layer {
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

    /* 🧾 CONTENT LAYER (z-index: 2) - Above blur */
    .main .block-container {
        position: relative;
        z-index: 2;
        background: transparent;
        padding-top: 2rem;
    }

    /* Hide streamlit default elements */
    header, footer {
        visibility: hidden;
    }

    /* 🔮 LOGIN CARD */
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
    }

    /* ✨ INPUTS */
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

    /* 🚀 BUTTON */
    .stButton button {
        background: rgba(255,255,255,0.25);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.4);
        border-radius: 12px;
        color: white;
        font-weight: 600;
        transition: 0.3s;
    }

    .stButton button:hover {
        background: rgba(255,255,255,0.4);
        transform: translateY(-2px);
    }
    </style>

    <!-- ✅ BLUR LAYER -->
    <div class="blur-layer"></div>
    """,
    unsafe_allow_html=True
)

# 🧾 Layout
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

st.markdown("<br>")
st.caption("⚡ Smart Energy Monitoring System | AI Powered")
