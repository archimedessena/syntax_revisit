import random

def generate_exam_timetable(subjects):
    random.shuffle(subjects)  # Shuffle subjects for randomness
    timetable = []
    
    for i in range(0, len(subjects), 2):
        morning = subjects[i]
        afternoon = subjects[i+1] if i+1 < len(subjects) else None
        timetable.append((morning, afternoon))
    
    return timetable

subjects = [
    "IT 1", "IT 2", "IT 3", "IT 4", "Geography 1", "Geography 2", "Geography 3", "Geography 4", "Physics 1", "Physics 2", "Physics 3", "Physics 4", "Physics 5", "Chemistry 1", "Chemistry 2", "Chemistry 3", "Chemistry 4", "Chemistry 5"
]

timetable = generate_exam_timetable(subjects)

print("Exam Timetable:")
for day, (morning, afternoon) in enumerate(timetable, start=1):
    print(f"Day {day}: Morning - {morning}, Afternoon - {afternoon if afternoon else 'No Exam'}")
