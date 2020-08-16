import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

sender_email = os.getenv("MY_EMAIL")
receiver_email = os.getenv("YOUR_EMAIL")
password = os.getenv("MY_PASSWORD")

def sendEmail(title, url):  
  message = MIMEMultipart("alternative")
  message["Subject"] = title
  message["From"] = sender_email
  message["To"] = receiver_email

  # Create the plain-text and HTML version of your message
  text = f"""\
  {url}
  """
  html = f"""\
  <html>
    <body>
        <a href="{url}">{url}</a> 
    </body>
  </html>
  """

  # Turn these into plain/html MIMEText objects
  part1 = MIMEText(text, "plain")
  part2 = MIMEText(html, "html")

  # Add HTML/plain-text parts to MIMEMultipart message
  # The email client will try to render the last part first
  message.attach(part1)
  message.attach(part2)

  # Create secure connection with server and send email
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(
          sender_email, receiver_email, message.as_string()
      )
  
  print("Email SENT!")
  os.system(f'spd-say "{title}"')