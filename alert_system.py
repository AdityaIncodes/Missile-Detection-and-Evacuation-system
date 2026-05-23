from twilio.rest import Client

# Twilio credentials
account_sid = "YOUR_TWILIO_SID"
auth_token = "YOUR_TWILIO_AUTH_TOKEN"

client = Client(account_sid, auth_token)

def send_alert(message):

    client.messages.create(
        body=message,
        from_="+1234567890",
        to="+919999999999"
    )

    print("Emergency Alert Sent!")