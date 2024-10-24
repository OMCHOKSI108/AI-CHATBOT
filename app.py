from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Chatbot logic
def chatbot_response(user_input):
    user_input = user_input.lower()

    # Regex patterns for simple responses
    if re.search(r"(hello|hi|hey)", user_input):
        return "Hello! How can I assist you today in your technical education journey?"
    elif re.search(r"(what courses|available courses)", user_input):
        return "We offer courses like Computer Science, Electrical Engineering, Mechanical Engineering, and more."
    elif re.search(r"(help|support)", user_input):
        return "You can reach out to our support team via email at support@technicaledu.com."
    elif re.search(r"(scholarship|financial aid)", user_input):
        return "Yes, we offer scholarships. Please visit our financial aid section for more details."
    elif re.search(r"(bye|goodbye)", user_input):
        return "Goodbye! Feel free to ask if you have more questions."
    else:
        return "Sorry, I didn't understand that. Can you please rephrase your question?"

# Routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    return chatbot_response(user_text)

if __name__ == "__main__":
    app.run(debug=True)
