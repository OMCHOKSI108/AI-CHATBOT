import streamlit as st
import pandas as pd
import random

# Load your Excel dataset (ensure 'DATASET01.xlsx' is in the same directory)
df = pd.read_excel('DATASET01.xlsx')

st.set_page_config(page_title="Technical Education Chatbot", page_icon=":robot_face:", layout="centered")
st.title("🤖 Technical Education Chatbot")

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Function to find the closest matching response
def get_response(user_input):
    user_input = user_input.lower()
    for index, row in df.iterrows():
        patterns = row['patterns'].split(',')  # Assuming patterns are comma-separated
        for pattern in patterns:
            if all(word in user_input for word in pattern.lower().split()):
                return random.choice(row['responses'].split(','))
    return "Sorry, I don't have the answer to that question."

# Function to display chat history
def display_chat():
    for message in st.session_state['messages']:
        if message['role'] == 'user':
            st.markdown(f"**You:** {message['content']}")
        else:
            st.markdown(f"**Bot:** {message['content']}")
    st.write("---")

# User input
user_input = st.text_input("Ask me anything about technical education:")

if user_input:
    st.session_state['messages'].append({"role": "user", "content": user_input})
    bot_response = get_response(user_input)
    st.session_state['messages'].append({"role": "assistant", "content": bot_response})

st.write("### Chat History:")
display_chat()

st.markdown("<div style='text-align: center; color: grey;'>Powered by a Rule-Based System & Streamlit</div>", unsafe_allow_html=True)
