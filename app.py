import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load model and column names
model = joblib.load("breast_cancer_model.pkl")
model_columns = joblib.load("breast_cancer_model_columns.pkl")

st.set_page_config(page_title="🩺 Breast Cancer Predictor", layout="wide")
st.title("🧬 Breast Cancer Prediction App")
st.write("Provide input values below to predict if the tumor is *Malignant* or *Benign*.")

mean_radius = st.slider("Mean Radius", 6.0, 30.0, 14.0)
mean_texture = st.slider("Mean Texture", 9.0, 40.0, 19.0)
mean_perimeter = st.slider("Mean Perimeter", 40.0, 190.0, 90.0)
mean_area = st.slider("Mean Area", 140.0, 2500.0, 600.0)
mean_smoothness = st.slider("Mean Smoothness", 0.05, 0.2, 0.1)

input_data = pd.DataFrame(np.zeros((1, len(model_columns))), columns=model_columns)
input_data["mean radius"] = mean_radius
input_data["mean texture"] = mean_texture
input_data["mean perimeter"] = mean_perimeter
input_data["mean area"] = mean_area
input_data["mean smoothness"] = mean_smoothness

st.subheader("Input Data Preview")
st.dataframe(input_data)

if st.button("Predict"):
    prediction = model.predict(input_data)
    proba = model.predict_proba(input_data)

    classes = ['Malignant', 'Benign']
    predicted_class = classes[prediction[0]]

    st.success(f"🔍 Predicted Diagnosis: *{predicted_class}*")
    st.subheader("Prediction Probabilities")
    for i, label in enumerate(classes):
        st.write(f"{label}: *{proba[0][i]:.2f}*")
