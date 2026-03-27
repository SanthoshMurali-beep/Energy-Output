import streamlit as st

# Page config
st.set_page_config(page_title="Smart Energy Login", layout="wide")

# 🔥 CLEAN CSS (removed dark box issue)
st.markdown("""
<style>

body {
    background-color: #0e1117;
}

.main {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}

/* Remove extra container spacing */
.block-container {
    padding-top: 2rem;
}

/* Card styling */
.card {
    background: rgba(255,255,255,0.05);
    padding: 40px;
    border-radius: 15px;
    backdrop-filter: blur(10px);
}

/* Title */
.title {
    font-size: 30px;
    font-weight: bold;
    color: white;
    margin-bottom: 20px;
}

/* Inputs */
.stTextInput>div>div>input {
    background-color: #1e1e2f;
    color: white;
    border-radius: 8px;
    border: 1px solid #333;
}

/* Button */
.stButton>button {
    width: 100%;
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    border-radius: 8px;
    padding: 10px;
    font-size: 16px;
    border: none;
}

</style>
""", unsafe_allow_html=True)

# Layout
col1, col2 = st.columns([1.2, 1])

# 🔥 LEFT SIDE (PROJECT-RELATED IMAGE)
with col1:
    st.image(
        "https://images.unsplash.com/photo-1581091870627-3c7c0baf7f5d",  # energy / smart grid image
        use_container_width=True
    )

# 🔥 RIGHT SIDE (LOGIN FORM)
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown('<div class="title">⚡ Smart Energy Login</div>', unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.success("Login Successful ✅")
            st.session_state["logged_in"] = True
            st.rerun()
        else:
            st.error("Invalid credentials ❌")

    st.markdown('</div>', unsafe_allow_html=True)

# Redirect
if st.session_state.get("logged_in"):
    st.switch_page("app.py")
