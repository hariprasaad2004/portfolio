from flask import Flask, send_from_directory, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS
import os

app = Flask(__name__, static_folder="static")
CORS(app)

# Serve index.html
@app.route("/")
def index():
    return send_from_directory("static", "index.html")

# Serve CSS, JS, Images correctly
@app.route("/static/<path:path>")
def serve_static(path):
    return send_from_directory("static", path)

# ---- EMAIL CONFIG ----
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True

app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME']

mail = Mail(app)

@app.route("/sendmail", methods=["POST"])
def send_mail():
    data = request.json

    name = data["name"]
    email = data["email"]
    mobile = data["mobile"]
    subject = data["subject"]
    message_text = data["message"]

    body = f"""
New portfolio message:

Name: {name}
Email: {email}
Mobile: {mobile}
Subject: {subject}

Message:
{message_text}
"""

    msg = Message(
        subject=f"Portfolio Message: {subject}",
        recipients=["hariprasaadmurugesan2004@gmail.com"],
        body=body,
        reply_to=email
    )

    mail.send(msg)
    return jsonify({"status": "success"}), 200


if __name__ == "__main__":
    app.run()
