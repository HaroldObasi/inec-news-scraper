import smtplib
from email.message import EmailMessage
from template import generate_html

app_name = "smtp_client_selenium"
app_password = "ddzqjpdefuqsoxpn"
data = ["harold", "gaius", "fadil"]

def send_emails(reciever, payload, data):
  msg = EmailMessage()
  msg["Subject"] = payload["subject"]
  msg["From"] = "Harold's Automated Bot"
  msg["To"] = reciever
  msg.set_content(payload["body"])
  msg.add_alternative(generate_html(data), subtype='html')
  with smtplib.SMTP_SSL(host="smtp.gmail.com", port=465) as smtp:
    smtp.login("haroldobasibackup@gmail.com", app_password)
    smtp.send_message(msg)

