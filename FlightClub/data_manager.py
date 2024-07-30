import requests
# import json
import os
from dotenv import load_dotenv
test_path = "C:\\Users\\rohit\\VS CODE\\VS CODE PY\\projects\\flight-deals-start\\test_file.json"
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        load_dotenv()
        self.auth = os.getenv('SHEETY_AUTH')
        self.DestUrl = os.getenv('SHEETY_DEST_URL')
        self.UsersUrl = os.getenv('SHEETY_USERS_URL')
        # self.status_code = ""
        self.header = {
            "Authorization" : self.auth
        }

    def getDest(self):
        try:
            resp = requests.get(url=self.DestUrl,headers=self.header)
            # self.status_code = resp.status_code
            if(len(resp.json()['destinations'])==0):
                return -1
            else: 
                return resp.json()['destinations']
        except:
            return "error"
    def getUsers(self):
        try:
            resp = requests.get(url=self.UsersUrl,headers=self.header)
            # print(resp.json())
            if(len(resp.json()['users'])==0):
                return -1
            users = [i['emailId'] for i in resp.json()['users']]
            # print(users)
            return users
        except:
            return "error"
# print(resp.status_code,resp.json())
# with open(test_path,'w') as file:
#     json.dump(resp.json(),file,indent=3)
# dt = DataManager()
# print(dt.getUsers())
# print(dt.status_code)