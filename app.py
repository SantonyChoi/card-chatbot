import os
from flask import Flask, render_template, request, jsonify
import openai
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/ask", methods=["POST"])
def ask():
    user_input = request.json["question"]

    response = call_openai_api(user_input)

    return jsonify({"response": response})


openai.api_key = os.getenv("OPENAI_API_KEY")


def call_openai_api(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50,  # Limit response to 50 characters
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()


if __name__ == "__main__":
    app.run(debug=True)
