# Project Synopsis: Student Placement Prediction Using Machine Learning and Streamlit

## 1. Project Title
**Student Placement Prediction Using Machine Learning and Streamlit**

## 2. Introduction
Student placement is an important milestone for students and educational institutions. This project demonstrates how selected academic performance and employability indicators can be used by a machine-learning classifier to estimate a student's placement likelihood. A simple Streamlit interface allows users to enter student details and view the estimated result.

## 3. Problem Statement
Students may need guidance to identify areas for improvement before applying for jobs. This project provides an educational demonstration of how data-driven predictions and basic improvement suggestions can be presented in an easy-to-use application.

## 4. Objectives
- Build a beginner-level binary classification project.
- Use student-related features such as CGPA, aptitude, communication, internships, projects, and coding skill.
- Train a Random Forest classifier.
- Save and load the trained pipeline using Joblib.
- Develop an interactive Streamlit application.
- Display estimated probability and practical suggestions.

## 5. Scope
The application is intended for learning machine learning, Python modular programming, and Streamlit development. It is not an official placement assessment system.

## 6. Tools and Technologies
- Programming language: Python
- Data processing: Pandas, NumPy
- Machine learning: Scikit-learn
- Model persistence: Joblib
- Web application: Streamlit
- Visualization/UI dependency: Plotly and Streamlit components
- Development environment: VS Code or another Python IDE

## 7. Dataset Description
The sample dataset is generated synthetically by `data_generator.py`. It contains:
- `cgpa`: CGPA on a 0–10 scale
- `aptitude_score`: aptitude score from 0–100
- `communication_score`: communication score from 0–100
- `internships`: number of internships
- `projects`: number of projects
- `coding_skill`: Beginner, Intermediate, or Advanced
- `placed`: target class (0 = not placed, 1 = placed)

The synthetic data is for demonstration only and does not represent actual student outcomes.

## 8. Methodology
1. Generate demonstration records.
2. Separate input features and target label.
3. Encode the categorical coding-skill feature.
4. Split the data into training and testing sets.
5. Train a Random Forest classifier.
6. Evaluate the model on the held-out synthetic test set.
7. Save the complete preprocessing/model pipeline with Joblib.
8. Collect user inputs in Streamlit and display the predicted class probability.

## 9. Main Modules
- `data_generator.py`: creates the synthetic dataset.
- `train_model.py`: prepares data, trains, evaluates, and saves the model.
- `predictor.py`: loads the model and produces a prediction.
- `app.py`: provides the Streamlit user interface.

## 10. Expected Output
The application displays whether the model estimates placement as more or less likely, the estimated probability, and suggestions based on the selected input values.

## 11. Limitations
- The dataset is synthetic, not real-world data.
- Model scores may not generalize to actual students or employers.
- Prediction can be affected by dataset design and bias.
- Probability must not be interpreted as a guarantee.
- The application must not be the sole basis for educational, employment, or placement decisions.

## 12. Future Enhancements
- Use a suitable, consented real dataset with documentation.
- Compare multiple classification algorithms.
- Add confusion matrix, precision, recall, F1-score, and ROC-AUC evaluation.
- Add data upload and model monitoring.
- Improve fairness, privacy, and model explainability.

## 13. Conclusion
This project demonstrates an end-to-end machine-learning workflow: synthetic data generation, preprocessing, model training, model persistence, prediction, and interactive deployment through Streamlit. It is suitable as a small learning project and starting point for further development.
