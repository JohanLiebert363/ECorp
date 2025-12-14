from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)  # allow frontend to access backend

DATA_FILE = "messages.json"
@app.route("/")
def home():
    return render_template("index.html")
from flask import render_template

@app.route("/")

@app.route("/api/contact", methods=["POST"])
def contact():
    data = request.get_json()
    email = data.get("email")
    message = data.get("message")

    if not email or not message:
        return jsonify({"message": "Please fill in all fields"}), 400

    new_entry = {"email": email, "message": message}

    # Load old messages
    messages = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            messages = json.load(f)

    # Append new message
    messages.append(new_entry)

    # Save back to file
    with open(DATA_FILE, "w") as f:
        json.dump(messages, f, indent=4)

    return jsonify({"message": "Message received! Thank you."}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
