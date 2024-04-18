import os
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage

load_dotenv()

# Access environment variables
senderEmail = os.getenv('senderEmail')
appKey = os.getenv('appKey')

#Sends text message
def send_message(gatewayAddress, message):

    # Send Text
    msg = EmailMessage()
    msg.set_content(message)

    msg['From'] = senderEmail
    msg['To'] = gatewayAddress
    msg['Subject'] = ''

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senderEmail, appKey)


    server.send_message(msg)
    server.quit()


