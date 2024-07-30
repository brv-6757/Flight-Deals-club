from amadeus import Client,ResponseError
import json
from dotenv import load_dotenv
import os
from datetime import datetime,timedelta

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self,origin):
        self.origin = origin
        self.cut_off = 0
        self.dest = ""
        self.dep_date = ""
        self.api_key = os.getenv('API_KEY_AMADEUS')
        self.api_secret = os.getenv('API_SECRET_AMADEUS')
    
    #-------------------------------- Function to connect to amadeus --------------------------#
    def search_flights(self):
        amadeus = Client(client_id=self.api_key,client_secret=self.api_secret)
        try:
            response = amadeus.shopping.flight_offers_search.get(
                originLocationCode=self.origin, destinationLocationCode=self.dest, departureDate=self.dep_date, adults=1)
            return response.data
        except ResponseError as error:
            return -1
    
    #------------------------------- Structuring flight data ----------------------------------#
    def get_flights(self,details):
        self.dest = details['iataCode']
        self.cut_off = details['cutOff']
        curr = datetime.now()
        next_week = curr + timedelta(days=30)
        self.dep_date = next_week.strftime('%Y-%m-%d') 

        flights = self.search_flights()
        if(flights==-1):
            return -1
        elif  len(flights)==0:
            return 0
        else:
            flights = flights[0]
            fare = flights['price']['total']
            if(float(fare)>self.cut_off): return 0

            departure = flights['itineraries'][0]['segments'][0]['departure']['at']
            arrival = flights['itineraries'][0]['segments'][-1]['arrival']['at']
            last_date = flights['lastTicketingDate']
            seats = flights["numberOfBookableSeats"]
            
            flight_info = {
                "departure" : departure,
                "arrival" : arrival,
                "last_date" : last_date,
                "fare" : fare,
                "seats" : seats,
                "dest" : details['city']
            }
            return flight_info







#-------------------------------------------- Authorization ------------------------------------------#
# auth_url = "https://test.api.amadeus.com/v1/security/oauth2/token/"
# auth_body = {
#     "grant_type" : "client_credentials",
#     "client_id" : pw[KEY]["password"],
#     "client_secret" : pw[SECRET]["password"]
# }
# auth_headers = {
#     "Content-Type":"application/x-www-form-urlencoded"
# }
# resp = requests.post(url=auth_url,json=auth_body,headers=auth_headers)
# print(resp.json())
# dt = FlightSearch('HYD')
# print(dt.get_flights('CDG',50,'2024-06-20'))



