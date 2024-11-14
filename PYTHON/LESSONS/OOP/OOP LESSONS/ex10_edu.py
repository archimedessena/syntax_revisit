# Modelling education 

class Education:
    
    def __init__(self, curriculum, training, exams):
        self.training = training
        self.curriculum = curriculum
        self.exams = exams        
        
        
    def institution(self):
        if self.curriculum == "Cambridge":
            print("The school fees is high")
        elif self.curriculum == "GES":
            print("The school fees is low")
        else:
            print("That is a mushroom school")
        
    def exam(self):
        Education.institution()
        if self.curriculum:
            print("The exam is every easy and the kids are pampered") 
            
        else:
            print("Not pampered")



        
        
        