from flask import Flask, request, jsonify
import pandas as pd
import random

app = Flask(__name__)

# Step 1: Load the dataset from the Excel file
df = pd.read_excel('DATASET01.xlsx')

# Step 2: Function to find the closest matching response
def get_response(user_input):
    for index, row in df.iterrows():
        patterns = row['patterns'].split(',')  # Assuming patterns are comma-separated
        for pattern in patterns:
            if pattern.strip().lower() in user_input.lower():
                return random.choice(row['responses'].split(','))  # Randomly choose a response
    return "Sorry, I don't have the answer to that question."

# Step 3: Route for chatbot interaction
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get('message', '')
    response = get_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
