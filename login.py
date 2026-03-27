import streamlit as st

st.set_page_config(page_title="Login", layout="centered")

# 🔐 Initialize session state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# 🎯 If already logged in → redirect to main app
if st.session_state["logged_in"]:
    st.success("✅ Already logged in!")
    st.switch_page("app.py")  # Make sure filename matches
    st.stop()

# 🧾 LOGIN UI
st.title("🔐 Smart Energy Dashboard Login")
st.markdown("---")

username = st.text_input("👤 Username")
password = st.text_input("🔑 Password", type="password")

# 🔑 Dummy credentials (you can change)
VALID_USERNAME = "admin"
VALID_PASSWORD = "1234"

# 🔘 Login button
if st.button("Login"):
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        st.session_state["logged_in"] = True
        st.success("🎉 Login Successful!")
        st.switch_page("app.py")  # redirect to main app
    else:
        st.error("❌ Invalid username or password")

st.markdown("---")
st.caption("AI Smart Energy System 🚀")
