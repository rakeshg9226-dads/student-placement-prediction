from pathlib import Path
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from data_generator import create_demo_dataset

ROOT = Path(__file__).resolve().parent
MODEL_DIR = ROOT / "models"
MODEL_PATH = MODEL_DIR / "placement_model.joblib"

FEATURES = ["cgpa", "aptitude_score", "communication_score", "internships", "projects", "coding_skill"]

def train_and_save_model():
    df = create_demo_dataset(n_samples=1000, random_state=42)
    X = df[FEATURES]
    y = df["placed"]

    categorical = ["coding_skill"]
    numeric = [c for c in FEATURES if c not in categorical]
    preprocessor = ColumnTransformer(
        transformers=[
            ("coding", OrdinalEncoder(categories=[["Beginner", "Intermediate", "Advanced"]]), categorical),
            ("numeric", "passthrough", numeric),
        ],
        remainder="drop"
    )
    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("classifier", RandomForestClassifier(n_estimators=180, random_state=42, class_weight="balanced"))
    ])
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    pipeline.fit(X_train, y_train)
    predictions = pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, MODEL_PATH)
    return {"accuracy": accuracy, "report": classification_report(y_test, predictions, zero_division=0)}

if __name__ == "__main__":
    metrics = train_and_save_model()
    print(f"Demo test accuracy: {metrics['accuracy']:.2%}")
    print(metrics["report"])
    print(f"Saved model to: {MODEL_PATH}")
