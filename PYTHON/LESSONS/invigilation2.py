import random

# List of teachers
teachers = [
    "Mr. Boateng", "Mr. Apedido", "Mr. Klegbe", "Mr. Gbemu", "Mr. Boakye", "Mr. Asirifie",
    "Mr. Lamadokou", "Mr. Opare", "Mr. Keteku", "Mr. Bankesie", "Mr. Indome", "Mr. Amudzi",
    "Ms Antoinette", "Mr. Grant", "Ms Afiefa", "Mr. Mintah", "Mr. Botwe", "Mr. Adzogble",
    "Mr. Tetteh", "Mr. Gina Mills", "Mr. Oduro", "Mrs. Mondeh", "Mr. Neequaye", "Mr. Dotse",
    "Mr. Gbegan", "Mr. Incoom", "Mr. Nanor", "Mr. Mensah"
]

# List of classes
classes = [
    "Year 7 Sage", "Year 7 Sepia", "Year 8 Emerald", "Year 8 Coral", "Year 9 Maroon", 
    "Year 9 Magenta", "Year 10 Turquoise", "Year 10 Chalcedony", "Year 12"
]

# Number of exam days and sessions per day
exam_days = 5
sessions_per_day = 2  # Morning and Afternoon

# Function to generate invigilation schedule
def generate_schedule():
    schedule = {}
    for day in range(1, exam_days + 1):
        schedule[f"Day {day}"] = {}
        for session in ["Morning", "Afternoon"]:
            assigned_teachers = random.sample(teachers, 3)  # 3 teachers per session
            assigned_classes = random.sample(classes, 3)    # 3 classes per session
            schedule[f"Day {day}"][session] = list(zip(assigned_teachers, assigned_classes))
    return schedule

# Generate and print schedule
invigilation_schedule = generate_schedule()
for day, sessions in invigilation_schedule.items():
    print(f"\n{day}")
    for session, assignments in sessions.items():
        print(f"  {session}:")
        for teacher, class_assigned in assignments:
            print(f"    {teacher} -> {class_assigned}")
