from flask import Flask, render_template, request, redirect, url_for, jsonify
import cohere
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("COHERE_API_KEY")
co = cohere.Client(api_key)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    return redirect(url_for('chatbot'))

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message')
    try:
        response = co.chat(
            message=user_message,
            model="command-r"
        )
        return jsonify({'response': response.text})
    except Exception as e:
        return jsonify({'response': f"Error: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)

