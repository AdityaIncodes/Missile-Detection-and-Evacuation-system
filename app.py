from flask import Flask, jsonify
from alert_system import send_alert

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "System Active",
        "message": "Missile Detection Backend Running"
    })

@app.route("/trigger-alert")
def trigger_alert():

    send_alert("⚠️ Missile Threat Detected! Evacuate Immediately.")

    return jsonify({
        "alert": "Emergency Alert Triggered"
    })

if __name__ == "__main__":
    app.run(debug=True)