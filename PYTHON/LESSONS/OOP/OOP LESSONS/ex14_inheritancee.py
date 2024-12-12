# Inheritance route 2
# Using the super() function to inherit while creating

# 1. When creating a child class, pass the Superclass in as a parameter 2. Add old and new properties 3. Add new methods

# super() allows us to inherit all the properties and methods from the superclass(parent class)


class Main:
    def __init__(self, name, age, location):
        self.name = name 
        self.age = age
        self.location = location
        
        
    def user_info(self):
        print("Welcome,", self.name)
        print("You are,", self.age)
        print("You live in,", self.location)



class User_Score(Main):
    def __init__(self, name, age, location, score):
        super().__init__(name, age, location) #initialize properties from superclass 
        self.score = int(score)
        
    
    def check_Avg(self, list1):
        x = self.score/len(list1)*100
        print("Results: ", x)   
            
            
list1 = [10, 23, 45, 13, 56]
user = User_Score("Sena", 200, "Accra", 5)
user.check_Avg(list1)



    
    
    
    
    
