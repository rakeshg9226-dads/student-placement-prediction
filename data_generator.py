import pandas as pd
import numpy as np

def create_demo_dataset(n_samples=600, random_state=42):
    """Create synthetic educational data; not real student records."""
    rng = np.random.default_rng(random_state)
    cgpa = rng.uniform(4.0, 10.0, n_samples).round(2)
    aptitude = rng.integers(25, 101, n_samples)
    communication = rng.integers(25, 101, n_samples)
    internships = rng.integers(0, 4, n_samples)
    projects = rng.integers(0, 7, n_samples)
    coding_skill = rng.choice(["Beginner", "Intermediate", "Advanced"], n_samples, p=[0.3, 0.45, 0.25])

    coding_score = pd.Series(coding_skill).map({"Beginner": 0, "Intermediate": 1, "Advanced": 2}).to_numpy()
    score = (
        (cgpa - 5.0) * 0.55
        + (aptitude - 50) / 28
        + (communication - 50) / 35
        + internships * 0.65
        + projects * 0.22
        + coding_score * 0.65
        + rng.normal(0, 1.15, n_samples)
    )
    placed = (score > 3.15).astype(int)

    return pd.DataFrame({
        "cgpa": cgpa,
        "aptitude_score": aptitude,
        "communication_score": communication,
        "internships": internships,
        "projects": projects,
        "coding_skill": coding_skill,
        "placed": placed
    })

if __name__ == "__main__":
    df = create_demo_dataset()
    df.to_csv("placement_data.csv", index=False)
    print("Created placement_data.csv")
