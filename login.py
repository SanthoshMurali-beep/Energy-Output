import streamlit as st

# Page config
st.set_page_config(page_title="Smart Energy Login", layout="wide")

# 🔥 CLEAN CSS (removed dark box issue)
st.markdown("""
<style>
/* Main background */
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}

/* Remove extra container spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Card styling */
.login-card {
    background: rgba(255,255,255,0.08);
    padding: 40px;
    border-radius: 15px;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    border: 1px solid rgba(255, 255, 255, 0.18);
}

/* Title */
.title {
    font-size: 30px;
    font-weight: bold;
    color: white;
    margin-bottom: 25px;
    text-align: center;
}

/* Input labels */
.stTextInput > label {
    color: #a0a0a0;
}

/* Inputs */
.stTextInput > div > div > input {
    background-color: rgba(30, 30, 47, 0.7);
    color: white;
    border-radius: 8px;
    border: 1px solid #333;
}

/* Button */
.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    border-radius: 8px;
    padding: 10px;
    font-size: 16px;
    border: none;
    font-weight: bold;
    transition: all 0.3s ease;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #0072ff, #00c6ff);
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0, 114, 255, 0.4);
}

/* Success/Error messages */
.stAlert {
    border-radius: 8px;
    margin-top: 15px;
}

/* Hide streamlit branding */
footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# Layout
col1, col2, col3 = st.columns([1, 1.2, 1])

# 🔥 LEFT SIDE (PROJECT-RELATED IMAGE)
with col1:
    # Using a more reliable image source with fallback
    try:
        st.image(
            "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80",
            use_container_width=True,
            caption="Smart Grid Technology"
        )
    except:
        # Fallback if image fails to load
        st.markdown("""
        <div style="background: rgba(255,255,255,0.05); padding: 40px; border-radius: 15px; height: 300px; display: flex; align-items: center; justify-content: center;">
            <div style="text-align: center; color: white;">
                <div style="font-size: 60px;">⚡</div>
                <p>Smart Grid Technology</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# 🔥 CENTER (LOGIN FORM)
with col2:
    st.markdown('<div class="login-card">', unsafe_allow_html=True)

    st.markdown('<div class="title">⚡ Smart Energy Login</div>', unsafe_allow_html=True)

    username = st.text_input("Username", key="username")
    password = st.text_input("Password", type="password", key="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.success("Login Successful ✅")
            st.session_state["logged_in"] = True
            st.rerun()
        else:
            st.error("Invalid credentials ❌")

    st.markdown('</div>', unsafe_allow_html=True)

# 🔥 RIGHT SIDE (ADDITIONAL INFO)
with col3:
    st.markdown("""
    <div style="background: rgba(255,255,255,0.05); padding: 30px; border-radius: 15px; height: 100%;">
        <h3 style="color: white; margin-top: 0;">Welcome to Smart Energy</h3>
        <p style="color: #a0a0a0;">Monitor and manage your energy grid with AI-powered insights.</p>
        <div style="margin-top: 30px;">
            <div style="color: white; margin-bottom: 15px;">
                <span style="font-size: 24px; margin-right: 10px;">🔒</span> Secure Access
            </div>
            <div style="color: white; margin-bottom: 15px;">
                <span style="font-size: 24px; margin-right: 10px;">📊</span> Real-time Monitoring
            </div>
            <div style="color: white;">
                <span style="font-size: 24px; margin-right: 10px;">🤖</span> AI-Powered Insights
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Redirect
if st.session_state.get("logged_in"):
    st.switch_page("app.py")
