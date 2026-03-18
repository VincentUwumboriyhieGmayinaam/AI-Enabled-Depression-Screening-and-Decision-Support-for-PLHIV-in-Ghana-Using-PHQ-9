import joblib

def load_model(path="models/best_model.pkl"):
    """Load the trained ML model."""
    return joblib.load(path)
