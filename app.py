import streamlit as st
import openai

# Set your OpenAI API key here
openai.api_key = "sk-RtIcDj3xQKXsHdjHs_-7l8w0Q5PIlrPFjwtTwfgFX2T3BlbkFJP72uTDRMEnMAnU8rMCP2iPmS3I_if6Sbx_Fp627TUA"

# Streamlit app title
st.title("Technical Education Chatbot with OpenAI")

# Initialize session state to store the conversation history
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Function to get response from OpenAI
def get_openai_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can also use "gpt-4" if available in your API
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Create a text input for user queries
user_input = st.text_input("Ask me anything about technical education:")

# When the user submits a question
if user_input:
    # Call the OpenAI API to get a response
    response = get_openai_response(user_input)
    
    # Append user input and response to conversation history
    st.session_state.conversation.append({"user": user_input, "bot": response})

# Display the conversation history
for chat in st.session_state.conversation:
    st.write(f"**You:** {chat['user']}")
    st.write(f"**Bot:** {chat['bot']}")
