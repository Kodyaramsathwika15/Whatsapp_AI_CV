# WhatsApp to Google Sheets Bot (pyngrok version)

## Setup

1. Place your Google credentials JSON file as `credentials.json` in this folder.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run Flask app:
   ```
   python app.py
   ```
4. Copy the **Public URL** printed in the console (from pyngrok).
5. Go to Twilio Sandbox → When a message comes in → paste:
   ```
   <Public URL>/webhook
   ```
6. Join the Twilio sandbox with your WhatsApp number.
7. Send a message → it will be logged in Google Sheets and you will get a reply.
