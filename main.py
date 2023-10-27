from logic import *  # modified the creat_table function to better optimize memory
from medical_diagnosis import *
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Medical Diagnosis Using Knowledge", layout="wide")

st.title("Medical Diagnosis Using Knowledge")
st.write("A diagnosis is made using knowledge base and the use of logical operators")
st.write("The logical statement for the knowledge base is: Implication(Or(And(all symptoms in set1), And(all symptoms in set2))), disease)")
st.write("Created by Yash Sindhu")
st.write("Developed as a college project, reach out for any questions or feedback at yashsindhu4903@gmail.com")

@st.cache   # saves time and memory by only creating the knowledge base once
def get_knowledge():
    return create_knowledgebase()

knowledge_base = create_knowledgebase()

symptom_list = pd.read_csv('Symptom-severity.csv').iloc[:,0].tolist()
st.subheader("Enter Symptoms")
selected_symptoms = st.multiselect(" ", symptom_list)

if st.button("Diagnose"):
    symptoms = And(*[Symbol(f"{s}") for s in selected_symptoms])

    diagnosis = diagnose(knowledge_base, symptoms)
    # Display the diagnosis
    st.subheader("Diagnosis:")
    if len(diagnosis) == 0:
        st.write("No disease found")
    else:
        for disease in diagnosis:
            st.write(disease)