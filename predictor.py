from pathlib import Path
import joblib
import pandas as pd
from train_model import MODEL_PATH, FEATURES, train_and_save_model

def load_model():
    if not Path(MODEL_PATH).exists():
        train_and_save_model()
    return joblib.load(MODEL_PATH)

def predict_placement(student):
    model = load_model()
    row = pd.DataFrame([{
        "cgpa": float(student["cgpa"]),
        "aptitude_score": int(student["aptitude_score"]),
        "communication_score": int(student["communication_score"]),
        "internships": int(student["internships"]),
        "projects": int(student["projects"]),
        "coding_skill": student["coding_skill"]
    }], columns=FEATURES)
    probability = float(model.predict_proba(row)[0][1])
    return {"placed": probability >= 0.5, "probability": probability}
