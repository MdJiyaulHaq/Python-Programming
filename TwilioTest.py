from twilio import Client

account_sid = "your_account_sid"
auth_token = "your_auth_token"

client = Client(account_sid, auth_token)


def send_sms(to, from_, body):
    try:
        message = client.messages.create(to=to, from_=from_, body=body)
        print(f"Message sent successfully: {message.sid}")
    except Exception as e:
        print(f"Failed to send message: {e}")
