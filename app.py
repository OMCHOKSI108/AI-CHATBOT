import streamlit as st
import pandas as pd
import random

# Load the dataset from the Excel file
df = pd.read_excel('DATASET01.xlsx')

# Streamlit application title
st.title("Technical Education Chatbot")

# Initialize session state to hold the conversation history
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Function to find the closest matching response
def get_response(user_input):
    user_input_words = user_input.lower().split()
    matching_responses = []

    for index, row in df.iterrows():
        patterns = row['patterns'].split(',')  # Assuming patterns are comma-separated
        tag = row['tag']

        for pattern in patterns:
            if all(word in pattern.lower() for word in user_input_words):
                matching_responses.extend(row['responses'].split(','))  # Add matching responses to the list

    if matching_responses:
        return random.choice(matching_responses)

    return "Sorry, I don't have the answer to that question."

# Step 3: Create a text input for user queries
user_input = st.text_input("Ask me anything about technical education:")

# Step 4: Generate a response when the user submits a question
if user_input:
    response = get_response(user_input)
    # Store the user input and response in the session state
    st.session_state.conversation.append({"user": user_input, "bot": response})

# Display the conversation history
for chat in st.session_state.conversation:
    st.write(f"**You:** {chat['user']}")
    st.write(f"**Bot:** {chat['bot']}")
