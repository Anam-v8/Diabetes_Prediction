import streamlit as st
import pickle
import pandas as pd

# Page Configuration

st.set_page_config(
page_title="Diabetes Prediction System",
page_icon="🩺",
layout="wide"
)

# Custom CSS

st.markdown("""

<style>
            
            /* Make input labels bigger */
div[data-testid="stNumberInput"] label p {
font-size: 25px !important;
font-weight: bold !important;
color: white !important;
}


/* Main Background */
.stApp {
    background-color: #F3E3D0;
}

/* Title */
.main-title {
    text-align: center;
    color: #81A6C6;
    font-size: 48px;
    font-weight: bold;
    margin-bottom: 10px;
}

/* Subtitle */
.sub-title {
    text-align: center;
    color: #555555;
    font-size: 18px;
    margin-bottom: 30px;
}

/* Input Fields */
.stNumberInput {
    background-color: #AACDDC;
    padding: 8px;
    border-radius: 12px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #D2C4B4;
}

/* Center Button */
div.stButton {
    display: flex;
    justify-content: center;
    margin-top: 20px;
}

/* Predict Button */
.stButton > button {
    background-color: #81A6C6;
    color: white;
    width: 250px;
    height: 70px;
    border-radius: 15px;
    border: none;
    font-size: 50px;
    font-weight: bold;
}
            .stButton > button p {
font-size: 25px !important;
font-weight: bold !important;
}


.stButton > button:hover {
    background-color: #AACDDC;
    color: black;
}

/* Result Box */
.result-box {
    text-align: center;
    padding: 15px;
    border-radius: 15px;
    font-size: 50px;
    font-weight: bold;
}

</style>

""", unsafe_allow_html=True)

# Load Model

model = pickle.load(
open('D:/Diabetes_Prediction/models/diabetes_model.pkl', 'rb')
)

# Title

st.markdown(
'<div class="main-title">🩺 Diabetes Prediction System</div>',
unsafe_allow_html=True
)

st.markdown(
'<div class="sub-title">Predict diabetes risk using Machine Learning</div>',
unsafe_allow_html=True
)

# Sidebar

st.sidebar.title("About")
st.sidebar.info(
"""
Diabetes Prediction System

```
Model: Logistic Regression
Accuracy: ~75%

Enter patient information and click Predict.
"""


)

# Input Layout

col1, col2 = st.columns(2)

with col1:
    preg = st.number_input("Pregnancies", min_value=0.0)
    glucose = st.number_input("Glucose", min_value=0.0)
    bp = st.number_input("Blood Pressure", min_value=0.0)
    skin = st.number_input("Skin Thickness", min_value=0.0)

with col2:
    insulin = st.number_input("Insulin", min_value=0.0)
    bmi = st.number_input("BMI", min_value=0.0)
    dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0)
    age = st.number_input("Age", min_value=0.0)

# Predict Button

if st.button("🔍 Predict"):

        data = pd.DataFrame({
            'Pregnancies': [preg],
            'Glucose': [glucose],
            'BloodPressure': [bp],
            'SkinThickness': [skin],
            'Insulin': [insulin],
            'BMI': [bmi],
            'DiabetesPedigreeFunction': [dpf],
            'Age': [age]
        })

        result = model.predict(data)

        st.markdown("<br>", unsafe_allow_html=True)

        if result[0] == 1:
            st.error("⚠️ High Risk of Diabetes")
        else:
            st.success("✅ Low Risk of Diabetes")

