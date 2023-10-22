from logic import *   # modified the Or() class to include add() function
import pandas as pd

def create_knowledgebase():
    df = pd.read_csv('dataset.csv')
    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)  # removing all leading spaces

    # Dictionary to store knowledge bases for every disease
    knowledge_bases = {}
    current =  None

    for i in range(len(df)):
        disease = df.iloc[i,0]
        if disease != current:  # Creating a new knowledge base for every disease
            disease_knowledge = Or()
            current = disease
            
        # iterates through every symptom column while ignoring the nan values
        symptoms = [df[col][i] for col in df.columns[1:] if not pd.isna(df[col][i])]

        # Creates a list of symbols for each symptoms to create a set of symptoms
        symptom_knowledge = And(*[Symbol(f'{symptom}') for symptom in symptoms])  
        disease_knowledge.add(symptom_knowledge)  # Each set is added to the Or for each disease
        if disease not in knowledge_bases:  # Adds the knowledge of the disease to the main knowledge base
            knowledge_bases[disease] = Implication(disease_knowledge, Symbol(disease))
    
    return knowledge_bases

def diagnose(your_symptoms):
    '''
    Model checking logic: Check if the symptoms i have imply that i have the disease
    '''
    knowledge_bases = create_knowledgebase()
    possible_diseases = []
    for disease in knowledge_bases:
        if model_check(knowledge_bases[disease], Implication(your_symptoms, Symbol(f'{disease}'))):
            # print(f'{disease}: Yes')
            possible_diseases.append(disease)
    
    return possible_diseases
            
# diagnose(And(Symbol('itching'),  Symbol('skin_rash'),  Symbol('dischromic_patches')))
            
# print(knowledge_bases['Fungal infection'])
# your_symptoms = And(Symbol('itching'),  Symbol('skin_rash'),  Symbol('dischromic_patches'))
# diagnose(your_symptoms)