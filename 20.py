Prefer = ["cinema","theater"]

Ticket = input("If you want to go to the cinema, write 'cinema' but if you want to go to the theater, write 'theater' :").lower()
if(Ticket == Prefer[0]):
    CinemaTicket = 15
    Person = input("Are you a student? Yes or No:")
    if(Person=="Yes"):
        print("Student cinema ticket : {0} Turkish Lira".format(float(CinemaTicket/2)))
    elif(Person=="No"):
        print("Cinema Ticket : {0} Turkish Lira".format(CinemaTicket))
    else:
        print("invalid value")
elif(Ticket == Prefer[1]):
    TheatreTicket = 10
    Person = input("Are you a student? Yes or No:")
    if(Person=="Yes"):
        print("Student theatre ticket : {0} Turkish Lira".format(float(TheatreTicket/2)))
    elif(Person=="No"):
        print("Theatre Ticket : {0} Turkish Lira".format(TheatreTicket))
    else:
        print("invalid value")
else:
    print("invalid value")
