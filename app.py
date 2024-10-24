import streamlit as st
import pandas as pd
import random

# Step 1: Load the dataset from the Excel file
df = pd.read_excel('DATASET01.xlsx')

# Streamlit application title
st.title("Technical Education Chatbot")

# Step 2: Function to find the closest matching response
def get_response(user_input):
    for index, row in df.iterrows():
        patterns = row['patterns'].split(',')  # Assuming patterns are comma-separated
        for pattern in patterns:
            if pattern.strip().lower() in user_input.lower():
                return random.choice(row['responses'].split(','))  # Randomly choose a response
    return "Sorry, I don't have the answer to that question."

# Step 3: Create a text input for user queries
user_input = st.text_input("Ask me anything about technical education:")

# Step 4: Generate a response when the user submits a question
if user_input:
    response = get_response(user_input)
    st.write("**Bot:**", response)

# Optional: To display more context or information, you can add more elements below
