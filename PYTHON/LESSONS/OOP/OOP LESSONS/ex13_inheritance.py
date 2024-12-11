# Iheritance route 1
# Inheriting everything from a superclass(parent class
# creating a child class that only needs new methods not properties
# When we make an instance of a child class, the superclass constructor(__init__) will be callledd and used in the child class

class Main:
    def __init__(self, name, age, location):
        self.name = name 
        self.age = age
        self.location = location
        
        
    def user_info(self):
        print("Welcome,", self.name)
        print("You are,", self.age)
        print("You live in,", self.location)
    
# Created a child class called "UserScore". This will be a class which uses the superclass properties. We inherit all the properties from our superclass, which can be  used throughout methods in our child class
class UserScore(Main):
    def calc_score(self, number):
        score = self.age * number
        return score 

    def check_age(self):
        if self.age >= 120:
            return "Grandfather"
        elif self.age <= 40:
            return "My co-equal"
        else:
            return "Minor"





