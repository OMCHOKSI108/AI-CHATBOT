import streamlit as st
import pandas as pd
import random

# Step 1: Load the dataset from the Excel file
# Make sure that 'DATASET01.xlsx' is in the same directory as this script
df = pd.read_excel('DATASET01.xlsx')

# Streamlit application title
st.title("Technical Education Chatbot")

# Step 2: Function to find the closest matching response
from fuzzywuzzy import process

# Step 2: Function to find the closest matching response
def get_response(user_input):
    user_input = user_input.lower()
    all_patterns = df['patterns'].str.cat(sep=',').split(',')  # Get all patterns into a list

    # Use fuzzy matching to find the best match
    best_match, _ = process.extractOne(user_input, [p.strip().lower() for p in all_patterns])

    # Check if the best match is a significant match (you can adjust the threshold)
    if process.extractOne(user_input, [p.strip().lower() for p in all_patterns])[1] >= 75:  
        # Find the corresponding row in the dataframe
        row = df[df['patterns'].str.contains(best_match, case=False)]
        if not row.empty:
            return random.choice(row['responses'].values[0].split(','))  # Randomly choose a response
    
    return "Sorry, I don't have the answer to that question."


# Step 3: Create a text input for user queries
user_input = st.text_input("Ask me anything about technical education:")

# Step 4: Generate a response when the user submits a question
if user_input:
    response = get_response(user_input)
    st.write("**Bot:**", response)

# Optional: To display more context or information, you can add more elements below
