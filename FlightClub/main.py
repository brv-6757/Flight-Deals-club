#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

class FlightDeals:
    def __init__(self,origin):
        self.data = DataManager()
        self.search = FlightSearch(origin)
        self.msg = FlightData()
        self.notify = NotificationManager()

    def get_deals(self):
        destinations = self.data.getDest()
        if(destinations=="error"):
            return "error at destinations: couldn't load data"
        if(destinations==-1):
            return "No data to load"
        flights=[]
        for i in destinations:
            f = self.search.get_flights(i)
            if(f==-1):
                return "error at flight search"
            elif(f!=0):
                flights.append(f)
        if(len(flights)!=0):
            msg = self.msg.data(flights)
            mails = self.data.getUsers()
            if(mails==-1):
                print("No Users to send mails")
            if(mails=='error'): 
                print("Error while sending mails")
            notification = self.notify.send_mails(msg,mails)
            if(notification=="error"):
                return "couldn't send message"
            return "sent"
        return "no flights"
        

f1 = FlightDeals('HYD')
print(f1.get_deals())
        