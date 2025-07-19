# 🩺 Breast Cancer Prediction App
A Streamlit web app that predicts breast cancer from clinical input data using a trained Random Forest Classifier model.

# ☯️ Live Demo
https://csiassignmentweek7-key8rhbb4bfmtwkc6stnno.streamlit.app/

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

## 📁 Project Structure and Purpose of Each File
- **app.py**  
  → The main Streamlit app that runs in the browser and provides the user interface.
- **breast_cancer_model.pkl**  
  → The trained Random Forest model used to make predictions.
- **breast_cancer_model_columns.pkl**  
  → A list of feature names (column headers) used during model training, required to ensure consistent input format.
- **main.ipynb**  
  → The Jupyter Notebook used for data preprocessing, training the model, and saving the model files.
- **week7_full_code_file.ipynb**  
  → A consolidated notebook that includes all code cells from the development process for easier review and submission.
- **requirements.txt**  
  → Contains a list of Python packages required to run the app, used during deployment (e.g., Streamlit, scikit-learn, pandas, joblib, etc.).
- **README.md**  
  → This file. Describes the project, its structure, and how to run or deploy it.

## 👩‍💻 Author
Sumana Chowdhury
