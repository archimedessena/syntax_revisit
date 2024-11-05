# OOP for an app 
class App():
    def __init__(self, users, storage, username):
        self.users = users
        self.storage = storage
        self.username = username 
        
    
    def login(self):
        if self.username == "owner" and self.users >= 1:
            print("Welcome,", self.username)
            print("Your storage is:", self.storage)
        else:
            print("Login is denied.")
        

    def increase_capacity(self, number):
        self.storage += number  
        print("Updated storage is", self.storage)
        
                
                        
sena = App(500, 99, "owner")
sena.login()
sena.increase_capacity(80)

#sena = App(800, 899, "user")
#sena.login()


