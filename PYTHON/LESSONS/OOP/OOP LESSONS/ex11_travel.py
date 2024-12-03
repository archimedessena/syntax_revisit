# Travel Planner and cost calculator 

# Description: The provided code represents  a travel planning and cost calculator system. It allows you to input the country you want to travel to, the month of travel, and the type of trip (leisure or business). The system provides information about the trip and calculates the total cost based on flight expenses and additional costs.

#Lets understand the how the code works.
# 1. Travel planning: When you create a new instance of the "Travel" class, you provide the country you want to visit, the month of travel, and the type of trip (leisure or business). The system stores this information.

# 2. Trip Information: The "trip_info()" method provides information about your trip based on the month of travel. if the month falls between October and March, it considers it as a winter trip and displays a message stating the country and trip type (leisure or business). If the month is between April and September, it considers it as a summer trip and displays a similar message. If an invalid month is entered, it displays an error message

#3. Cost Calculation: The "calc_cost(cost)" method calculates the cost the total cost of the trip. It takes the flight cost as input and prompts you to enter any additional cost. The system keeps adding the cost and updates the total price accordingly. It also provides advice based on the total cost, categorizing it as "low budget" for costs below 500, "Enjoy a flight to anywhere" for costs between 500 and 1500, and "Luxury trip" for costs exceeding 1500


class Travel:
    def __init__(self, country, month, type):
        self.country = country
        self.type = type
        self.month = month
        self.price = 0
        
    
    def trip_info(self):
        if self.month >= 10 and self.month <= 3:
            print(f"You are going to {self.country} in the winter! This is a {self.type} trip")
        elif self.month > 3 and self.month < 10:
             print(f"You are going to {self.country} in the summer! This is a {self.type} trip")
        else:
            print("Invalid Input")
    
    
    def calc_cost(self, cost):
        costs = []
        while cost != 0:
            self.price += cost
            costs.append(cost)
            cost = int(input("Enter another cost:"))
        
        advice = self.advice(self.price)
        inspect = self.list_inspect(costs)
        return advice, inspect 
            
    def advice(self, number):
        if number < 500:
            print("You have low budget")
        elif number >= 500 and number < 1500:
            print("Take a flight to anywhere.")
        else:
            print("Luxury trip.")

    def list_inspect(self, costs):
        less_than_ten = 0 
        for i in costs:
            if i >= 10:
                less_than_ten += 1
                
        if less_than_ten <= 10:
            self.price += 100
            print(f"Updated price: {self.price}")


location = input("Enter a country: ").capitalize()
trip_type = input("Leisure or Business: ").capitalize()
month = input("Enter a month: ") 


test = Travel(location, month, trip_type)


test.trip_info()

flight_cost = int(input("Enter a flight cost:"))
test.calc_cost(flight_cost)



































iiiii