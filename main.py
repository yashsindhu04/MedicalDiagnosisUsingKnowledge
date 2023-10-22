from logic import *
from medical_diagnosis import *
import streamlit as st
import pandas

st.title("Medical Diagnosis Using Knowledge")
st.write("A diagnosis is made using knowledge base and the use of logical operators")
st.write("Created by Yash Sindhu")
st.write("Developed as a college project, reach out for any questions or feedback at yashsindhu4903@gmail.com")

symptom_list = pd.read_csv('Symptom-severity.csv').iloc[:,0].tolist()
selected_symptoms = st.multiselect("Enter symptoms", symptom_list)

symptoms = [Symbol(f"{s}") for s in selected_symptoms]

diagnosis = diagnose(symptoms)
# Display the selected symptoms
st.write("Diagnosis:", diagnosis)