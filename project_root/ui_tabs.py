import streamlit as st


# --------------------------- Demographic Tab -----------------------------
def demographic_tab():
    col1, col2, col3 = st.columns(3)

    return {
        "Age": col1.number_input("Age", min_value=10, max_value=120, value=30),
        "Sex": col1.selectbox("Sex", ["1", "2"]),
        "Ethnicity": col2.selectbox("Ethnicity", ["1", "2", "3", "4", "5", "6"]),
        "Religion": col2.selectbox("Religion", ["1", "2", "3", "4", "5", "6"]),
        "Marital": col3.selectbox("Marital Status", ["1", "2", "3", "4", "5"]),
        "Education": col3.selectbox("Education Level", ["1", "2", "3", "4"]),
        "Occupation": col3.selectbox("Occupation", ["1", "2", "3", "4", "5", "6", "7"]),
    }


# --------------------------- Clinical Tab -----------------------------
def clinical_tab():
    col1, col2, col3 = st.columns(3)

    return {
        "CD4": col1.number_input("CD4 Count", 1, 1500, 450),
        "ARTDuration": col1.number_input("Months on ART", 0, 360, 24),
        "HIVStage": col1.selectbox("HIV Stage", ["1", "2", "3", "4"]),
        "TBscreen": col2.selectbox("TB Screening Done?", ["1", "0"]),
        "TBresult": col2.selectbox("TB Result", ["1", "0"]),
        "Cough": col3.selectbox("Cough >2 Weeks", ["0", "1"]),
        "NightSweat": col3.selectbox("Night Sweats", ["0", "1"]),
        "Fever": col3.selectbox("Chills/Fever", ["0", "1"]),
        "ChestPain": col3.selectbox("Chest Pain", ["0", "1"]),
        "WeightLoss": col3.selectbox("Weight Loss", ["0", "1"]),
    }


# --------------------------- PHQ-9 Tab -----------------------------
def phq9_tab():
    questions = [
        "Little interest or pleasure in doing things",
        "Feeling down, depressed, or hopeless",
        "Trouble falling or staying asleep",
        "Feeling tired or having little energy",
        "Poor appetite or overeating",
        "Feeling bad about yourself",
        "Trouble concentrating",
        "Moving/speaking slowly or very restless",
        "Thoughts of self-harm",
    ]

    return {f"PHQ{i + 1}": st.selectbox(q, [0, 1, 2, 3]) for i, q in enumerate(questions)}


# --------------------------- Psychosocial Tab -----------------------------
def psychosocial_tab():
    col1, col2, col3 = st.columns(3)

    return {
        "Worry": col1.selectbox("Often worried/anxious?", ["1", "2", "3", "4"]),
        "Loneliness": col1.selectbox("Feel lonely often?", ["1", "2", "3", "4"]),
        "Substance": col2.selectbox("Substance use?", ["0", "1"]),
        "Tobacco": col2.selectbox("Tobacco use?", ["0", "1"]),
        "Stigma": col3.selectbox("Experienced stigma?", ["1", "2", "3", "4"]),
        "Cultural": col3.selectbox("Cultural beliefs affect care?", ["1", "2", "3", "4"]),
    }
