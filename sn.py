from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
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

@app.route('/')
def hello():
  return "Hello, World!"

@app.route('/sms', methods=['POST'])
def sms():
  msg = request.values.get('Body')
  res = MessagingResponse()
  res.message("This is a reply")
  return str(res)

app.run(host="0.0.0.0", port="80")
