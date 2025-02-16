import os
import pickle
import streamlit as st
import numpy as np
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# loading the saved models
diabetes_model = pickle.load(open('saved_models/diabetes_model.pkl', 'rb'))
heart_disease_model = pickle.load(open('saved_models/heart_disease_model.pkl', 'rb'))

# Sidebar for navigation
st.sidebar.title("Disease Prediction System")
selected = st.sidebar.radio('Select a disease to predict:',
                            ['Heart Disease Prediction', 'Diabetes Prediction'])

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    # Page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex (0/1)')

    with col3:
        cp = st.text_input('Chest Pain types (cp)(0-3)')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure (trestbps)(94-200)')

    with col2:
        chol = st.text_input('Serum Cholestoral (chol) > 120 in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar (fbs)(0/1)')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results (restecg)(0/1)')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved (thalach)')

    with col3:
        exang = st.text_input('Exercise Induced Angina (exang)(0/1)')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise (oldpeak)(0-6.2)')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment (slope)(0/1/2)')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy (ca)(0-4)')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # Code for Prediction
    heart_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        # Check if any input field is empty
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        if '' in user_input:
            heart_diagnosis = 'Kindly fill all the input fields'
        else:
            if heart_disease_model is not None:
                try:
                    user_input = [float(x) for x in user_input]
                    heart_prediction = heart_disease_model.predict([user_input])

                    if heart_prediction[0] == 1:
                        heart_diagnosis = 'The person is having heart disease'
                    else:
                        heart_diagnosis = 'The person does not have any heart disease'
                except Exception as e:
                    heart_diagnosis = f"Error in prediction: {e}"
            else:
                heart_diagnosis = "Heart disease model not available."

        st.success(heart_diagnosis)


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    # Page title
    st.title('Diabetes Prediction using ML')

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')

    # Code for Prediction
    diab_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Diabetes Test Result'):
        # Check if any input field is empty
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        if '' in user_input:
            diab_diagnosis = 'Kindly fill all the input fields'
        else:
            if diabetes_model is not None:
                try:
                    user_input = [float(x) for x in user_input]
                    diab_prediction = diabetes_model.predict([user_input])

                    if diab_prediction[0] == 1:
                        diab_diagnosis = 'The person is diabetic'
                    else:
                        diab_diagnosis = 'The person is not diabetic'
                except Exception as e:
                    diab_diagnosis = f"Error in prediction: {e}"
            else:
                diab_diagnosis = "Diabetes model not available."

        st.success(diab_diagnosis)
