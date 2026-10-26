# Student Placement Prediction (Machine Learning + Streamlit)

A beginner-friendly project that estimates a student's placement likelihood using a Random Forest classifier and a Streamlit web app.

> **Important:** The training data is synthetic and created only for demonstration. The probability is not a guarantee and must not be used as the sole basis for real placement or hiring decisions.

## Features
- Attractive Streamlit interface with sidebar navigation
- Inputs for CGPA, aptitude, communication, internships, projects, and coding skill
- Placement probability estimate
- Personalized improvement suggestions
- Separate modules for data generation, model training, prediction, and UI

## Project Structure
```text
Student_Placement_Prediction/
├── app.py
├── data_generator.py
├── train_model.py
├── predictor.py
├── requirements.txt
├── README.md
├── PROJECT_SYNOPSIS.md
├── .gitignore
└── models/
    └── .gitkeep
```
The trained model is generated locally the first time you make a prediction. You do not need to upload the generated model file to GitHub.

## Requirements
- Python 3.10 or newer recommended
- Internet connection for installing packages
- VS Code or another Python editor

## Run Locally (Windows)
1. Download and extract the project ZIP.
2. Open the project folder in VS Code.
3. Open Terminal in VS Code.
4. Create a virtual environment (recommended):
   ```bash
   python -m venv .venv
   .venv\\Scripts\\activate
   ```
5. Install libraries:
   ```bash
   pip install -r requirements.txt
   ```
6. Start the app:
   ```bash
   streamlit run app.py
   ```
7. A browser tab should open with the app. If not, use the local URL printed in the terminal.

## Retrain the Model
```bash
python train_model.py
```
This creates `models/placement_model.joblib`. The model is generated from synthetic data.

## Upload to GitHub
1. Create a new repository on GitHub, e.g. `student-placement-prediction`.
2. Keep it **Public** if you want to deploy on Streamlit Community Cloud.
3. Upload `app.py`, `data_generator.py`, `train_model.py`, `predictor.py`, `requirements.txt`, `README.md`, `PROJECT_SYNOPSIS.md`, `.gitignore`, and `models/.gitkeep`.
4. Do not upload `.venv/`, `__pycache__/`, `.env`, private credentials, or temporary files.
5. In Streamlit Community Cloud, create a new app, choose the repository, branch, and `app.py`, then deploy.

## Troubleshooting
- **`ModuleNotFoundError`:** activate the correct environment and run `pip install -r requirements.txt`.
- **App cannot find model:** run `python train_model.py`, or use the Predict page; it can create the model automatically.
- **Python version:** use a currently supported Python version compatible with the installed scikit-learn version.

## Disclaimer
This is an educational prototype. Use representative, consented, appropriately protected data and validate model quality and fairness before any real-world use.
