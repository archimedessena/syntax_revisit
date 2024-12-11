# Title: Guest Management and Loyalty Program 


# Description:
#This code represents a guest management system with a loyalty program. It allows you to input information about guest, such as their  names, ranks, and ages. The system provides various functionalities to retrieve guest information, track loyalty points, and calculate average guest age. 
### 

# lets understand how the code works

# 1. Creating  Guest Objects:The code starts by creating guest objects. Each guest has a last name, first name, rank, and age. The rank and age are converted to integer for calculations.

# 2. Guest Information: The "guest_info(all_guests)" method displays information about all guests. It takes a list of all guests as input and loops through each guest, printing their their first name, last name, and age. This provides an overview of all the guests.

#3. Loyalty Points: The "loyalty_points(all_guests)" method identifies the guests who qualify as gold members based on their ranks. It loops through all guests and checks if their rank is greater  than or equal to 10. if so, it prints their last name, indicating that they are gold members


class Guest: 
    def __init__(self, first, last, rank, age):
        self.last_name = last
        self.first_name = first
        self.rank = int(rank)
        self.age = int(age)

    def guest_info(self, all_guests):
        for guest in all_guests:
            print(guest.first_name, guest.last_name, "Age:",  guest.age)
            
    def loyalty_program(self, all_guests):
        #1. create a list of any guest who meets certain conditions 
        #2.  for every guest in my list, add their last name to the list 
        #3. This condition must be met in order to be added to the list 
        gold_members = [guest.last_name for guest in all_guests if guest.rank >= 10]
        if gold_members:
            print ("Gold members")
            for member in gold_members:
                print("\tGuest", member)
                
    def guest_avg(self, all_guests):
        total_age = 0 
        for guest in all_guests:
            total_age += guest.age 
        avg_age = total_age / len(all_guests)
        print("Average customer age: ", avg_age)
        
        
        

all_guests = list()
num_guests = int(input("Enter a number of guests: "))        
for i in range(num_guests):
    data = input("First Name/Last Name/Rank/Age: ").split("/")       
    guest = Guest(data[0], data[1], int(data[2]), int(data[3])) 
    all_guests.append(guest)
        
        
guest = all_guests[0]
guest.loyalty_program(all_guests)
guest.guest_info(all_guests)
guest.guest_avg(all_guests)       
        
  