import random

def generate_exam_timetable(subjects):
    random.shuffle(subjects)  # Shuffle subjects for randomness
    timetable = []
    
    for i in range(0, len(subjects), 2):
        morning = subjects[i]
        afternoon = subjects[i+1] if i+1 < len(subjects) else None
        timetable.append((morning, afternoon))
    
    return timetable

subjects = ["Biology", "Physics", "Chemistry", "Extended Maths", "First Language", "French", "Literature", "Physical Education", "ICT", "Core Maths", "Business", "Economics", "Arts and Design", "Drama", "Geography","Spanish", "Sociology", "History"] #[
    #"Accounting 1", "Accounting 2", "Add Math 1", "Add Math 2", "Arts and Design 1", "Arts and Design 2",
   # "Biology 2", "Biology 4", "Biology 6", "Business Studies 1", "Business Studies 2",
   # "Chemistry 2", "Chemistry 4", "Chemistry 6", "Economics 1", "Economics 2", "English 1", "English 2",
    #"French 1", "French 2", "French 4", "Geography 1", "Geography 2", "Geography 4", "History 1",
    #"History 2", "History 4", "ICT 1", "ICT 2", "ICT 3", "Literature 1", "Literature 3", "Literature 4",
    #"Core Math 1", "Core Math 3", "Extended Math 2", "Extended Math 4"


timetable = generate_exam_timetable(subjects)

print("Exam Timetable:")
for day, (morning, afternoon) in enumerate(timetable, start=1):
    print(f"Day {day}: Morning - {morning}, Afternoon - {afternoon if afternoon else 'No Exam'}")
