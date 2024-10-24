import streamlit as st
import openai



# Set your OpenAI API key here
openai.api_key = "sk-RtIcDj3xQKXsHdjHs_-7l8w0Q5PIlrPFjwtTwfgFX2T3BlbkFJP72uTDRMEnMAnU8rMCP2iPmS3I_if6Sbx_Fp627TUA"

# Streamlit app title
st.set_page_config(page_title="Technical Education Chatbot", page_icon=":robot_face:", layout="centered")
st.title("🤖 Technical Education Chatbot")

# Chat History
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Function to get OpenAI GPT model response using the Chat Completion API
def get_openai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a helpful assistant knowledgeable in technical education."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

# Function to display chat history
def display_chat():
    for message in st.session_state['messages']:
        if message['role'] == 'user':
            st.markdown(f"**You:** {message['content']}")
        else:
            st.markdown(f"**Bot:** {message['content']}")
    st.write("---")

# User input for asking questions
user_input = st.text_input("Ask me anything about technical education:")

# Check if there is input
if user_input:
    # Append user input to the session state
    st.session_state['messages'].append({"role": "user", "content": user_input})
    
    # Get response from OpenAI GPT
    bot_response = get_openai_response(user_input)
    
    # Append bot response to the session state
    st.session_state['messages'].append({"role": "assistant", "content": bot_response})

# Display the chat history
st.write("### Chat History:")
display_chat()

# Add some footer info (optional)
st.markdown("<div style='text-align: center; color: grey;'>Powered by GPT & Streamlit</div>", unsafe_allow_html=True)
