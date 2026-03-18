import streamlit as st

from auth import login_screen, logout_button, require_login
from ui_tabs import demographic_tab, clinical_tab, phq9_tab, psychosocial_tab
from prediction import predict_risk, build_feature_dict
from pdf_reports import generate_pdf_report
from alerts import send_alert
from database import save_screening_to_db
from dashboard import admin_dashboard
from config import ADMINS


# ---------------------- PAGE CONFIG -------------------------
st.set_page_config(
    page_title="AI Depression Screening Tool for PLHIV",
    page_icon="🧠",
    layout="wide",
)

# ---------------------- AUTH CHECK ---------------------------
require_login()

st.sidebar.image("assets/logo.png", width=160)
logout_button()

username = st.session_state["username"]

# ---------------------- TITLE -------------------------------
st.title("🧠 AI Depression Screening Tool for PLHIV")
st.write("Use each tab below to enter patient information.")

# ---------------------- TABS -------------------------------
tabs = st.tabs([
    "🧍 Demographics",
    "🧬 Clinical Info",
    "📝 PHQ‑9",
    "🌱 Psychosocial Factors",
    "📊 Admin Dashboard",
])

# ---------------------- DEMOGRAPHICS TAB ---------------------
with tabs[0]:
    demographic_inputs = demographic_tab()

# ---------------------- CLINICAL TAB --------------------------
with tabs[1]:
    clinical_inputs = clinical_tab()

# ---------------------- PHQ‑9 TAB -----------------------------
with tabs[2]:
    phq_inputs = phq9_tab()

# ---------------------- PSYCHOSOCIAL TAB ---------------------
with tabs[3]:
    psychosocial_inputs = psychosocial_tab()


# ---------------------- PREDICT BUTTON -----------------------
if st.button("🔍 Predict Depression Risk", type="primary"):

    # Combine all collected data
    feature_dict = build_feature_dict(
        demographic_inputs,
        clinical_inputs,
        phq_inputs,
        psychosocial_inputs,
        username
    )

    # Run AI prediction
    risk, action = predict_risk(feature_dict)

    # Display results
    st.header(f"📊 Depression Risk Score: **{risk:.3f}**")
    st.subheader(f"📌 Recommended Action:\n{action}")

    # Save to DB
    save_screening_to_db(feature_dict, risk, action)
    st.success("✅ Screening saved to database.")

    # Alert if very high risk
    if risk >= 0.80:
        st.error("⚠️ VERY HIGH RISK — Patient requires urgent attention!")
        phone = st.text_input("Enter WhatsApp/SMS Contact Number (e.g. whatsapp:+233XXXXXXXXX):")

        if st.button("📲 Send Emergency Alert"):
            sid = send_alert(phone, risk, action)
            st.success(f"Alert sent! (Message SID: {sid})")

    # PDF option
    if st.button("📄 Generate PDF Report"):
        pdf_path = generate_pdf_report(feature_dict, risk, action)
        with open(pdf_path, "rb") as f:
            st.download_button(
                label="Download PDF Report",
                data=f,
                file_name="depression_risk_report.pdf"
            )


# ---------------------- ADMIN DASHBOARD -----------------------
with tabs[4]:
    if username in ADMINS:
        admin_dashboard()
    else:
        st.error("You do not have permission to view the admin dashboard.")
