#Approach :

#Create a class named flashcard.
#Initialize dictionary fruits using __init__() method.
#Now randomly choose a pair from fruits using choice() method and store the key in variable fruit and value in variable color.
#Now prompt the user to answer the color of the randomly chosen fruit.
#If correct print correct else print wrong.



import random

class flashcard:
    def __init__(self):
      
        self.fruits={'apple':'red',
                     'orange':'orange',
                     'watermelon':'green',
                     'banana':'yellow'}
        
    def quiz(self):
        while (True):
          
            fruit, color = random.choice(list(self.fruits.items()))
            
            print("What is the color of {}".format(fruit))
            user_answer = input()
            
            if(user_answer.lower() == color):
                print("Correct answer")
            else:
                print("Wrong answer")
                
            option = int(input("enter 0 , if you want to play again : "))
            if (option):
                break

print("welcome to fruit quiz ")
fc=flashcard()
fc.quiz()