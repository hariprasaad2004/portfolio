from flask import Flask, request, jsonify, send_from_directory
import os
from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route("/")
def home():
    return send_from_directory("static", "index.html")
# ----------------------------------------------------
# 🔶 FILL THIS SECTION WITH YOUR GMAIL & APP PASSWORD
# ----------------------------------------------------
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True

app.config['MAIL_USERNAME'] = "hariprasaadmurugesan2004@gmail.com" 
# Example: app.config['MAIL_USERNAME'] = "hariprasaadmurugesan2004@gmail.com"

app.config['MAIL_PASSWORD'] = "qglk vnam bsuu dvsq"
# Example: app.config['MAIL_PASSWORD'] = 'abcd efgh ijkl mnop'
# ----------------------------------------------------

app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME']

mail = Mail(app)

@app.route("/sendmail", methods=["POST"])
def send_mail():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    message_text = data.get("message")

    msg = Message(
        subject=f"New Portfolio Message from {name}",

        # ----------------------------------------------------
        # 🔶 FILL THIS WITH YOUR GMAIL (THIS IS WHERE MAIL ARRIVES)
        # ----------------------------------------------------
        recipients=["hariprasaadmurugesan2004@gmail.com"],  
        # Example: recipients=["hariprasaad123@gmail.com"],
        # ----------------------------------------------------

        body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_text}"
    )

    mail.send(msg)
    return jsonify({"status": "success", "message": "Mail sent!"}), 200

if __name__ == "__main__":
    app.run(debug=True)





#YOUR_EMAIL = "hariprasaadmurugesan2004@gmail.com"
#YOUR_PASSWORD = "qglk vnam bsuu dvsq"
