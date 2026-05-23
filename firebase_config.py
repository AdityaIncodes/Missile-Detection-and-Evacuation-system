import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("firebase_key.json")

firebase_admin.initialize_app(cred)

db = firestore.client()

def log_threat(data):

    db.collection("threat_logs").add(data)

    print("Threat Logged to Firebase")