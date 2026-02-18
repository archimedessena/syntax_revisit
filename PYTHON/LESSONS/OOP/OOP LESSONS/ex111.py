class Travel:
    def __init__(self, country, month, trip_type):
        self.country = country
        self.month = month
        self.trip_type = trip_type
        self.price = 0

    def trip_info(self):
        # Check if month is a valid integer and within range
        try:
            month = int(self.month)
            if month >= 1 and month <= 12:
                if 10 <= month <= 12 or 1 <= month <= 3:
                    print(f"You are going to {self.country} in the winter! This is a {self.trip_type} trip")
                else:  # Months 4 to 9
                    print(f"You are going to {self.country} in the summer! This is a {self.trip_type} trip")
            else:
                print("Invalid month: Please enter a number between 1 and 12")
        except ValueError:
            print("Invalid Input: Month must be a number")

    def calc_cost(self, cost):
        costs = []
        self.price = cost
        costs.append(cost)
        while True:
            try:
                cost = int(input("Enter another cost (0 to stop): "))
                if cost == 0:
                    break
                self.price += cost
                costs.append(cost)
            except ValueError:
                print("Invalid Input: Please enter a valid number")

        advice = self.advice(self.price)
        inspect = self.list_inspect(costs)
        return advice, inspect

    def advice(self, number):
        if number < 500:
            return "You have a low budget."
        elif 500 <= number < 1500:
            return "Take a flight to anywhere."
        else:
            return "Luxury trip."

    def list_inspect(self, costs):
        # Count costs >= 10 (clarify if this should be < 10 based on intent)
        count = sum(1 for i in costs if i >= 10)
        if count <= 10:  # Adjust logic based on your needs
            self.price += 100
            print(f"Updated price: {self.price}")
        return count  # Return the count for inspection

# Get user input
location = input("Enter a country: ").capitalize()
trip_type = input("Leisure or Business: ").capitalize()
month = input("Enter a month (1-12): ")

# Create Travel instance
test = Travel(location, month, trip_type)

# Display trip info
test.trip_info()

# Get flight cost and calculate total
try:
    flight_cost = int(input("Enter a flight cost: "))
    advice, count = test.calc_cost(flight_cost)
    print(f"Advice: {advice}")
    print(f"Number of costs >= 10: {count}")
except ValueError:
    print("Invalid Input: Flight cost must be a number")