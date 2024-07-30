from smtplib import *
import os
from dotenv import load_dotenv

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
#----------- create a .env file to add all the environment variables used here ---------------#
        load_dotenv()
        self.mail = os.getenv('SMTP_MAIL') #smtp credentials
        self.auth = os.getenv('SMTP_PASS')
        self.msg = ""
        self.mails = []

    def send_mails(self,data,mails):
        self.msg = data
        self.mails = mails
        try:
            with SMTP(host="smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=self.mail,password=self.auth)
                for i in self.mails:
                    connection.sendmail(from_addr=self.mail,to_addrs=i,msg=self.msg)
            return 1
        except:
            return "error"
        
        
# def main():
#     noti = NotificationManager()
#     print(noti.send_mails("hello user",['b.rohithvarma@gmail.com','vinitkumarjsr08@gmail.com']))

# main()