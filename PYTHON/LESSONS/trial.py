def name_guess():
    name = input("What is my name?:")
    name1 = "Archimedes"
    if name == name1: 
        print("That is my name,", name )
    else: 
        print("My name is {} not {}".format(name1, name))
        
        
name_guess()