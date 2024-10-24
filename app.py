import streamlit as st
import pandas as pd
import random

# Load the dataset from the Excel file
df = pd.read_excel('DATASET01.xlsx')

# Streamlit application title
st.title("Technical Education Chatbot")

# Step 2: Function to find the closest matching response
def get_response(user_input):
    # Split user input into words for substring matching
    user_input_words = user_input.lower().split()

    # List to hold matching responses
    matching_responses = []

    # Check each row in the dataset
    for index, row in df.iterrows():
        patterns = row['patterns'].split(',')  # Assuming patterns are comma-separated
        tag = row['tag']

        # Check if any word from the user input matches any pattern
        for pattern in patterns:
            # Convert the pattern to lowercase for case-insensitive matching
            if all(word in pattern.lower() for word in user_input_words):
                matching_responses.extend(row['responses'].split(','))  # Add matching responses to the list

    # If there are matching responses, return one at random
    if matching_responses:
        return random.choice(matching_responses)

    return "Sorry, I don't have the answer to that question."

# Step 3: Create a text input for user queries
user_input = st.text_input("Ask me anything about technical education:")

# Step 4: Generate a response when the user submits a question
if user_input:
    response = get_response(user_input)
    st.write("**Bot:**", response)
