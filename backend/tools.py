import ollama
from twilio.rest import Client
import config
from dotenv import load_dotenv
load_dotenv()
import os

def query_medgemma(prompt:str)->str:
    try:
        response = ollama.chat(
            model='alibayram/medgemma:latest',
            messages=[
                {"role": "system", "content": config.system_prompt},
                {"role": "user", "content": prompt}
            ],
            options={
                'num_predict': 350,  # Slightly higher for structured responses
                'temperature': 0.7,  # Balanced creativity/accuracy
                'top_p': 0.9        # For diverse but relevant responses
            }
        )
        return response['message']['content'].strip()
    except Exception as e:
        print(e)
        return f"I'm having technical difficulties, but I want you to know your feelings matter. Please try again shortly."

# Step2: Setup Twilio calling API tool


def call_emergency():
    client = Client(os.getenv("Account_SID"), os.getenv("Auth_Token"))
    call = client.calls.create(
        to=os.getenv("EMERGENCY_CONTACT"),
        from_=os.getenv("TWILIO_FROM_NUMBER"),
        url="http://demo.twilio.com/docs/voice.xml"  # Can customize message
    )
    
# print(query_medgemma("Hello, I am feeling very anxious and overwhelmed lately. Can you help me?"))