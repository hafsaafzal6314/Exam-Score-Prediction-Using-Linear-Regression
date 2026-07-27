import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("exam_score_model.pkl")

# Page title
st.title("🎓 Exam Score Prediction")
st.write("Enter the student's details below.")

# ---------- User Inputs ----------

sex = st.selectbox("Sex", ["Female", "Male"])
age = st.number_input("Age", min_value=15, max_value=22, value=17)

address = st.selectbox("Address", ["Rural", "Urban"])

Medu = st.slider("Mother's Education (0-4)", 0, 4, 2)
Fedu = st.slider("Father's Education (0-4)", 0, 4, 2)

traveltime = st.slider("Travel Time (1-4)", 1, 4, 2)
studytime = st.slider("Study Time (1-4)", 1, 4, 2)

failures = st.slider("Previous Failures", 0, 4, 0)

schoolsup = st.selectbox("School Support", ["No", "Yes"])
famsup = st.selectbox("Family Support", ["No", "Yes"])
paid = st.selectbox("Extra Paid Classes", ["No", "Yes"])
activities = st.selectbox("Extra Activities", ["No", "Yes"])
higher = st.selectbox("Higher Education", ["No", "Yes"])
internet = st.selectbox("Internet Access", ["No", "Yes"])

famrel = st.slider("Family Relationship (1-5)", 1, 5, 3)
freetime = st.slider("Free Time (1-5)", 1, 5, 3)
goout = st.slider("Going Out (1-5)", 1, 5, 3)
health = st.slider("Health (1-5)", 1, 5, 3)

absences = st.number_input("Absences", min_value=0, max_value=100, value=0)

G1 = st.slider("First Term Grade (G1)", 0, 20, 10)
G2 = st.slider("Second Term Grade (G2)", 0, 20, 10)

# Convert categorical values to numbers

sex = 0 if sex == "Female" else 1
address = 0 if address == "Rural" else 1

schoolsup = 0 if schoolsup == "No" else 1
famsup = 0 if famsup == "No" else 1
paid = 0 if paid == "No" else 1
activities = 0 if activities == "No" else 1
higher = 0 if higher == "No" else 1
internet = 0 if internet == "No" else 1

if st.button("Predict Score"):

    input_data = pd.DataFrame([[
        sex,
        age,
        address,
        Medu,
        Fedu,
        traveltime,
        studytime,
        failures,
        schoolsup,
        famsup,
        paid,
        activities,
        higher,
        internet,
        famrel,
        freetime,
        goout,
        health,
        absences,
        G1,
        G2
    ]], columns=[
        'sex',
        'age',
        'address',
        'Medu',
        'Fedu',
        'traveltime',
        'studytime',
        'failures',
        'schoolsup',
        'famsup',
        'paid',
        'activities',
        'higher',
        'internet',
        'famrel',
        'freetime',
        'goout',
        'health',
        'absences',
        'G1',
        'G2'
    ])

    prediction = model.predict(input_data)

    st.success(f"🎯 Predicted Final Exam Score: {prediction[0]:.2f} / 20")