#Practice on Inheritance Using Animal as example

class Animal: # Parent class
    def __init__(self, region, animal_type, color, lethal):
        self.region = region
        self.animal_type = animal_type
        self.color = color
        self.lethal = lethal
        
    def animal_bio(self):
        print("Animal Passport:") 
        print(f"Found in: {self.region}")
        print(f"Species: {self.animal_type}")
        print(f"Color: {self.color}")
        print(f"Dangerous: {self.lethal}")
 
        
#Inheritance
class Clinic(Animal): # Child class
    def animal_info(self):
        print(f"This is a {self.animal_type} from {self.region}")
        
    def search(self, animals):
        region = input("Enter a region: ").lower()
        for animal in animals:
            if animal.region == region:
                print(f"Species: {self.animal_type}")
                

animals = []
num_animals = int(input("Enter number of animals: "))
for i in range(num_animals):
    region = input("Enter a region: ").lower()
    species = input("Enter a species: ").lower()
    color = input("Enter a color: ").lower()
    lethal = input("Is it dangerous: ").lower()
    lethal = lethal == "yes"
    
    
    animal = Animal(region, species, color, lethal)
    
    animals.append(animal)
    

clinic = Clinic("asia", "tiger", "orange", True)   

clinic.animal_bio()
clinic.animal_info()
clinic.search(animals)
