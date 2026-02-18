# Modelling education 

class Education:
    
    def __init__(self, curriculum, training, exams, teachers, students, training_materials):
        self.training = training
        self.curriculum = curriculum
        self.exams = exams  
        self.teachers = teachers
        self.students = students
        self.training_materials = training_materials      
        
        
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


  

        
        
        