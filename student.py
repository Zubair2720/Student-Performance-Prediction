
import streamlit as st
import pandas as pd
import joblib

# Saved model load karna
bundle = joblib.load("student_model.pkl")

model = bundle["model"]
scale = bundle["scaler"]
feature_columns = bundle["feature_columns"]

st.title("Student Performance Prediction")
st.write("Student ki information enter karein.")

gender = st.selectbox("Gender", ["Male", "Female"])

study_hours = st.number_input(
    "Study Hours per Week",
    min_value=0,
    max_value=168,
    value=20
)

attendance = st.number_input(
    "Attendance Rate (%)",
    min_value=0.0,
    max_value=100.0,
    value=80.0
)

past_score = st.number_input(
    "Past Exam Scores",
    min_value=0,
    max_value=100,
    value=70
)

parent_education = st.selectbox(
    "Parental Education Level",
    ["Bachelors", "High School", "Masters", "PhD"]
)

internet = st.selectbox(
    "Internet Access at Home",
    ["Yes", "No"]
)

activities = st.selectbox(
    "Extracurricular Activities",
    ["Yes", "No"]
)

if st.button("Predict Result"):

    # Numeric encoding
    row = {
        "Gender": 0 if gender == "Male" else 1,
        "Study_Hours_per_Week": study_hours,
        "Attendance_Rate": attendance,
        "Past_Exam_Scores": past_score,
        "Internet_Access_at_Home": 1 if internet == "Yes" else 0,
        "Extracurricular_Activities": 1 if activities == "Yes" else 0
    }

    # One-hot encoding ke training columns ke mutabiq
    for col in feature_columns:
        if col.startswith("Parental_Education_Level_"):
            level = col.replace("Parental_Education_Level_", "")
            row[col] = int(parent_education == level)

    input_df = pd.DataFrame([row])

    # Missing ya extra columns ko handle karna
    input_df = input_df.reindex(
        columns=feature_columns,
        fill_value=0
    )

    # Training mein use kiye gaye numeric columns scale karna
    numeric_cols = [
        "Study_Hours_per_Week",
        "Attendance_Rate",
        "Past_Exam_Scores"
    ]

    input_df[numeric_cols] = scale.transform(input_df[numeric_cols])

    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.success("Predicted Result: PASS")
    else:
        st.error("Predicted Result: FAIL")
