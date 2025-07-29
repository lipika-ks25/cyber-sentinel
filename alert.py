import smtplib
from email.message import EmailMessage
import json
with open('config.json')as f:
    config = json.load(f)
def send_email_alert(subject, body):
    msg=EmailMessage()
    msg.set_content(body)
    msg['Subject']= subject
    msg['From']= config["email"]["sender"]
    msg['To']= config["email"]["sender"]

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.login(config["email"]["sender"], config["email"]["password"])
        server.send_message(msg)
        server.quit()
        print(" Email Alert Sent! ")
    except Exception as e:
        print(" Failed To Send Alert:", e)