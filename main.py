from logic import *
from medical_diagnosis import *
import streamlit as st

symptom_categories = {
    'Skin-related Symptoms': [
        'itching', 'skin_rash', 'nodal_skin_eruptions',
        'red_sore_around_nose', 'yellow_crust_ooze',
        'silver_like_dusting', 'skin_peeling', 'blackheads'
    ],
    'Respiratory Symptoms': [
        'continuous_sneezing', 'cough', 'chest_pain',
        'phlegm', 'throat_irritation', 'runny_nose', 'congestion',
        'rusty_sputum'
    ],
    'Gastrointestinal Symptoms': [
        'stomach_pain', 'acidity', 'ulcers_on_tongue',
        'vomiting', 'indigestion', 'nausea', 'loss_of_appetite',
        'abdominal_pain', 'diarrhoea', 'constipation', 'painful_walking'
    ],
    'General Health Symptoms': [
        'fatigue', 'weight_gain', 'weight_loss',
        'restlessness', 'lethargy', 'malaise', 'depression',
        'irritability', 'altered_sensorium'
    ],
    'Fever and Infection-related Symptoms': [
        'high_fever', 'sweating', 'dehydration', 'yellowish_skin',
        'dark_urine', 'pain_behind_the_eyes', 'mild_fever',
        'acute_liver_failure', 'flu-like symptoms'
    ],
    'Musculoskeletal Symptoms': [
        'joint_pain', 'muscle_wasting', 'weakness_in_limbs',
        'muscle_pain', 'stiff_neck', 'swelling_joints',
        'movement_stiffness', 'loss_of_balance', 'unsteadiness',
        'weakness_of_one_body_side', 'knee_pain', 'hip_joint_pain',
        'cramps', 'neck_pain'
    ],
    'Urinary and Kidney Symptoms': [
        'burning_micturition', 'spotting_urination',
        'irregular_sugar_level', 'yellow_urine', 'yellowing_of_eyes',
        'bladder_discomfort', 'foul_smell_of_urine', 'continuous_feel_of_urine'
    ],
    'Eye-related Symptoms': [
        'redness_of_eyes', 'blurry_vision', 'visual_disturbances',
        'red_spots_over_body', 'watering_from_eyes'
    ],
    'Genitourinary Health': [
        'extra_marital_contacts', 'excessive_hunger',
        'painful_bowel_movements', 'pain_in_anal_region',
        'bloody_stool', 'irritation_in_anus'
    ],
    'Miscellaneous': [
        'sunken_eyes', 'swelling_of_stomach',
        'swelled_lymph_nodes', 'dizziness', 'bruising', 'obesity',
        'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes',
        'enlarged_thyroid', 'brittle_nails', 'swollen_extremities',
        'internal_itching', 'toxic_look_(typhos)', 'belly_pain',
        'abnormal_menstruation', 'dischromic_patches',
        'increased_appetite', 'polyuria', 'family_history',
        'receiving_blood_transfusion', 'receiving_unsterile_injections',
        'coma', 'stomach_bleeding', 'distention_of_abdomen',
        'history_of_alcohol_consumption', 'blood_in_sputum',
        'prominent_veins_on_calf', 'palpitations', 'pus_filled_pimples',
        'small_dents_in_nails', 'inflammatory_nails', 'blister'
    ]
}

symptom_list = pd.read_csv('Symptom-severity.csv').iloc[:,0].tolist()
selected_symptoms = st.multiselect("Select Symptoms",symptom_list)
# # Create a multiselect dropdown with checkboxes for symptom categories
# selected_symptoms = st.multiselect("Select Symptoms ", list(symptom_categories.keys()), key="categories")

# Display the selected symptoms
st.write("Selected Symptoms:", selected_symptoms)