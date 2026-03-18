import streamlit as st
import plotly.express as px
from database import load_all_screenings


def admin_dashboard():
    """
    Full Admin Analytics Dashboard:
    - Total screenings
    - Risk category breakdown
    - Daily screening volume
    - Full screenings table
    """

    st.header("📊 Admin Dashboard — Screening Statistics")

    df = load_all_screenings()

    if df.empty:
        st.warning("No screening records found.")
        return

    # ---------------------------
    # Total count
    # ---------------------------
    st.subheader("📌 Total Screenings")
    st.metric("Total", len(df))

    # ---------------------------
    # Risk category mapping
    # ---------------------------
    df["risk_band"] = ( 
        pd.cut(
            df["risk_score"],
            bins=[-0.01, 0.20, 0.40, 0.60, 0.80, 1.00],
            labels=["Very Low", "Mild", "Moderate", "High", "Very High"]
        )
    )

    # ---------------------------
    # Pie Chart — Risk Distribution
    # ---------------------------
    st.subheader("📈 Risk Category Distribution")
    fig = px.pie(
        df,
        names="risk_band",
        title="Distribution of Depression Risk Categories"
    )
    st.plotly_chart(fig, use_container_width=True)

    # ---------------------------
    # Trend Chart — Screenings Over Time
    # ---------------------------
    st.subheader("📅 Screening Volume Over Time")

    df["date"] = df["timestamp"].dt.date
    trend = df.groupby("date")["id"].count().reset_index(name="screenings")

    fig2 = px.line(
        trend,
        x="date",
        y="screenings",
        markers=True,
        title="Daily Screening Activity"
    )
    st.plotly_chart(fig2, use_container_width=True)

    # ---------------------------
    # Display full table
    # ---------------------------
    st.subheader("📄 All Screening Records")
    st.dataframe(df, use_container_width=True)
