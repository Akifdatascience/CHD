#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('model1.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Function to make predictions
def predict_chd(age, diabetes, sysBP, diaBP, glucose, sex_M, is_smoking_YES):
    input_data = pd.DataFrame({
        'age': [age],
        'diabetes': [diabetes],
        'sysBP': [sysBP],
        'diaBP': [diaBP],
        'glucose': [glucose],
        'sex_M': [sex_M],
        'is_smoking_YES': [is_smoking_YES]
    })
    prediction = model.predict(input_data)[0]
    return prediction

# Streamlit app
def main():
    st.title("Coronary Heart Disease (CHD) Prediction")

    # Input fields
    age = st.slider("Age", 20, 100, 50)
    diabetes = st.selectbox("Diabetes", ['No', 'Yes'])
    sysBP = st.number_input("Systolic Blood Pressure (mmHg)", min_value=70, max_value=250, value=120)
    diaBP = st.number_input("Diastolic Blood Pressure (mmHg)", min_value=40, max_value=150, value=80)
    glucose = st.number_input("Glucose (mg/dL)", min_value=50, max_value=400, value=100)
    sex_M = st.selectbox("Sex", ['Male', 'Female'])
    is_smoking_YES = st.selectbox("Smoking", ['No', 'Yes'])

    # Convert categorical values to numerical
    diabetes = 1 if diabetes == 'Yes' else 0
    sex_M = 1 if sex_M == 'Male' else 0
    is_smoking_YES = 1 if is_smoking_YES == 'Yes' else 0

    # Predict button
    if st.button("Predict"):
        prediction = predict_chd(age, diabetes, sysBP, diaBP, glucose, sex_M, is_smoking_YES)
        if prediction == 1:
            st.error("The person is predicted to be affected by CHD after ten years.")
        else:
            st.success("The person is predicted not to be affected by CHD after ten years.")

if __name__ == "__main__":
    main()


# In[ ]:




