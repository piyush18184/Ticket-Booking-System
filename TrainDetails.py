class TrainDetails:
    list_of_trains=[];
    list_of_train_bookings = [];
    list_of_train_confirmed_bookings = [];
    def __init__(self,t_num,t_name,t_source,t_destination,t_type,t_price,t_date):
        self.t_num=t_num
        self.t_name=t_name
        self.t_price=t_price
        self.t_source=t_source
        self.t_destination=t_destination
        self.t_type=t_type
        self.t_date=t_date
        self.list_of_trains.append(self)

    def GetTrainNumber(self):
        return self.t_num

    def GetTrainName(self):
        return self.t_name

    def GetTrainPrice(self):
        return self.t_price

    def GetTrainSource(self):
        return self.t_source

    def GetTrainDestination(self):
        return self.t_destination

    def GetTrainType(self):
        return self.t_type

    def BookTrain(t_num, t_date, t_source, t_destination):
        arr = [t_num, t_date, t_source, t_destination]
        TrainDetails.list_of_train_bookings.append(arr)

    def ModifyBookTrain(self):
        TrainDetails.list_of_train_bookings.pop(0)

    def ConfirmedBooking(self):
        TrainDetails.list_of_train_confirmed_bookings=TrainDetails.list_of_train_bookings

    def GetConfirmedBooking(self):
        return TrainDetails.list_of_train_confirmed_bookings

    def ModifyConfirmedBookTrain(self):
        TrainDetails.list_of_train_confirmed_bookings.pop(0)

    def GetTrainDate(self):
        return self.t_date

t1=TrainDetails("12229","Lucknow Mail   ","Lucknow","Delhi","3AC    ",1000,"01/10/18")
t2=TrainDetails("12343","Duronto        ","Lucknow","Delhi","1AC    ",3000,"01/10/18")
t3=TrainDetails("15538","Jansadharan    ","Varanasi","Ahmedabad","Sleeper",800,"01/10/18")
t4=TrainDetails("19897","Tiri Express   ","Bangalore","Trivandrum","2AC    ",1500,"01/10/18")
t5=TrainDetails("11233","Goa Superfast  ","Goa","Mumbai","Sleeper",200,"01/10/18")
t6=TrainDetails("14567","Chennai Express","Mumbai","Chennai","2S     ",100,"01/10/18")
t7=TrainDetails("13378","Kaifiyat       ","'Delhi","Lucknow","Sleeper",315,"01/10/18")