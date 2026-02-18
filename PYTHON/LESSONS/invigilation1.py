import random

def generate_invigilation_schedule(teachers, classes, days, subjects_per_day):
    schedule = {}
    
    for day in range(1, days + 1):
        schedule[f"Day {day}"] = []
        assigned_teachers = set()
        
        for subject in range(1, subjects_per_day + 1):
            session = {}
            random.shuffle(teachers)
            
            for class_name in classes:
                available_teachers = [t for t in teachers if t not in assigned_teachers]
                if available_teachers:
                    selected_teacher = random.choice(available_teachers)
                    assigned_teachers.add(selected_teacher)
                    session[class_name] = selected_teacher
                else:
                    session[class_name] = "No teacher available"
            
            schedule[f"Day {day}"].append(session)
    
    return schedule

teachers = [
    "Mr. Boateng", "Mr. Apedido", "Mr. Klegbe", "Mr. Gbemu", "Mr. Boakye", "Mr. Asirifie", "Mr. Lamadokou", "Mr. Opare", "Mr. Keteku",
    "Mr. Bankesie", "Mr. Indome", "Mr. Amudzi", "Ms Antoinette", "Mr. Grant", "Ms Afiefa", "Mr. Mintah", "Mr. Botwe", "Mr. Adzogble",
    "Mr. Tetteh", "Ms. Gina Mills", "Mr. Oduro", "Mrs. Mondeh", "Mr. Neequaye", "Mr. Dotse", "Mr. Gbegan", "Mr. Incoom", "Mr. Nanor", "Mr. Mensah"
]

classes = [
    "Year 7 Sage", "Year 7 Sepia", "Year 8 Emerald", "Year 8 Coral", "Year 9 Maroon", "Year 9 Magenta", 
    "Year 10 Turquoise", "Year 10 Chalcedony", "Year 12"
]

days = 8
subjects_per_day = 2

schedule = generate_invigilation_schedule(teachers, classes, days, subjects_per_day)

for day, sessions in schedule.items():
    print(f"{day}:")
    for i, session in enumerate(sessions, 1):
        print(f"  Subject {i}:")
        for class_name, teacher in session.items():
            print(f"    {class_name}: {teacher}")
    print()
