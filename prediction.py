import pandas as pd
from model_loader import load_model
from config import decision_engine

# Load AI/ML model from models/best_model.pkl
model = load_model()

def build_feature_dict(demographic, clinical, phq, psychosocial, clinician_username):
    """
    Combine all input dictionaries into a unified feature dictionary.
    """
    combined = {
        "clinician": clinician_username,

        # Demographics
        "Age": demographic["Age"],
        "Sex": demographic["Sex"],
        "Ethnicity": demographic["Ethnicity"],
        "Religion": demographic["Religion"],
        "Marital": demographic["Marital"],
        "Education": demographic["Education"],
        "Occupation": demographic["Occupation"],

        # Clinical
        "CD4": clinical["CD4"],
        "ARTDuration": clinical["ARTDuration"],
        "HIVStage": clinical["HIVStage"],
        "TBscreen": clinical["TBscreen"],
        "TBresult": clinical["TBresult"],
        "Cough": clinical["Cough"],
        "NightSweat": clinical["NightSweat"],
        "Fever": clinical["Fever"],
        "ChestPain": clinical["ChestPain"],
        "WeightLoss": clinical["WeightLoss"],
    }

    # Add PHQ‑9 items
    for i in range(1, 10):
        combined[f"PHQ{i}"] = phq[f"PHQ{i}"]

    # Add psychosocial variables
    combined.update({
        "Worry": psychosocial["Worry"],
        "Loneliness": psychosocial["Loneliness"],
        "Substance": psychosocial["Substance"],
        "Tobacco": psychosocial["Tobacco"],
        "Stigma": psychosocial["Stigma"],
        "Cultural": psychosocial["Cultural"],
    })

    return combined


def predict_risk(feature_dict):
    """
    Converts the feature dictionary into the feature structure expected by the model,
    runs prediction, and returns (risk_score, recommended_action).
    """
    # Convert to model input dataframe
    df_model = pd.DataFrame([{
        # Demographics
        "Age": feature_dict["Age"],
        "Sex": feature_dict["Sex"],
        "Ethnicity": feature_dict["Ethnicity"],
        "Religion": feature_dict["Religion"],
        "Marital status": feature_dict["Marital"],
        "Educational level": feature_dict["Education"],
        "Occupation": feature_dict["Occupation"],

        # Clinical
        "WhatisyourCD4count_": feature_dict["CD4"],
        "HowlonghaveyoubeenonART_": feature_dict["ARTDuration"],
        "StageofHIVclassification_": feature_dict["HIVStage"],
        "Haveyoueverbeenscreenedorq_": feature_dict["TBscreen"],
        "Whatwasyourresult_": feature_dict["TBresult"],
        "Coughfortwo2ormoreweeks_": feature_dict["Cough"],
        "Nightsweats_": feature_dict["NightSweat"],
        "Chillsandfever_": feature_dict["Fever"],
        "Chestpain_": feature_dict["ChestPain"],
        "Weightloss_": feature_dict["WeightLoss"],

        # PHQ‑9
        "Littleinterestorpleasureind_1": feature_dict["PHQ1"],
        "Feelingdowndepressedorhope_1": feature_dict["PHQ2"],
        "Troublefallingorstayingaslee_1": feature_dict["PHQ3"],
        "Feelingtiredorhavinglittlee_1": feature_dict["PHQ4"],
        "Poorappetiteorovereating_1": feature_dict["PHQ5"],
        "Feelingbadaboutyourselfor_1": feature_dict["PHQ6"],
        "Troubleconcentratingonthings_1": feature_dict["PHQ7"],
        "Movingorspeakingsoslowlytha_1": feature_dict["PHQ8"],
        "Thoughtsthatyouwouldbebette_1": feature_dict["PHQ9"],

        # Psychosocial
        "Doyoutendtoworryorfeelanx_1": feature_dict["Worry"],
        "Howoftendoyoufeellowinene_1": feature_dict["Loneliness"],
        "Doyouengageinsubstanceabuse_": feature_dict["Substance"],
        "Doyouusetobacco_": feature_dict["Tobacco"],
        "Doyouthinkthereisastigma_1": feature_dict["Stigma"],
        "Doculturalbeliefsinfluenceyo_1": feature_dict["Cultural"],
    }])

    # Run model probability prediction
    risk_score = float(model.predict_proba(df_model)[0][1])

    # Use decision engine to generate action
    action = decision_engine(risk_score)

    return risk_score, action
