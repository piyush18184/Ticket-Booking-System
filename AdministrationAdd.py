class AdministrationAdd:
    new_flight=[];
    new_flight_added=[];
    new_train = [];
    new_train_added = [];
    new_bus = [];
    new_bus_added = [];
    def AddFlight(f_num,f_name,f_source,f_destination,f_type,f_price,f_date):
        for i in range (0,1):
            AdministrationAdd.new_flight.append(f_num)
            AdministrationAdd.new_flight.append(f_name)
            AdministrationAdd.new_flight.append(f_source)
            AdministrationAdd.new_flight.append(f_destination)
            AdministrationAdd.new_flight.append(f_type)
            AdministrationAdd.new_flight.append(f_price)
            AdministrationAdd.new_flight.append(f_date)
            break
        AdministrationAdd.new_flight_added=AdministrationAdd.new_flight

    def AddTrain(t_num,t_name,t_source,t_destination,t_type,t_price,t_date):
        for i in range (0,1):
            AdministrationAdd.new_train.append(t_num)
            AdministrationAdd.new_train.append(t_name)
            AdministrationAdd.new_train.append(t_source)
            AdministrationAdd.new_train.append(t_destination)
            AdministrationAdd.new_train.append(t_type)
            AdministrationAdd.new_train.append(t_price)
            AdministrationAdd.new_train.append(t_date)
            break
        AdministrationAdd.new_train_added=AdministrationAdd.new_train

    def AddBus(b_name,b_source,b_destination,b_type,b_price,b_date):
        for i in range (0,1):
            AdministrationAdd.new_bus.append(b_name)
            AdministrationAdd.new_bus.append(b_source)
            AdministrationAdd.new_bus.append(b_destination)
            AdministrationAdd.new_bus.append(b_type)
            AdministrationAdd.new_bus.append(b_price)
            AdministrationAdd.new_bus.append(b_date)
            break
        AdministrationAdd.new_bus_added=AdministrationAdd.new_bus
