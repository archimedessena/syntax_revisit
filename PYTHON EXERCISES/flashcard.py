#In this article, we will see how to build a flashcard using class in python. A flashcard is a card having information on both sides, which can be used as an aid in memorization. Flashcards usually have a question on one side and an answer on the other. Particularly in this article, we are going to create flashcards that will be having a word and its meaning.

#Approach

#Take the word and its meaning as input from the user. 
# Create a class named flashcard, use the __init__() function to assign values for Word and Meaning. 
# Now we use the __str__() function to return a string that contains the word and meaning.
# Store the returned strings in a list named flash.
# Use a while loop to print all the stored flashcards.


class FlashCard:
    
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
        
    def __str__(self):
        return self.word+' ( '+self.meaning+' )'
    


flash = []

while True:
    words = input("Enter a word: ").lower()
    meaning = input("Enter a meaning of the word: ").lower()
    
    
    flash.append(FlashCard( words, meaning ))
    option = int(input("enter 0 , if you want to add another flashcard or 1 if you want print out: "))
    
    if(option):
        break

print("\nYour flashcards")
for i in flash:
    print(">", i)