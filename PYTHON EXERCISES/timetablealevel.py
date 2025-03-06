import random

def generate_exam_timetable(subjects):
    random.shuffle(subjects)  # Shuffle subjects for randomness
    timetable = []
    
    for i in range(0, len(subjects), 2):
        morning = subjects[i]
        afternoon = subjects[i+1] if i+1 < len(subjects) else None
        timetable.append((morning, afternoon)) 
    return timetable

subjects = ["Biology", "Physics", "Chemistry", "Extended Maths", "First Language", "French", "Literature", "Physical Education", "ICT", "Core Maths", "Business", "Economics", "Arts and Design", "Drama", "Geography","Spanish", "Sociology", "History"]

timetable = generate_exam_timetable(subjects)

print("Exam Timetable:")
for day, (morning, afternoon) in enumerate(timetable, start=1):
    print(f"Day {day}: Morning - {morning}, Afternoon - {afternoon if afternoon else 'No Exam'}")

