import streamlit as st
import openai



# Set your OpenAI API key here
openai.api_key = "sk-RtIcDj3xQKXsHdjHs_-7l8w0Q5PIlrPFjwtTwfgFX2T3BlbkFJP72uTDRMEnMAnU8rMCP2iPmS3I_if6Sbx_Fp627TUA"
# Custom CSS for a better look
def add_custom_css():
    st.markdown("""
        <style>
        /* Background color */
        body {
            background-color: #1a1a2e;
            color: #ffffff;
        }

        /* Chat box input styling */
        .stTextInput > div > input {
            background-color: #0f3460;
            color: #e94560;
            border: none;
            border-radius: 10px;
            padding: 10px;
            font-size: 16px;
            width: 100%;
            height: 50px;
        }

        /* Chat text appearance */
        .chat-message {
            background-color: #16213e;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 10px;
            font-size: 16px;
            border: 1px solid #0f3460;
        }

        /* User input style */
        .user-input {
            background-color: #0f3460;
            color: #e94560;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
            border: 1px solid #e94560;
            font-weight: bold;
        }

        /* Bot response style */
        .bot-response {
            background-color: #16213e;
            color: #ffffff;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
            border: 1px solid #0f3460;
        }

        /* Chatbot title */
        .title h1 {
            color: #e94560;
            font-family: 'Helvetica', sans-serif;
        }

        </style>
    """, unsafe_allow_html=True)

# Call the custom CSS
add_custom_css()

# Title section with styling
st.markdown('<div class="title"><h1>✨ Technical Education Chatbot ✨</h1></div>', unsafe_allow_html=True)

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

# Display the conversation history with custom styling
st.write("<h3>Chat History:</h3>", unsafe_allow_html=True)

for chat in st.session_state.conversation:
    st.markdown(f'<div class="user-input">**You:** {chat["user"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="bot-response">**Bot:** {chat["bot"]}</div>', unsafe_allow_html=True)
