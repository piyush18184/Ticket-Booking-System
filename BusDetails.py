class BusDetails:
    list_of_buses=[];
    list_of_bus_bookings = [];
    list_of_bus_confirmed_bookings = [];
    def __init__(self,b_name,b_source,b_destination,b_type,b_price,b_date):
        self.b_name=b_name
        self.b_price=b_price
        self.b_source=b_source
        self.b_destination=b_destination
        self.b_type=b_type
        self.b_date=b_date
        self.list_of_buses.append(self)

    def GetBusName(self):
        return self.b_name

    def GetBusPrice(self):
        return self.b_price

    def GetBusSource(self):
        return self.b_source

    def GetBusDestination(self):
        return self.b_destination

    def GetBusType(self):
        return self.b_type

    def GetBusDate(self):
        return self.b_date

    def BookBus(b_name, b_date, b_source, b_destination):
        arr = [b_name, b_date, b_source, b_destination]
        BusDetails.list_of_bus_bookings.append(arr)

    def ModifyBookBus(self):
        BusDetails.list_of_bus_bookings.pop(0)

    def ConfirmedBooking(self):
        BusDetails.list_of_bus_confirmed_bookings=BusDetails.list_of_bus_bookings

    def GetConfirmedBooking(self):
        return BusDetails.list_of_bus_confirmed_bookings

    def ModifyConfirmedBookBus(self):
        BusDetails.list_of_bus_confirmed_bookings.pop(0)

b1=BusDetails("Indigo Pvt. Ltd.","Lucknow","Delhi","AC Seater    ",1000,"01/10/18")
b2=BusDetails("Josh Travels","Lucknow","Delhi","Sleeper    ",3000,"01/10/18")
b3=BusDetails("Non Stop Goers","Varanasi","Ahmedabad","Sleeper",800,"01/10/18")
b4=BusDetails("Hakamura Travels","Bangalore","Trivandrum","AC Sleeper   ",1500,"01/10/18")
b5=BusDetails("Jai Travellers","Goa","Mumbai","Sleeper",200,"01/10/18")
b6=BusDetails("Jai Travellers","Mumbai","Chennai","Seater     ",100,"01/10/18")
b7=BusDetails("Kumar Non Stop","'Delhi","Lucknow","Seater",315,"01/10/18")