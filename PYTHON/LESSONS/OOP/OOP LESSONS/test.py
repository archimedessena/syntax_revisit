class App():
    def __init__(self, users, username, storages):
        self.users = users
        self.username = username
        self.storages = storages
        
    
    def login(self):
        if self.username == "Archimedes" and self.users <= 10:
            print("Access granted.")
            print("Greetings,", self.username)
            
        elif self.username == "Sena" and self.users <= 10:
            print("Access granted.")
            print("Greetings,", self.username)
        
        else:
            print("Access denied.")
           
    
 
    def increase_capacity(self, number):
        if self.storages >= 1500 and number >= 1500:
            self.storages += number
            print(self.storages, "is out of range")
            
        elif self.storages >= 1500 and number <= 1500:
            self.storages += number
            print("Your updated storage is:", self.storages)
        
        else:
            print("You have not added enough storage.")
            
        
    #def check_upgrade(self):
    #    if self.users >= self.storages:
    #        upgrade_amt = int(input("Please enter upgrade_amount: "))
    #        self.storages += upgrade_amt
    #    
    #    else:
    #        print("You will still have:", str(self.storages - self.users), "spaces open!")
            
            
t = App(10, "Sena", 1500)   

t.login()    
t.increase_capacity(1400)    
#t.check_upgrade()   
        