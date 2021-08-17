import sendgrid
import os

from sendgrid.helpers.mail import *
from dotenv import load_dotenv


load_dotenv()

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
from_email = Email(os.environ.get('SENDER'))
to_email = To(os.environ.get('RECEIVER'))
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, to_email, subject, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)