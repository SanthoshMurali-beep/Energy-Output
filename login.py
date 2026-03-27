import streamlit as st

# Page config
st.set_page_config(page_title="Smart Energy Login", layout="wide")

# 🔥 CUSTOM CSS (Premium UI)
st.markdown("""
<style>
body {
    background-color: #0e1117;
}

.main {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}

.login-container {
    display: flex;
    height: 100vh;
}

.left {
    flex: 1;
    background: url("https://images.unsplash.com/photo-1509395176047-4a66953fd231") no-repeat center;
    background-size: cover;
}

.right {
    flex: 1;
    display: flex;
    justify-content: center;
    align-items: center;
}

.card {
    background: rgba(255,255,255,0.05);
    padding: 40px;
    border-radius: 15px;
    backdrop-filter: blur(10px);
    width: 350px;
}

.title {
    font-size: 28px;
    font-weight: bold;
    color: white;
    margin-bottom: 20px;
}

.stTextInput>div>div>input {
    background-color: #1e1e2f;
    color: white;
    border-radius: 8px;
}

.stButton>button {
    width: 100%;
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    border-radius: 8px;
    padding: 10px;
    font-size: 16px;
}

</style>
""", unsafe_allow_html=True)

# Layout
col1, col2 = st.columns([1,1])

# LEFT SIDE (Image feel)
with col1:
    st.image("https://images.unsplash.com/photo-1509395176047-4a66953fd231", use_container_width=True)

# RIGHT SIDE (Login)
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown('<div class="title">⚡ Smart Energy Login</div>', unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.success("Login Successful ✅")
            st.session_state["logged_in"] = True
        else:
            st.error("Invalid credentials ❌")

    st.markdown('</div>', unsafe_allow_html=True)

# Redirect after login
if st.session_state.get("logged_in"):
    st.switch_page("app.py")  # your main dashboard
