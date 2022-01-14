from redis_proj import agency

obj=agency()

def menu():
    print("hello welcome to my agency")

    print('''

    select :
    1-createuser
    2-showuser
    3-addtrip
    4-showtrip
    5-addtour
    6-showtour



    ''')

    option=int(input(":"))

    if option==1:
        name=input("name:")
        phone_number=input("phone_number")
        age=input("age:")
        obj.user_creator(name,phone_number,age)
        

        a=input("anykey...")
        menu()

    if option==2:
        name=input("name:")

        print(obj.show_user(name))

        a=input("anykey...")
        menu()

    if option==3:
        source=input("source:")
        destination=input("destination:")
        time=input("time(day):")
        vehicle=input("vehicle:")
        users=input("name of users seprate by ,:")

        obj.trip_creator(source,destination,time,vehicle,users)


        a=input("anykey...")
        menu()

    if option==4:
        source=input("source:")
        destination=input("destination:")
        time=input("time(day):")

        print(obj.show_trip(source,destination,time))
        a=input("anykey...")
        menu()

    if option==5:

        source=input("source:")
        destination=input("destination:")
        days=input("days:")
        price=input("price:")
        users=input("name of users seprate by ,")
        leader=input("leader:")
        details=input("details:")


        obj.tour_creator(leader,users,days,price,source,destination,details)

        a=input("anykey...")
        menu()

    if option==6:
        source=input("source:")
        destination=input("destination:")
        leader=input("leader:")


        obj.show_tour(source,destination,leader)

        a=input("anykey...")
        menu()


menu()