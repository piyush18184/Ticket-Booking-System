from Admin import *
from FlightDetails import *
from TrainDetails import *
from BusDetails import *
from AdministrationDetails import *
import sys
from datetime import *
from AdministrationAdd import *

if __name__ == '__main__':
    print()
    print("-------------Make My Trip-------------")
    print("-----------1. Admin Login-------------")
    print("-----------2. User Login--------------")
    print("----------Enter your choice-----------")
    abc=int(input())
    if abc==1:
        c = 1;
        while c <= 3:
            print()
            print("LOGIN WINDOW:")
            print()
            print("Enter the Email")
            em = input()
            print("Enter the password")
            ps = input()
            print()
            for i in AdministrationDetails.list_of_admins:
                if (i.GetUserEmail()==em) and (i.GetUserPassword()==ps):
                    print("Login Succesful")

                    while True:
                        print()
                        print("1:View Self Details")
                        print("2:View User Details")
                        print("3:Add/Remove Flight")
                        print("4:Add/Remove Train")
                        print("5:Add/Remove Bus")
                        print("Press any other key to exit")
                        print()
                        print("Enter choice:")
                        num = int(input())
                        print()

                        while True:

                            if num == 1:
                                print("User's Details:")
                                print("USERID", "         ", "USER NAME", "             ", "EMAIL ADDRESS",
                                      "             ", "PASSWORD")
                                print(i.GetUserID(), "     ", i.GetUserName(), "     ", i.GetUserEmail(), "     ",
                                      i.GetUserPassword())
                                break

                            elif num == 2:
                                print("User's Details:")
                                for i in Admin.list_of_users:
                                    print(i.GetUserID(),"",i.GetUserName(),"",i.GetUserEmail(),"",i.GetUserPassword())
                                break

                            elif num == 3:
                                print()
                                print("Enter your choice:")
                                print("1. Add Flight:")
                                print("2. Go to Home Page")
                                print("Press Any other key to Log Out")
                                print()
                                n = int(input())
                                print()
                                if n == 1:
                                    print("Enter the flight details:")
                                    f_num = input("Enter the flight number")
                                    f_name = input("Enter the flight name")
                                    f_source = input("Enter the flight source")
                                    f_destination = input("Enter the flight destination")
                                    f_type = input("Enter the flight type")
                                    f_price = input("Enter the flight price")
                                    f_date = input("Enter the flight date")
                                    AdministrationAdd.AddFlight(f_num,f_name,f_source,f_destination,f_type,f_price,f_date)
                                    print("Details Added Successfully...")
                                    for i in FlightDetails.list_of_flights:
                                        print(i.GetFlightNumber(),"",i.GetFlightName(),"",i.GetFlightSource(),"",
                                              i.GetFlightDestination(),"",i.GetFlightPrice(),"",i.GetFlightDate(),"",i.GetFlightType())
                                    for j in AdministrationAdd.new_flight_added[-1]:
                                        print(AdministrationAdd.new_flight_added[0], "", AdministrationAdd.new_flight_added[1], "", AdministrationAdd.new_flight_added[2], "",
                                              AdministrationAdd.new_flight_added[3], "", AdministrationAdd.new_flight_added[5],
                                              "",AdministrationAdd.new_flight_added[6],"", AdministrationAdd.new_flight_added[4])
                                        break

                                elif n == 2:
                                    break

                                else:
                                    sys.exit()

                            elif num == 4:
                                print()
                                print("Enter your choice:")
                                print("1. Add Train:")
                                print("2. Go to Home Page")
                                print("Press Any other key to Log Out")
                                print()
                                n = int(input())
                                print()
                                if n == 1:
                                    print("Enter the train details:")
                                    t_num = input("Enter the train number")
                                    t_name = input("Enter the train name")
                                    t_source = input("Enter the train source")
                                    t_destination = input("Enter the train destination")
                                    t_type = input("Enter the train type")
                                    t_price = input("Enter the train price")
                                    t_date = input("Enter the train date")
                                    AdministrationAdd.AddTrain(t_num, t_name, t_source, t_destination, t_type, t_price,
                                                                t_date)
                                    print("Details Added Successfully...")
                                    for i in TrainDetails.list_of_trains:
                                        print(i.GetTrainNumber(), "", i.GetTrainName(), "", i.GetTrainSource(), "",
                                              i.GetTrainDestination(), "", i.GetTrainPrice(), "", i.GetTrainDate(),
                                              "", i.GetTrainType())
                                    for j in AdministrationAdd.new_train_added[-1]:
                                        print(AdministrationAdd.new_train_added[0], "",
                                              AdministrationAdd.new_train_added[1], "",
                                              AdministrationAdd.new_train_added[2], "",
                                              AdministrationAdd.new_train_added[3], "",
                                              AdministrationAdd.new_train_added[5], "",
                                              AdministrationAdd.new_train_added[6], "",
                                              AdministrationAdd.new_train_added[4])
                                        break

                                elif n == 2:
                                    break

                                else:
                                    sys.exit()

                            elif num == 5:
                                print()
                                print("Enter your choice:")
                                print("1. Add Bus:")
                                print("2. Go to Home Page")
                                print("Press Any other key to Log Out")
                                print()
                                n = int(input())
                                print()
                                if n == 1:
                                    print("Enter the train details:")
                                    b_name = input("Enter the bus name")
                                    b_source = input("Enter the bus source")
                                    b_destination = input("Enter the bus destination")
                                    b_type = input("Enter the bus type")
                                    b_price = input("Enter the bus price")
                                    b_date = input("Enter the bus date")
                                    AdministrationAdd.AddTrain(b_name, b_source, b_destination, b_type, b_price,
                                                               b_date)
                                    print("Details Added Successfully...")
                                    for i in BusDetails.list_of_buses:
                                        print(i.GetBusName(), "", i.GetBusSource(), "",
                                              i.GetBusDestination(), "", i.GetBusPrice(), "", i.GetBusDate(),
                                              "", i.GetBusType())
                                    for j in AdministrationAdd.new_bus_added[-1]:
                                        print(AdministrationAdd.new_bus_added[0], "",
                                              AdministrationAdd.new_bus_added[1], "",
                                              AdministrationAdd.new_bus_added[2], "",
                                              AdministrationAdd.new_bus_added[3], "",
                                              AdministrationAdd.new_bus_added[5], "",
                                              AdministrationAdd.new_bus_added[6], "",
                                              AdministrationAdd.new_bus_added[4])
                                        break

                                elif n == 2:
                                    break

                                else:
                                    sys.exit()

                            else:
                                sys.exit()
            print("Invalid Details")
            print("Total Incorrect Attempts:", c)
            print(3 - c, "more attempts left")
            c = c + 1

        print("Exiting.....Press Any Key to continue")
        input()
        sys.exit()

    elif abc==2:
        c = 1;
        while c<=3:
            print()
            print("LOGIN WINDOW:")
            print()
            print("Enter the Email")
            em = input()
            print("Enter the password")
            ps = input()
            print()
            for i in Admin.list_of_users:
                if (i.GetUserEmail()==em) and (i.GetUserPassword()==ps):
                    print("Login Succesful")

                    while True:
                        print()
                        print("1:View User Details")
                        print("2:New Booking")
                        print("3:Manage Current Bookings")
                        print("4:History of Bookings")
                        print("Press any other key to exit")
                        print()
                        print("Enter choice:")
                        num = int(input())
                        print()

                        while True:



                            if num == 1:
                                print("User's Details:")
                                print("USERID", "         ", "USER NAME", "             ", "EMAIL ADDRESS", "             ","PASSWORD")
                                print(i.GetUserID(), "     ", i.GetUserName(), "     ", i.GetUserEmail(), "     ",i.GetUserPassword())
                                break




                            elif num == 2:
                                print()
                                print("Enter the type of booking:")
                                print("1. Airline:")
                                print("2. Train:")
                                print("3. Bus:")
                                print("4. Go to Home Page")
                                print("Press Any other key to Log Out")
                                print()
                                n = int(input())
                                print()
                                if n == 1:
                                    cyn=input("Do you have a coupon code(Y/N)")
                                    if cyn=='Y' or cyn=='y':
                                        cou=input("Enter the coupon code")
                                        if cou in AdministrationDetails.list_of_coupons:
                                            print("Coupon Applied...Cashback will be credited post travel")
                                            s=input("Enter the Source:")
                                            d=input("Enter the Destination:")
                                            da=input("Enter the Date of Journey:")
                                            print()
                                            print("NUMBER", "        ", "NAME", "            ", "PRICE", "     ", "TYPE")
                                            print()
                                            for i in FlightDetails.list_of_flights:
                                                if (i.GetFlightSource() == s) and (i.GetFlightDestination() == d) and (i.GetFlightDate() == da):
                                                    print(i.GetFlightNumber(), "     ", i.GetFlightName(), "     ", i.GetFlightPrice(), "     ",i.GetFlightType(),"     ",i.GetFlightDate())
                                                else:
                                                    pass
                                            print()
                                            print("Enter the Flight Number to create a booking")
                                            fn = input()
                                            for i in FlightDetails.list_of_flights:
                                                if (i.GetFlightSource() == s) and (i.GetFlightDestination() == d) and (
                                                        i.GetFlightNumber() == fn) and (i.GetFlightDate() == da):
                                                    FlightDetails.BookFlight(fn,da,s,d)
                                                else:
                                                    pass
                                            sel_flight = FlightDetails.list_of_flight_bookings[-1]
                                            for j in FlightDetails.list_of_flight_bookings[-1]:
                                                print("Selected Flight Number:", sel_flight)
                                                print("Want to continue with current selection,  (Y/N)")
                                                con = input()
                                                if con == 'Y' or con == 'y':
                                                    FlightDetails.ConfirmedBooking(
                                                        FlightDetails.list_of_flight_bookings)
                                                    print("Booking Confirmed")
                                                    break
                                                else:
                                                    FlightDetails.ModifyBookFlight(
                                                        FlightDetails.list_of_flight_bookings)
                                                    print("Removed Current Selection")
                                                    print("Make new selection")
                                                    break
                                        else:
                                            print("Invalid Coupon")
                                            break
                                    else:
                                        s = input("Enter the Source:")
                                        d = input("Enter the Destination:")
                                        da = input("Enter the Date of Journey:")
                                        print()
                                        print("NUMBER", "        ", "NAME", "            ", "PRICE", "     ", "TYPE")
                                        print()
                                        for i in FlightDetails.list_of_flights:
                                            if (i.GetFlightSource() == s) and (i.GetFlightDestination() == d) and (
                                                    i.GetFlightDate() == da):
                                                print(i.GetFlightNumber(), "     ", i.GetFlightName(), "     ",
                                                      i.GetFlightPrice(), "     ", i.GetFlightType(), "     ",
                                                      i.GetFlightDate())
                                            else:
                                                pass
                                        print()
                                        print("Enter the Flight Number to create a booking")
                                        fn = input()
                                        for i in FlightDetails.list_of_flights:
                                            if (i.GetFlightSource() == s) and (i.GetFlightDestination() == d) and (
                                                    i.GetFlightNumber() == fn) and (i.GetFlightDate() == da):
                                                FlightDetails.BookFlight(fn, da, s, d)
                                            else:
                                                pass
                                        sel_flight = FlightDetails.list_of_flight_bookings[-1]
                                        for j in FlightDetails.list_of_flight_bookings[-1]:
                                            print("Selected Flight Number:", sel_flight)
                                            print("Want to continue with current selection,  (Y/N)")
                                            con = input()
                                            if con == 'Y' or con == 'y':
                                                FlightDetails.ConfirmedBooking(
                                                    FlightDetails.list_of_flight_bookings)
                                                print("Booking Confirmed")
                                                break
                                            else:
                                                FlightDetails.ModifyBookFlight(
                                                    FlightDetails.list_of_flight_bookings)
                                                print("Removed Current Selection")
                                                print("Make new selection")
                                                break

                                elif n == 2:
                                    cyn = input("Do you have a coupon code(Y/N)")
                                    if cyn == 'Y' or cyn == 'y':
                                        cou = input("Enter the coupon code")
                                        if cou in AdministrationDetails.list_of_coupons:
                                            print("Coupon Applied...Cashback will be credited post travel")
                                            s=input("Enter the Source:")
                                            d=input("Enter the Destination:")
                                            da=input("Enter the Date of Journey:")
                                            print()
                                            print("NUMBER", "        ", "NAME", "            ", "PRICE", "     ", "TYPE")
                                            print()
                                            for i in TrainDetails.list_of_trains:
                                                if (i.GetTrainSource() == s) and (i.GetTrainDestination() == d) and (i.GetTrainDate() == da):
                                                    print(i.GetTrainNumber(), "     ", i.GetTrainName(), "     ", i.GetTrainPrice(), "     ",i.GetTrainType(),"     ",i.GetTrainDate())
                                                else:
                                                    pass
                                            print()
                                            print("Enter the Train Nummber to create a booking")
                                            fn=input()
                                            for i in TrainDetails.list_of_trains:
                                                if (i.GetTrainSource() == s) and (i.GetTrainDestination() == d) and (i.GetTrainNumber()==fn) and (i.GetTrainDate() == da):
                                                    TrainDetails.BookTrain(fn,da,s,d)
                                                else:
                                                    pass
                                            sel_train=TrainDetails.list_of_train_bookings[-1]
                                            for j in TrainDetails.list_of_train_bookings[-1]:
                                                print("Selected Train Number:",sel_train)
                                                print("Want to continue with current selection,  (Y/N)")
                                                con=input()
                                                if con=='Y' or con=='y':
                                                    TrainDetails.ConfirmedBooking(TrainDetails.list_of_train_bookings)
                                                    print("Booking Confirmed")
                                                    break
                                                else:
                                                    TrainDetails.ModifyBookTrain(TrainDetails.list_of_train_bookings)
                                                    print("Removed Current Selection")
                                                    print("Make new selection")
                                                    break
                                            else:
                                                print("Invalid Coupon")
                                                break
                                        else:
                                            s = input("Enter the Source:")
                                            d = input("Enter the Destination:")
                                            da = input("Enter the Date of Journey:")
                                            print()
                                            print("NUMBER", "        ", "NAME", "            ", "PRICE", "     ",
                                                  "TYPE")
                                            print()
                                            for i in TrainDetails.list_of_trains:
                                                if (i.GetTrainSource() == s) and (i.GetTrainDestination() == d) and (
                                                        i.GetTrainDate() == da):
                                                    print(i.GetTrainNumber(), "     ", i.GetTrainName(), "     ",
                                                          i.GetTrainPrice(), "     ", i.GetTrainType(), "     ",
                                                          i.GetTrainDate())
                                                else:
                                                    pass
                                            print()
                                            print("Enter the Train Nummber to create a booking")
                                            fn = input()
                                            for i in TrainDetails.list_of_trains:
                                                if (i.GetTrainSource() == s) and (i.GetTrainDestination() == d) and (
                                                        i.GetTrainNumber() == fn) and (i.GetTrainDate() == da):
                                                    TrainDetails.BookTrain(fn, da, s, d)
                                                else:
                                                    pass
                                            sel_train = TrainDetails.list_of_train_bookings[-1]
                                            for j in TrainDetails.list_of_train_bookings[-1]:
                                                print("Selected Train Number:", sel_train)
                                                print("Want to continue with current selection,  (Y/N)")
                                                con = input()
                                                if con == 'Y' or con == 'y':
                                                    TrainDetails.ConfirmedBooking(TrainDetails.list_of_train_bookings)
                                                    print("Booking Confirmed")
                                                    break
                                                else:
                                                    TrainDetails.ModifyBookTrain(TrainDetails.list_of_train_bookings)
                                                    print("Removed Current Selection")
                                                    print("Make new selection")
                                                    break

                                elif n == 3:
                                    cyn = input("Do you have a coupon code(Y/N)")
                                    if cyn == 'Y' or cyn == 'y':
                                        cou = input("Enter the coupon code")
                                        if cou in AdministrationDetails.list_of_coupons:
                                            print("Coupon Applied...Cashback will be credited post travel")
                                            s=input("Enter the Source:")
                                            d=input("Enter the Destination:")
                                            da = input("Enter the Date of Journey:")
                                            print()
                                            print("    NAME", "            ", "PRICE", "     ", "TYPE")
                                            print()
                                            for i in BusDetails.list_of_buses:
                                                if (i.GetBusSource() == s) and (i.GetBusDestination() == d) and (i.GetBusDate() == da):
                                                    print(i.GetBusName(), "     ", i.GetBusPrice(), "     ",i.GetBusType(),"       ",(i.GetBusDate()))
                                                else:
                                                    pass
                                            print()
                                            print("Enter the Bus to create a booking")
                                            fn=input()
                                            for i in BusDetails.list_of_buses:
                                                if (i.GetBusSource() == s) and (i.GetBusDestination() == d) and (i.GetBusName()==fn) and (i.GetBusDate()==da):
                                                    BusDetails.BookBus(fn,da,s,d)
                                                else:
                                                    pass
                                            sel_bus=BusDetails.list_of_bus_bookings[-1]
                                            for j in BusDetails.list_of_bus_bookings[-1]:
                                                print("Selected Bus Name:",sel_bus)
                                                print("Want to continue with current selection,  (Y/N)")
                                                con=input()
                                                if con=='Y' or con=='y':
                                                    BusDetails.ConfirmedBooking(BusDetails.list_of_bus_bookings)
                                                    print("Booking Confirmed")
                                                    break
                                                else:
                                                    BusDetails.ModifyBookBus(BusDetails.list_of_bus_bookings)
                                                    print("Removed Current Selection")
                                                    print("Make new selection")
                                                    break
                                        else:
                                            print("Invalid Coupon")
                                            break
                                    else:
                                        s = input("Enter the Source:")
                                        d = input("Enter the Destination:")
                                        da = input("Enter the Date of Journey:")
                                        print()
                                        print("    NAME", "            ", "PRICE", "     ", "TYPE")
                                        print()
                                        for i in BusDetails.list_of_buses:
                                            if (i.GetBusSource() == s) and (i.GetBusDestination() == d) and (
                                                    i.GetBusDate() == da):
                                                print(i.GetBusName(), "     ", i.GetBusPrice(), "     ", i.GetBusType(),
                                                      "       ", (i.GetBusDate()))
                                            else:
                                                pass
                                        print()
                                        print("Enter the Bus to create a booking")
                                        fn = input()
                                        for i in BusDetails.list_of_buses:
                                            if (i.GetBusSource() == s) and (i.GetBusDestination() == d) and (
                                                    i.GetBusName() == fn) and (i.GetBusDate() == da):
                                                BusDetails.BookBus(fn, da, s, d)
                                            else:
                                                pass
                                        sel_bus = BusDetails.list_of_bus_bookings[-1]
                                        for j in BusDetails.list_of_bus_bookings[-1]:
                                            print("Selected Bus Name:", sel_bus)
                                            print("Want to continue with current selection,  (Y/N)")
                                            con = input()
                                            if con == 'Y' or con == 'y':
                                                BusDetails.ConfirmedBooking(BusDetails.list_of_bus_bookings)
                                                print("Booking Confirmed")
                                                break
                                            else:
                                                BusDetails.ModifyBookBus(BusDetails.list_of_bus_bookings)
                                                print("Removed Current Selection")
                                                print("Make new selection")
                                                break
                                elif n==4:
                                    break

                                else:
                                    sys.exit()



                            elif num == 3:
                                print()
                                print("1. View Current Bookings:")
                                print("2. Cancel Booking:")
                                print("3. Go back to previous menu")
                                print("Press any other key to Log Out")
                                print()
                                n = int(input())
                                print()
                                if n == 1:
                                    print("Current Bookings Are:")
                                    print("Confirmed Flight Bookings are:")
                                    for i in FlightDetails.list_of_flight_confirmed_bookings:
                                        print(FlightDetails.list_of_flight_confirmed_bookings)
                                        break
                                    print("Confirmed Train Bookings are:")
                                    for j in TrainDetails.list_of_train_confirmed_bookings:
                                        print(TrainDetails.list_of_train_confirmed_bookings)
                                        break
                                    print("Confirmed Bus Bookings are:")
                                    for k in BusDetails.list_of_bus_confirmed_bookings:
                                        print(BusDetails.list_of_bus_confirmed_bookings)
                                        break

                                elif n == 2:
                                    while True:
                                        print("Enter the type of booking to cancel:")
                                        print("1. Airline:")
                                        print("2. Train:")
                                        print("3. Bus:")
                                        print("4. Go to previous page")
                                        print("Press Any other key to Log Out")
                                        print()
                                        n = int(input())
                                        print()
                                        if n==1:
                                            print("You will be charged a minimum of 400 cancellation charge")
                                            ch=input("Do you wish to continue (Y/N)")
                                            if ch=='Y' or ch=='y':
                                                print("Enter the Flight Number to cancel:")
                                                fn = input()
                                                FlightDetails.list_of_flight_confirmed_bookings.pop(0)
                                                print("Flight Cancelled")
                                                for i in FlightDetails.list_of_flights:
                                                    if i.GetFlightNumber()==fn:
                                                        now = str(datetime.now())
                                                        curr_date = now[8:10] + "/" + now[5:7] + "/" + now[2:4]
                                                        a = datetime.strptime(curr_date, "%d/%m/%y")
                                                        b = datetime.strptime(i.GetFlightDate(), "%d/%m/%y")
                                                        if a<b:
                                                            print("Refunded Amount:",i.GetFlightPrice()-400)
                                                            break
                                                        elif a==b:
                                                            print("Refunded Amount:0")
                                                        else:
                                                            break
                                                    else:
                                                        pass

                                                break
                                            else:
                                                print("Exiting...Press any key to continue")
                                                input()

                                        elif n==2:
                                            print("You will be charged a minimum of 80 cancellation charge")
                                            ch = input("Do you wish to continue (Y/N)")
                                            if ch == 'Y' or ch == 'y':
                                                print("Enter the Train Number to cancel:")
                                                fn = input()
                                                TrainDetails.list_of_train_confirmed_bookings.pop(0)
                                                print("Train Cancelled")
                                                for i in TrainDetails.list_of_trains:
                                                    if i.GetTrainNumber() == fn:
                                                        now = str(datetime.now())
                                                        curr_date = now[8:10] + "/" + now[5:7] + "/" + now[2:4]
                                                        a = datetime.strptime(curr_date, "%d/%m/%y")
                                                        b = datetime.strptime(i.GetTrainDate(), "%d/%m/%y")
                                                        if a < b:
                                                            print("Refunded Amount:", i.GetTrainPrice() - 400)
                                                            break
                                                        elif a == b:
                                                            print("Refunded Amount:0")
                                                        else:
                                                            break
                                                    else:
                                                        pass

                                                break
                                            else:
                                                print("Exiting...Press any key to continue")
                                                input()

                                        elif n==3:
                                            print("You will be charged a minimum of 400 cancellation charge")
                                            ch = input("Do you wish to continue (Y/N)")
                                            if ch == 'Y' or ch == 'y':
                                                print("Enter the Bus Name to cancel:")
                                                fn = input()
                                                BusDetails.list_of_bus_confirmed_bookings.pop(0)
                                                print("Bus Cancelled")
                                                for i in BusDetails.list_of_buses:
                                                    if i.GetBusName() == fn:
                                                        now = str(datetime.now())
                                                        curr_date = now[8:10] + "/" + now[5:7] + "/" + now[2:4]
                                                        a = datetime.strptime(curr_date, "%d/%m/%y")
                                                        b = datetime.strptime(i.GetBusDate(), "%d/%m/%y")
                                                        if a < b:
                                                            print("Refunded Amount:", i.GetBusPrice() - 400)
                                                            break
                                                        elif a == b:
                                                            print("Refunded Amount:0")
                                                        else:
                                                            break
                                                    else:
                                                        pass

                                                break
                                            else:
                                                print("Exiting...Press any key to continue")
                                                input()

                                        elif n==4:
                                            break

                                        else:
                                            sys.exit()

                                elif n == 3:
                                    break

                                else:
                                    sys.exit()

                            elif num==4:
                                print("Confirmed Flight Bookings are:")
                                for i in FlightDetails.list_of_flight_confirmed_bookings:
                                    print(FlightDetails.list_of_flight_confirmed_bookings)
                                    break
                                print("Confirmed Train Bookings are:")
                                for j in TrainDetails.list_of_train_confirmed_bookings:
                                    print(TrainDetails.list_of_train_confirmed_bookings)
                                    break
                                print("Confirmed Bus Bookings are:")
                                for k in BusDetails.list_of_bus_confirmed_bookings:
                                    print(BusDetails.list_of_bus_confirmed_bookings)
                                    break
                                break


                            else:
                                sys.exit()


            print("Invalid Details")
            print("Total Incorrect Attempts:", c)
            print(3-c,"more attempts left")
            c = c + 1


        print("Exiting.....Press Any Key to continue")
        input()
        sys.exit()

    else:
        print("Wrong Input.....Press Any Key to exit")
        input()
        sys.exit()
