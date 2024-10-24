import streamlit as st
import requests

# Title of the app
st.title("Technical Education Chatbot")

# Chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Function to handle sending messages
def send_message(user_input):
    # Display user message
    st.session_state.chat_history.append({"message": user_input, "is_user": True})
    
    # Send the user message to the chatbot backend
    # Replace 'http://localhost:5000/get' with your actual backend URL if deployed
     response = requests.get(f"https://ai-chatbot-technical-23aiml010.streamlit.app/{user_input}")

    bot_reply = response.text
    
    # Display bot reply
    st.session_state.chat_history.append({"message": bot_reply, "is_user": False})

# User input text box
user_input = st.text_input("Type your message...", "")
if st.button("Send"):
    if user_input:
        send_message(user_input)
        st.text_input("Type your message...", "", key='new_input')

# Display chat history
for chat in st.session_state.chat_history:
    if chat["is_user"]:
        st.markdown(f"You: {chat['message']}")
    else:
        st.markdown(f"Bot: {chat['message']}")
