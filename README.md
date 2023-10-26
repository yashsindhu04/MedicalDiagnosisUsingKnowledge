## Medical Diagnosis Using Knowledge

This repository contains Python code for a medical diagnosis system that utilizes a knowledge base and logical operators to diagnose diseases based on a set of symptoms. The system consists of two main files: `medical_diagnosis.py` and `main.py`. Below is an overview of each file and its functionality.

### `medical_diagnosis.py`

`medical_diagnosis.py` is a Python script that defines functions for creating a knowledge base of diseases and symptoms and for diagnosing diseases based on a set of symptoms provided as input.

- **`create_knowledgebase()`:** This function reads a dataset from the CSV file of the dataset and creates a knowledge base for diseases and symptoms. It iterates through the dataset, organizing symptoms into sets for each disease using logical operators. It builds a knowledge base for each disease and stores them in a dictionary.

- **`diagnose(knowledge_bases, your_symptoms)`:** This function performs model checking logic to check if a set of symptoms implies a particular disease. It checks each disease's knowledge base against the given symptoms and returns a list of possible diseases that match the symptoms.

### `main.py`

`main.py` is the main application script that uses the knowledge base created in `medical_diagnosis.py` to diagnose diseases based on user-provided symptoms. It also utilizes the `streamlit` library for creating a web-based user interface. The script performs the following functions:

- **Knowledge Base Caching:** It uses Streamlit's caching feature to load and create the knowledge base once, saving time and memory when diagnosing multiple symptoms.

- **User Interface:** The script creates a Streamlit web interface for users to enter their symptoms and initiate the diagnosis.

    - It creates a list of symptoms from a dataset and allows users to select their symptoms from a multiselect widget.
    
    - When the "Diagnose" button is pressed, the selected symptoms are converted into a logical statement and passed to the `diagnose()` function from `medical_diagnosis.py`.

- **Display Diagnosis:** The script displays the diagnosis results on the web page, showing the possible diseases that match the provided symptoms. If no disease is found, it displays a "No disease found" message.

### Usage

To use this medical diagnosis system, follow these steps:

1. Ensure you have the required libraries installed, from `requirements.txt`.

4. Run `streamlit run main.py` using a Python interpreter.

5. Use the web interface to select symptoms and click the "Diagnose" button to receive a list of possible diseases.

This system is a basic example of medical diagnosis using knowledge-based reasoning and can be further expanded and refined for more comprehensive applications.

For any questions or feedback, please contact the developer, Yash Sindhu, at yashsindhu4903@gmail.com.
