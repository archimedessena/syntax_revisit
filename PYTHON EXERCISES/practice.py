# flashcard implementation

class FlashCard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning 
        
    def __str__(self):
         return self.word+' ( '+self.meaning+' )'
     
    
word = []  
while True:
    entry = input("Enter word: ")
    mean = input("Enter meaning of word: ")
    word.append(FlashCard(entry, mean))
    
    option = int(input("Enter 0 if you want to halt the program for result:"))
    if option:
        break
    

for i in word:
    print(i)