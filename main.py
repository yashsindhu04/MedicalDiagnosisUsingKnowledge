from logic import *
from medical_diagnosis import *
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Medical Diagnosis Using Knowledge", layout="wide")
# Define the custom theme colors
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: #e6e3e3;
    }}
    .st-eb {{
        background-color: #ffffff;
    }}
    .st-ej {{
        background-color: #9639d0;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)
# base="light"
# primaryColor="#9639d0"
# backgroundColor="#e6e3e3"
# secondaryBackgroundColor="#ffffff"

st.title("Medical Diagnosis Using Knowledge")
st.write("A diagnosis is made using knowledge base and the use of logical operators")
st.write("Created by Yash Sindhu")
st.write("Developed as a college project, reach out for any questions or feedback at yashsindhu4903@gmail.com")

symptom_list = pd.read_csv('Symptom-severity.csv').iloc[:,0].tolist()
st.subheader("Enter Symptoms")
selected_symptoms = st.multiselect("", symptom_list)

if st.button("Diagnose"):
    symptoms = And(*[Symbol(f"{s}") for s in selected_symptoms])

    diagnosis = diagnose(symptoms)
    # Display the diagnosis
    st.subheader("Diagnosis:")
    if len(diagnosis) == 0:
        st.write("No disease found")
    else:
        for disease in diagnosis:
            st.write(disease)