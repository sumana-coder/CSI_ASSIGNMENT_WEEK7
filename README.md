# 🩺 Breast Cancer Prediction App
A Streamlit web app that predicts breast cancer from clinical input data using a trained Random Forest Classifier model.


## 🧠 Model Details
Dataset: Breast Cancer Dataset from scikit-learn
Algorithm: Random Forest Classifier
Accuracy: ~97% on test data

## 🚀 Features
Input sliders for all 30 breast cancer features
Live prediction of tumor type (Benign or Malignant)
Displays class probabilities for better insight
Clean and responsive UI built with Streamlit
Real-time feedback as input features are adjusted
Model trained on sklearn’s breast cancer dataset
Supports joblib-based model loading for fast inference

## Purpose of each file
app.py	--- The main Streamlit app that runs in the browser
breast_cancer_model.pkl	---  The trained Random Forest model
breast_cancer_model_columns.pkl	---  List of features (column names) used during model training
main.ipynb	---  Jupyter notebook used to train and save the model
week7_full_code_file --- list of all code cells in a single notebook
requirements.txt	--- List of Python packages required by the app
README.md -- Description of the project for GitHub or documentation purposes

## 👩‍💻 Author
Sumana Chowdhury
