import streamlit as st
import psycopg2
import pandas as pd

def get_connection():
    """Connect to PostgreSQL using Streamlit secrets."""
    return psycopg2.connect(
        host=st.secrets["postgres"]["host"],
        port=st.secrets["postgres"]["port"],
        database=st.secrets["postgres"]["database"],
        user=st.secrets["postgres"]["user"],
        password=st.secrets["postgres"]["password"],
    )

def save_screening_to_db(inputs, risk, action):
    """Store a single screening result into the PostgreSQL database."""
    conn = get_connection()
    cur = conn.cursor()

    query = """
        INSERT INTO screenings (
            clinician, age, sex, ethnicity, religion, marital_status, education, occupation,
            cd4, art_duration, hiv_stage, tb_screen, tb_result, cough, night_sweat, fever,
            chest_pain, weight_loss, phq1, phq2, phq3, phq4, phq5, phq6, phq7, phq8, phq9,
            worry, loneliness, substance, tobacco, stigma, cultural, risk_score, recommended_action
        ) VALUES (
            %(clinician)s, %(Age)s, %(Sex)s, %(Ethnicity)s, %(Religion)s, %(Marital)s,
            %(Education)s, %(Occupation)s, %(CD4)s, %(ARTDuration)s, %(HIVStage)s,
            %(TBscreen)s, %(TBresult)s, %(Cough)s, %(NightSweat)s, %(Fever)s,
            %(ChestPain)s, %(WeightLoss)s, %(PHQ1)s, %(PHQ2)s, %(PHQ3)s, %(PHQ4)s,
            %(PHQ5)s, %(PHQ6)s, %(PHQ7)s, %(PHQ8)s, %(PHQ9)s, %(Worry)s, %(Loneliness)s,
            %(Substance)s, %(Tobacco)s, %(Stigma)s, %(Cultural)s, %(RiskScore)s, %(Action)s
        );
    """

    inputs["RiskScore"] = risk
    inputs["Action"] = action

    cur.execute(query, inputs)
    conn.commit()
    cur.close()
    conn.close()

def load_all_screenings():
    """Load all screening entries for the admin dashboard."""
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM screenings ORDER BY timestamp DESC;", conn)
    conn.close()
    return df
