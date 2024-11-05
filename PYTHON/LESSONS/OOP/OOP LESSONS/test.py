class App():
    def __init__(self,  users, storages, username):
        self.username = username
        self.users = users
        self.storages = storages
        
    
    def login(self):
        if self.username == "sena" and self.users >=1:
            print("Hi,", self.username)
        else:
            print("Login denied.")
            
        
    def increase_capacity(self, number):
        self.storages += number
        print(self.storages)
    
    
    
    
                        
sena = App(500, 99, "owner")
sena.login()
sena.increase_capacity(180)

#sena = App(800, 899, "user")
#sena.login()

            
            
        
        
        
        