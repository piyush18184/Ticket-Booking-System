from datetime import *
from AdministrationAdd import *

class FlightDetails(AdministrationAdd):
    list_of_flights=[];
    list_of_flight_bookings=[];
    list_of_flight_confirmed_bookings = [];
    def __init__(self,f_num,f_name,f_source,f_destination,f_type,f_price,f_date):
        self.f_num=f_num
        self.f_name=f_name
        self.f_price=f_price
        self.f_source=f_source
        self.f_destination=f_destination
        self.f_type=f_type
        self.f_date=f_date
        self.list_of_flights.append(self)

    def GetFlightNumber(self):
        return self.f_num

    def GetFlightName(self):
        return self.f_name

    def GetFlightPrice(self):
        return self.f_price

    def GetFlightSource(self):
        return self.f_source

    def GetFlightDestination(self):
        return self.f_destination

    def GetFlightType(self):
        return self.f_type

    def GetFlightDate(self):
        return self.f_date

    def GetConfirmedFlightBooking(self):
        return FlightDetails.list_of_flight_confirmed_bookings

    def BookFlight(f_num,f_date,f_source,f_destination):
        arr=[f_num,f_date,f_source,f_destination]
        FlightDetails.list_of_flight_bookings.append(arr)

    def ModifyBookFlight(self):
        FlightDetails.list_of_flight_bookings.pop(0)

    def ModifyConfirmedBookFlight(self):
        FlightDetails.list_of_flight_confirmed_bookings.pop(0)

    def ConfirmedBooking(self):
        FlightDetails.list_of_flight_confirmed_bookings=FlightDetails.list_of_flight_bookings

    def GetConfirmedBooking(self):
        return FlightDetails.list_of_flight_confirmed_bookings

    def GetAll(f_num):
        for i in FlightDetails.list_of_flights:
            if f_num==i.GetFlightNumber():
                print(i.GetFlightName(),i.GetFlightNumber())

f1=FlightDetails("AI103","Air India","Delhi","Mumbai","Economy",4000,"01/11/18")
f2=FlightDetails("AI243","Air India","Lucknow","Chennai","Economy",5000,"01/10/18")
f3=FlightDetails("AI553","Air India","Varanasi","Ahmedabad","Business",20000,"01/10/18")
f4=FlightDetails("JA113","Jet Airways","Bangalore","Trivandrum","Business",30000,"01/10/18")
f5=FlightDetails("JA993","Jet Airways","Goa","Mumbai","Business",40000,"01/10/18")
f6=FlightDetails("IA543","Indian Airlines","Mumbai","Chennai","Economy",2000,"01/10/18")
f7=FlightDetails("IA323","Indian Airlines","Delhi","Mumbai","Economy",4000,"15/10/18")