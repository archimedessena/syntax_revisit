# Title: Guest Management and Loyalty Program 


# Description:
#This code represents a guest management system with a loyalty program. It allows you to input information about guest, such as their  names, ranks, and ages. The system provides various functionalities to retrieve guest information, track loyalty points, and calculate average guest age. 
### 

# lets understand how the code works

# 1. Creating  Guest Objects:The code starts by creating guest objects. Each guest has a last name, first name, rank, and age. The rank and age are converted to integer for calculations.

# 2. Guest Information: The "guest_info(all_guests)" method displays information about all guests. It takes a list of all guests as input and loops through each guest, printing their their first name, last name, and age. This provides an overview of all the guests.

#3. Loyalty Points: The "loyalty_po(all_guests)" method identifies the guests who qualify as gold members based on their ranks. It loops through all guests and checks if their rank is greater  than or equal to 10. if so, it prints their last name, indicating that they are gold members


class Guest: 
    def __init__(self, last, first, rank, age):
        self.last = last
        self.first = first
        self.rank = rank
        self.age = age



























