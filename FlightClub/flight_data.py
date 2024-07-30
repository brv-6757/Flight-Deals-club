from random import choice
class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.first = ["GRAB THE DEAL!!!","PACK YOUUR BAGS!!","YOU GOT A DEAL!!","IT'S TIME TO MOVE!!"]
        self.msg = f"Subject:{choice(self.first)}\n\nBook Your Flight Now. Here Are Your Deals:\n"

    def data(self,flight):
        for deals in flight:
            dep_date = deals['departure'].split('T')[0]
            dep_time = deals['departure'].split('T')[1]
            arr_date = deals['arrival'].split('T')[0]
            arr_time = deals['arrival'].split('T')[1]
            last_date = deals['last_date']
            fare = deals['fare']
            dest = deals['dest']
            messg = f"Price: {fare} EUR!!\nleave from: Hyderabad on {dep_date} at {dep_time}\nreach: {dest} on {arr_date} at {arr_time}\nbook before {last_date} only {deals['seats']} seats left!!!\n\n"
            self.msg += messg
        return self.msg