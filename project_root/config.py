# Decision logic for AI-generated risk score

def decision_engine(risk):
    if risk < 0.20:
        return "Very Low Risk: Reassure, routine follow-up."
    elif risk < 0.40:
        return "Mild Risk: Provide psychoeducation, follow-up in 4 weeks."
    elif risk < 0.60:
        return "Moderate Risk: Start mhGAP psychosocial support."
    elif risk < 0.80:
        return "High Risk: Initiate mhGAP interventions. Consider referral."
    else:
        return "VERY HIGH RISK: URGENT referral and immediate safety assessment."

# Which clinician accounts are administrators?
ADMINS = ["clinician2"]
