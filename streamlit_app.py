import streamlit as st
import pandas as pd
st.title('🤖 ML Visualization App')

st.info('This app builds a ML model')

with st.expander('data'):
  st.info('This app builds a ML model')
        name = st.text_input('Name')
        age = st.number_input('Age', min_value=1, max_value=100)
        symptoms = st.selectbox('Select your primary symptom', options=unique_symptoms)
        sleep_cycle = st.selectbox('What is your sleep cycle?', ['4 hours', '6 hours', '8 hours'])
        activity_level = st.selectbox('How is your life activity level?', ['active', 'very active', 'less active', 'lazy'])
        medical_history = st.selectbox('Do you have a medical history of any of the following diseases?',
                                               ["Diabetes", "Hypertension", "Asthma", "Heart Disease", "Cancer", "Arthritis", "Thyroid Disorder", "None of the above"])
        submitted = st.form_submit_button("Submit")
  

