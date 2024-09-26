from flask import Flask, render_template, request
from twilio.rest import Client
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)

# Twilio Credentials from environment variables
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/make_call', methods=['POST'])
def make_call():
    to_number = request.form['to_number']
    
    call = client.calls.create(
        twiml='<Response><Say>Calling from your Twilio Bot. Please hold.</Say></Response>',
        to=to_number,
        from_=TWILIO_PHONE_NUMBER
    )
    
    return f"Call initiated with ID: {call.sid}"

if __name__ == '__main__':
    app.run(debug=True)
    
