import requests
from dotenv import load_dotenv
import os
from smtplib import *
load_dotenv()
auth = os.getenv('SHEETY_AUTH')
DestUrl = os.getenv('SHEETY_DEST_URL')
UsersUrl = os.getenv('SHEETY_USERS_URL')
resp = requests.get(url=UsersUrl,headers={"Authorization":auth})
print(resp.json())
users = [i['emailId'] for i in resp.json()['users']]
print(type(users[0]))
# with SMTP(host="smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=mail,password=auth)
#     connection.sendmail(from_addr=mail,to_addrs="vinitkumarjsr08@gmail.com",msg="Subject: HEY GND\n\n Hello Vinit Pinit kumar")
