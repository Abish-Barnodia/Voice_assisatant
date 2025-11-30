from flask import Flask, request, jsonify
from flask_cors import CORS

import pyttsx3
import google.generativeai as genai

# Directly set Gemini API key (user request)
GOOGLE_API_KEY = "AIzaSyCLjX4ohuSQcwP5vo2hdK-gXu8xleUABWU"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("models/gemini-2.5-pro")

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    if not user_message:
        return jsonify({'reply': "I didn't get your message."})
    # Special commands
    if "stop the program" in user_message.lower():
        shutdown = request.environ.get('werkzeug.server.shutdown')
        if shutdown is not None:
            shutdown()
        return jsonify({'reply': "Stopping now and shutting down the server."})
    if "exit" in user_message.lower() or "quit" in user_message.lower():
        return jsonify({'reply': "Goodbye!"})
    if "your name" in user_message.lower():
        return jsonify({'reply': "My name is Peter."})
    if "how old are you" in user_message.lower():
        return jsonify({'reply': "I am 2 years old."})
    if "time" in user_message.lower():
        import datetime
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return jsonify({'reply': f"The time is {current_time}"})
    # Otherwise, use Gemini
    try:
        response = model.generate_content(user_message)
        return jsonify({'reply': response.text})
    except Exception as e:
        return jsonify({'reply': f"AI error: {e}"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
