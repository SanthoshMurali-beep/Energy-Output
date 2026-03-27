import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Smart Energy Login",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# Custom CSS for styling
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Inline CSS to avoid file dependency
st.markdown("""
<style>
/* Hide Streamlit elements */
#MainMenu, footer, header, .stDeployButton {
    visibility: hidden;
    height: 0;
}

/* Main app background */
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    background-attachment: fixed;
}

/* Container styling */
.main .block-container {
    padding-top: 3rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

/* Column spacing */
div[data-testid="column"] {
    padding: 0 10px;
}

/* Image container */
.image-container {
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

/* Login card */
.login-card {
    background: rgba(255,255,255,0.08);
    padding: 45px 35px;
    border-radius: 20px;
    backdrop-filter: blur(15px);
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    border: 1px solid rgba(255, 255, 255, 0.18);
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

/* Title styling */
.title {
    font-size: 32px;
    font-weight: 700;
    color: white;
    margin-bottom: 30px;
    text-align: center;
    letter-spacing: 0.5px;
}

/* Input styling */
.stTextInput > label {
    color: #a0a0a0;
    font-weight: 500;
    margin-bottom: 5px;
}

.stTextInput > div > div > input {
    background-color: rgba(30, 30, 47, 0.7);
    color: white;
    border-radius: 10px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 12px 15px;
    font-size: 16px;
}

/* Button styling */
.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    border-radius: 10px;
    padding: 14px;
    font-size: 16px;
    font-weight: 600;
    border: none;
    margin-top: 15px;
    box-shadow: 0 4px 15px rgba(0, 114, 255, 0.3);
}

/* Info card */
.info-card {
    background: rgba(255,255,255,0.05);
    padding: 40px 30px;
    border-radius: 20px;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

/* Alert styling */
.stAlert {
    border-radius: 10px;
    margin-top: 15px;
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)

# Redirect if already logged in
if st.session_state.get("logged_in"):
    st.switch_page("app.py")

# Create three columns for layout
col1, col2, col3 = st.columns([1, 1, 1])

# Left column - Image
with col1:
    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    try:
        st.image(
            "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?ixlib=rb-4.0.3&auto=format&fit=crop&w=1770&q=80",
            use_container_width=True,
            caption="Smart Grid Technology"
        )
    except:
        # Fallback if image fails to load
        st.markdown("""
        <div style="background: rgba(255,255,255,0.05); padding: 40px; border-radius: 15px; height: 100%; display: flex; align-items: center; justify-content: center;">
            <div style="text-align: center; color: white;">
                <div style="font-size: 60px;">⚡</div>
                <p>Smart Grid Technology</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Middle column - Login Form
with col2:
    st.markdown('<div class="login-card">', unsafe_allow_html=True)
    st.markdown('<div class="title">⚡ Smart Energy Login</div>', unsafe_allow_html=True)
    
    username = st.text_input("Username", key="username", placeholder="Enter your username")
    password = st.text_input("Password", type="password", key="password", placeholder="Enter your password")
    
    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.success("Login Successful ✅")
            st.session_state["logged_in"] = True
            st.rerun()
        else:
            st.error("Invalid credentials ❌")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Right column - Information
with col3:
    st.markdown('<div class="info-card">', unsafe_allow_html=True)
    st.markdown("""
    <h3 style="color: white; margin-top: 0; margin-bottom: 20px; font-weight: 600; font-size: 24px;">Welcome to Smart Energy</h3>
    <p style="color: #a0a0a0; margin-bottom: 30px; line-height: 1.6;">Monitor and manage your energy grid with AI-powered insights.</p>
    
    <div style="display: flex; align-items: center; margin-bottom: 20px; color: white;">
        <div style="font-size: 28px; margin-right: 15px; width: 40px; text-align: center;">🔒</div>
        <div style="font-size: 16px;">Secure Access</div>
    </div>
    
    <div style="display: flex; align-items: center; margin-bottom: 20px; color: white;">
        <div style="font-size: 28px; margin-right: 15px; width: 40px; text-align: center;">📊</div>
        <div style="font-size: 16px;">Real-time Monitoring</div>
    </div>
    
    <div style="display: flex; align-items: center; color: white;">
        <div style="font-size: 28px; margin-right: 15px; width: 40px; text-align: center;">🤖</div>
        <div style="font-size: 16px;">AI-Powered Insights</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
