from flask import Flask, render_template, request, jsonify
from chatbot import get_gemini_response
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_input = request.json.get("message")
        if not user_input:
            return jsonify({"response": "Please enter a message."})

        bot_response = get_gemini_response(user_input)
        return jsonify({"response": bot_response})

    except Exception as e:
        return jsonify({"response": f"❌ Server error: {str(e)}"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render gives a PORT env variable
    app.run(host='0.0.0.0', port=port)
