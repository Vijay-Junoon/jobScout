import smtplib
import os
from dotenv import load_dotenv
from email.message import EmailMessage
from email.utils import make_msgid

load_dotenv()

gmail_password = os.environ['gmail_password']

mail_sender = smtplib.SMTP('smtp.gmail.com', 587)
mail_sender.starttls()
mail_sender.login('jobscout545@gmail.com', gmail_password)


def sendMail(name,email, email_body):

    msg = EmailMessage()

    msg["Subject"] = "JobScout Notification"
    msg["From"] = "jobscout545@gmail.com"
    msg["To"] = email

    image_cid = make_msgid()[1:-1]
    email_body = email_body.replace("\n", "<br>")
    html = f"""
    <html>
    <body>

    <img src="cid:{image_cid}" width="600">

    <h2>Hello {name}!</h2>

    <p>{email_body}</p>

    <p>Thank you.</p>

    </body>
    </html>
    """
    msg.set_content(email_body)

    msg.add_alternative(html, subtype="html")


    with open("src/tools/banner.png", "rb") as img:
        image_data = img.read()

    msg.get_payload()[1].add_related(
        image_data,
        maintype="image",
        subtype="png",
        cid=image_cid
    )


    mail_sender.send_message(msg)

