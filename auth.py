import streamlit as st
import hashlib

# Hardcoded clinician credentials (hashed for security)
CLINICIANS = {
    "clinician1": hashlib.sha256("Pass1234".encode()).hexdigest(),
    "clinician2": hashlib.sha256("Admin2024".encode()).hexdigest(),
    "nurseA": hashlib.sha256("Nurse@2024".encode()).hexdigest(),
}

def check_login(username, password):
    """Check user credentials using SHA-256 hashing."""
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return username in CLINICIANS and CLINICIANS[username] == hashed

def login_screen():
    """Render login UI."""
    st.title("🔐 Clinician Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if check_login(username, password):
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.rerun()
        else:
            st.error("❌ Invalid username or password.")

def require_login():
    """Protects all screens — user must log in first."""
    if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
        login_screen()
        st.stop()

def logout_button():
    """Logout button in sidebar."""
    st.sidebar.markdown("---")
    if st.sidebar.button("🚪 Logout"):
        st.session_state["logged_in"] = False
        st.rerun()
