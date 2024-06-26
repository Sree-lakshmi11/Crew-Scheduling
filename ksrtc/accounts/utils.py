 
import random
import string
from django.conf import settings
from twilio.rest import Client  # Import the Twilio Client if using Twilio



def generate_otp(length=6):
    characters = string.digits
    otp = ''.join(random.choice(characters) for _ in range(length))
    return otp

def send_otp_phone(phone_number, otp):
    account_sid = 'AC4c3e3201934e14e0cb3244e5903ed4cf'  # Replace with your Twilio account SID
    auth_token = '2bd09aaf17839de5ef535adcbec075b4'  # Replace with your Twilio auth token
    twilio_phone_number = '+12513060608'  # Replace with your Twilio phone number

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f'Your KSRT account login OTP is: {otp}',
        from_ = twilio_phone_number,
        to = phone_number
    )
    
 