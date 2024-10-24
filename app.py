import openai
import streamlit as st

openai.api_key = "sk-RtIcDj3xQKXsHdjHs_-7l8w0Q5PIlrPFjwtTwfgFX2T3BlbkFJP72uTDRMEnMAnU8rMCP2iPmS3I_if6Sbx_Fp627TUA"

st.set_page_config(page_title="Technical Education Chatbot", page_icon=":robot_face:", layout="centered")
st.title("🤖 Technical Education Chatbot")

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

def get_openai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant knowledgeable in technical education."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

def display_chat():
    for message in st.session_state['messages']:
        if message['role'] == 'user':
            st.markdown(f"**You:** {message['content']}")
        else:
            st.markdown(f"**Bot:** {message['content']}")
    st.write("---")

user_input = st.text_input("Ask me anything about technical education:")

if user_input:
    st.session_state['messages'].append({"role": "user", "content": user_input})
    bot_response = get_openai_response(user_input)
    st.session_state['messages'].append({"role": "assistant", "content": bot_response})

st.write("### Chat History:")
display_chat()

st.markdown("<div style='text-align: center; color: grey;'>Powered by GPT & Streamlit</div>", unsafe_allow_html=True)
