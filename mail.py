import smtplib
import os


class SendMsg:
    def __init__(self):
        self.email = os.getenv("EMAIL")
        self.password = os.getenv("EMAIL_PASSWORD")

    def send_email(self, name , email, phone, message):
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            connection.sendmail(from_addr=self.email, to_addrs=email, msg=f"Subject:Welcome form using Flask \n\n Hello {name}, \n Contact No.: {phone} \n message:{message}")

            