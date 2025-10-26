from flask import Flask, request
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("CV_AI_DATA").sheet1  # Change to your Google Sheet name

@app.route("/webhook", methods=["POST"])
def webhook():
    msg_body = request.form.get('Body')
    from_number = request.form.get('From')
    
    # Log to Google Sheet
    sheet.append_row([from_number, msg_body])
    
    # Reply via WhatsApp
    resp = MessagingResponse()
    resp.message(f"Hello! Your message '{msg_body}' has been logged.")
    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

@app.route("/", methods=["GET"])
def index():
    return "WhatsApp bot is running!"
