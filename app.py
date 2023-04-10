from flask import Flask, request, jsonify
import random
import openai

app = Flask(__name__)

@app.route('/api/ask', methods=['POST'])
def ask():
    user_input = request.json['question']

    response = call_openai_api(user_input)

    return jsonify({'response': response})

openai.api_key = "your_api_key"

def call_openai_api(prompt):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=50,  # Limit response to 50 characters
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

if __name__ == '__main__':
    app.run(debug=True)
