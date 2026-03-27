import streamlit as st

# Page config
st.set_page_config(page_title="Smart Energy Login", layout="wide", initial_sidebar_state="collapsed")

# Hide Streamlit default elements
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Premium CSS Styling
st.markdown("""
<style>
/* Main app background */
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    background-attachment: fixed;
}

/* Container adjustments */
.main .block-container {
    padding-top: 3rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

/* Login card styling */
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
    transition: all 0.3s ease;
}

.stTextInput > div > div > input:focus {
    border-color: #00c6ff;
    box-shadow: 0 0 0 2px rgba(0, 198, 255, 0.2);
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
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(0, 114, 255, 0.3);
}

.stButton > button:hover {
    background: linear-gradient(90deg, #0072ff, #00c6ff);
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0, 114, 255, 0.4);
}

/* Info card styling */
.info-card {
    background: rgba(255,255,255,0.05);
    padding: 40px 30px;
    border-radius: 20px;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.info-card h3 {
    color: white;
    margin-top: 0;
    margin-bottom: 20px;
    font-weight: 600;
    font-size: 24px;
}

.info-card p {
    color: #a0a0a0;
    margin-bottom: 30px;
    line-height: 1.6;
}

.feature-item {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
    color: white;
}

.feature-icon {
    font-size: 28px;
    margin-right: 15px;
    width: 40px;
    text-align: center;
}

.feature-text {
    font-size: 16px;
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

.image-container img {
    width: 100%;
    height: auto;
    display: block;
    object-fit: cover;
}

/* Alert styling */
.stAlert {
    border-radius: 10px;
    margin-top: 15px;
    font-weight: 500;
}

/* Spacing between columns */
div[data-testid="column"] {
    padding: 0 10px;
}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# Create a centered layout with proper columns
col1, col2, col3 = st.columns([1, 1, 1])

# LEFT SIDE (PROJECT-RELATED IMAGE)
with col1:
    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    try:
        st.image(
            "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80",
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

# CENTER (LOGIN FORM)
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

# RIGHT SIDE (ADDITIONAL INFO)
with col3:
    st.markdown("""
    <div class="info-card">
        <h3>Welcome to Smart Energy</h3>
        <p>Monitor and manage your energy grid with AI-powered insights.</p>
        
        <div class="feature-item">
            <div class="feature-icon">🔒</div>
            <div class="feature-text">Secure Access</div>
        </div>
        
        <div class="feature-item">
            <div class="feature-icon">📊</div>
            <div class="feature-text">Real-time Monitoring</div>
        </div>
        
        <div class="feature-item">
            <div class="feature-icon">🤖</div>
            <div class="feature-text">AI-Powered Insights</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Redirect if logged in
if st.session_state.get("logged_in"):
    st.switch_page("app.py")
