#please Select Hotel Mumbai Hotel A
def hotela():
    dno=3
    maxr=5
    maxp=3
    selectednroom=0
    maxperson=0
    print("Welcome to Hotel A")
    print("*****************")
    print("How many rooms do you need ?")
    userselecroom=int(input("Type Here: "))
    if userselecroom <= 5 :
        print("You have entered",userselecroom,"Rooms")
        print("How many persons will be in one room ?")
        userselecno=int(input("Type Here: "))
        if userselecno <= 3 :
            print("You have entered",userselecno,"persons")
            print("Do you have any children with you ?")
            child=input("yes/no: ")
            if child=="yes":
                print("Enter the age of children")
                age=int(input("Type Here: "))
                if age<=12:
                    print("Sorry children below age 12 are not allowed")
                else:
                    print("select type of Room")
                    print("1.With View")
                    print("2.Without View")
                    typeofroom=int(input("Type here:"))
                    if typeofroom ==1:
                        print("select type of View")
                        print("1.Mountain View | Cost:Rs 15000")
                        print("2.Pool View | Cost:Rs 10000")
                        viewselec=int(input("Type Here"))
                        if viewselec ==1:
                            print("Please enter your Info for booking")
                            name=input("Your Name:")
                            address=input("Your Address")
                            cost="Rs 15000"
                            print("Booking Sucessfull")
                            print("Bill info")
                            print(name)
                            print(address)
                            print("Total Cost:",cost)
                        
                        if viewselec ==2:
                            print("Please enter your Info for booking")
                            name=input("Your Name:")
                            address=input("Your Address")
                            cost="Rs 10000"
                            print("Booking Sucessfull")
                            print("Bill info")
                            print(name)
                            print(address)
                            print("Total Cost:",cost)    
                         
                         
                    elif typeofroom ==2:    
                            print("1.Normal Room | Cost:Rs 2000")
                            if viewselec ==1:
                                print("Please enter your Info for booking")
                                name=input("Your Name:")
                                address=input("Your Address")
                                cost="Rs 2000"
                                print("Booking Sucessfull")
                                print("Bill info")
                                print(name)
                                print(address)
                                print("Total Cost:",cost)
                                print("2.AC Deluxe room | Cost:Rs 5000")
                            elif viewselec ==2:
                                print("Please enter your Info for booking")
                                name=input("Your Name:")
                                address=input("Your Address")
                                cost="Rs 2000"
                                print("Booking Sucessfull")
                                print("Bill info")
                                print(name)
                                print(address)
                                print("Total Cost:",cost)
                    else:
                        print("Sorry this type of room is not available")    
                    
                    
            else:
                print("select type of Room")
                print("1.With View")
                print("2.Without View")
                typeofroom=input("Type here:")
                if typeofroom ==1:
                        print("select type of View")
                        print("1.Mountain View | Cost:Rs 15000")
                        print("2.Pool View | Cost:Rs 10000")
                        if viewselec ==1:
                            print("Please enter your Info for booking")
                            name=input("Your Name:")
                            address=input("Your Address")
                            cost="Rs 15000"
                            print("Booking Sucessfull")
                            print("Bill info")
                            print(name)
                            print(address)
                            print("Total Cost:",cost)
                        elif viewselec ==2:
                            print("Please enter your Info for booking")
                            name=input("Your Name:")
                            address=input("Your Address")
                            cost="Rs 10000"
                            print("Booking Sucessfull")
                            print("Bill info")
                            print(name)
                            print(address)
                            print("Total Cost:",cost)    
                elif typeofroom ==2:    
                        print("1.Normal Room | Cost:Rs 2000")
                        if viewselec ==1:
                                print("Please enter your Info for booking")
                                name=input("Your Name:")
                                address=input("Your Address")
                                cost="Rs 2000"
                                print("Booking Sucessfull")
                                print("Bill info")
                                print(name)
                                print(address)
                                print("Total Cost:",cost)
                        
                        print("2.AC Deluxe room | Cost:Rs 5000")
                else:
                    print("Sorry this type of room is not available") 
        else:
            print("Sorry this hotel doesnot allow more than 3 persons")
    else:
        print("Sorry this hotel doesnot allow more than 5 room to a person")
    
    
    
    
          
    
    
    

    
def mumbai():
    print("Selected location: MUMBAI")
    print("*************************************")
    print("List of Hotels")
    print("1:Hotel A")
    print("2:Hotel B")
    print("*************************************")
    print("Select your Desired Hotel")
    mumbaihotel=input("Type Here")
    if mumbaihotel=="1":
        hotela()
    elif mumbaihotel=="2":
        hotela()
    else:
        print("You have selected wrong locations")

def shimla():
    print("Selected location: Shimla")
    print("*************************************")
    print("List of Hotels")
    print("1:Hotel C")
    print("2:Hotel D")
    print("*************************************")
    shimlahotel=input("Select your Desired Hotel")
    if shimlahotel=="1":
        hotela()
    elif shimlahotel=="2":
        hotela()
    else:
        print("You have selected wrong locations")
    
locations=["MUMBAI","SHIMLA","PATNA","LUCKNOW"]
print("*************************************")
print("***Welcome To Hotel Booking system***")
print("*************************************")
print("Please select the your Destination")
print("1:MUMBAI")
print("2:SHIMLA")
print("*************************************")
userloc=input("Type here: ")
print("*************************************")
if userloc=="1":
    mumbai()
elif userloc=="2":
    shimla()
else:
    print("You have selected wrong locations")





