import streamlit as st
import pandas as pd
import plotly.express as px
from predictor import predict_placement
from train_model import train_and_save_model
from pathlib import Path
from style import load_css, show_header

st.set_page_config(page_title="Student Placement Predictor", page_icon="🎓", layout="wide")

load_css()
show_header()

with st.sidebar:
    st.header("📌 Navigation")
    page = st.radio("Choose a page", ["Predict Placement", "Project Overview", "Model Information"])
    st.divider()
    st.caption("Educational demo only. Predictions are estimates, not guarantees.")

if page == "Predict Placement":
    left, right = st.columns([1.15, 0.85], gap="large")
    with left:
        st.subheader("🧑‍🎓 Student Details")
        with st.form("student_form"):
            c1, c2 = st.columns(2)
            with c1:
                cgpa = st.slider("CGPA (0–10)", 0.0, 10.0, 7.0, 0.1)
                aptitude = st.slider("Aptitude score (0–100)", 0, 100, 70)
                communication = st.slider("Communication score (0–100)", 0, 100, 70)
            with c2:
                internships = st.number_input("Internships completed", 0, 10, 1)
                projects = st.number_input("Projects completed", 0, 20, 2)
                coding = st.selectbox("Coding skill", ["Beginner", "Intermediate", "Advanced"], index=1)
            submitted = st.form_submit_button("✨ Predict Placement", use_container_width=True)

    with right:
        st.subheader("📊 Quick Guide")
        st.info("Enter a student's academic performance, experience, projects, and skill levels, then select **Predict Placement**.")
        st.markdown("""
        **Inputs used**
        - CGPA
        - Aptitude and communication scores
        - Internship and project counts
        - Coding skill level
        """)
        st.warning("This project trains on a small synthetic sample dataset. Use real, representative data before making real-world decisions.")

    if submitted:
        input_data = {
            "cgpa": cgpa, "aptitude_score": aptitude,
            "communication_score": communication, "internships": internships,
            "projects": projects, "coding_skill": coding
        }
        try:
            result = predict_placement(input_data)
            st.divider()
            st.subheader("Prediction Result")
            col1, col2 = st.columns([1, 1])
            with col1:
                if result["placed"]:
                    st.success("### Likely to be placed")
                else:
                    st.error("### Placement may be challenging")
                st.metric("Estimated placement probability", f'{result["probability"]:.1%}')
                st.progress(int(result["probability"] * 100))
            with col2:
                st.markdown("**Suggested next steps**")
                suggestions = []
                if cgpa < 7:
                    suggestions.append("Strengthen core subjects and improve academic performance where possible.")
                if aptitude < 70:
                    suggestions.append("Practice quantitative aptitude and logical reasoning.")
                if communication < 70:
                    suggestions.append("Practice interview introductions and mock interviews.")
                if internships < 1:
                    suggestions.append("Look for internships, volunteering, or practical experience.")
                if projects < 2:
                    suggestions.append("Build and document 2–3 practical projects.")
                if coding == "Beginner":
                    suggestions.append("Practice coding fundamentals and problem-solving.")
                if not suggestions:
                    suggestions.append("Prepare a polished resume and practice role-specific interviews.")
                for item in suggestions:
                    st.write("• " + item)
        except Exception as exc:
            st.error(f"Could not create prediction: {exc}")
            st.info("If this is the first run, click the button again after the model is created.")

elif page == "Project Overview":
    st.subheader("About the Project")
    st.write("This beginner-friendly project uses a Random Forest classifier to estimate whether a student may be placed based on selected academic and employability indicators.")
    a, b, c = st.columns(3)
    a.metric("ML Algorithm", "Random Forest")
    b.metric("App Framework", "Streamlit")
    c.metric("Input Features", "6")
    st.markdown("### Project Workflow")
    st.markdown("1. Create a small demonstration dataset.\\n2. Train a classification model.\\n3. Save the model with Joblib.\\n4. Collect student details through Streamlit.\\n5. Display estimated probability and practical suggestions.")
    st.markdown("### Limitations")
    st.write("The bundled data is synthetic and intended for learning. It does not represent any real college or hiring outcome. Model output can reflect bias in data and must not be used as the sole basis for decisions.")

else:
    st.subheader("Model Information")
    st.markdown("""
    - **Problem type:** Binary classification
    - **Target:** `placed` (0 = not placed, 1 = placed)
    - **Algorithm:** Random Forest Classifier
    - **Preprocessing:** Ordinal encoding for coding skill
    - **Model file:** `models/placement_model.joblib`
    - **Training data:** Generated synthetic example records
    """)
    if st.button("🔄 Retrain demonstration model"):
        with st.spinner("Training model..."):
            metrics = train_and_save_model()
        st.success(f"Model retrained. Demo test accuracy: {metrics['accuracy']:.1%}")
