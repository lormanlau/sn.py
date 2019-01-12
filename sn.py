from flask import Flask
from twilio.rest import Client
from config import account_sid, auth_token

app = Flask(__name__)

account_sid = account_sid
auth_token = auth_token
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hello World",
                     from_='+16502977449',
                     to='+15106485381'
                 )

@app.route('/', methods=['GET', 'POST'])
def sms():
  return "Hello, World!"

app.run(debug = True)