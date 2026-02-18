import random
from collections import defaultdict
import pandas as pd
#from tabulate import tabulate

# Teacher names
teachers = [
    "Mr. Boateng", "Mr. Apedido", "Mr. Klegbe", "Mr. Gbemu", "Mr. Boakye", 
    "Mr. Asirifie", "Mr. Lamadokou", "Mr. Opare", "Mr. Keteku", "Mr. Bankesie", 
    "Mr. Indome", "Mr. Amudzi", "Ms Antoinette", "Mr. Grant", "Ms Afiefa", 
    "Mr. Mintah", "Mr. Botwe", "Mr. Adzogble", "Mr. Tetteh", "Mr. Gina Mills", 
    "Mr. Oduro", "Mrs. Mondeh", "Mr. Neequaye", "Mr. Dotse", "Mr. Gbegan", 
    "Mr. Incoom", "Mr. Nanor", "Mr. Mensah"
]

# Classes
classes = [
    "Year 7 Sage", "Year 7 Sepia", "Year 8 Emerald", "Year 8 Coral",
    "Year 9 Maroon", "Year 9 Magenta", "Year 10 Turquoise", "Year 10 Chalcedony", "Year 12"
]

# Exam parameters
num_subjects_per_day = 2
num_days = 5
subjects = ["Subject " + str(i+1) for i in range(num_subjects_per_day * num_days)]

# We need 2 invigilators per class
invigilators_per_class = 2

def generate_invigilation_schedule():
    # Schedule structure: day -> subject -> class -> invigilators
    schedule = {}
    
    # Track teacher workload to ensure fair distribution
    teacher_workload = defaultdict(int)
    
    # Track when teachers are scheduled to avoid double booking
    teacher_schedule = defaultdict(list)
    
    for day in range(1, num_days + 1):
        schedule[day] = {}
        
        for subject_idx in range(num_subjects_per_day):
            subject = f"Subject {(day-1) * num_subjects_per_day + subject_idx + 1}"
            schedule[day][subject] = {}
            
            # For each class, assign invigilators
            for class_name in classes:
                # Get available teachers (not already scheduled for this subject on this day)
                time_slot = f"Day {day}, {subject}"
                available_teachers = [t for t in teachers if time_slot not in teacher_schedule[t]]
                
                # Sort by workload to prioritize less busy teachers
                available_teachers.sort(key=lambda t: teacher_workload[t])
                
                # Select invigilators
                selected_invigilators = available_teachers[:invigilators_per_class]
                
                # Update workload and schedule
                for teacher in selected_invigilators:
                    teacher_workload[teacher] += 1
                    teacher_schedule[teacher].append(time_slot)
                
                schedule[day][subject][class_name] = selected_invigilators
    
    return schedule, teacher_workload

def format_schedule(schedule, teacher_workload):
    # Format for display
    formatted_schedule = []
    
    for day in range(1, num_days + 1):
        for subject_idx in range(num_subjects_per_day):
            subject = f"Subject {(day-1) * num_subjects_per_day + subject_idx + 1}"
            
            for class_name in classes:
                invigilators = schedule[day][subject][class_name]
                formatted_schedule.append([
                    f"Day {day}", 
                    subject, 
                    class_name, 
                    " & ".join(invigilators)
                ])
    
    # Create DataFrame for better display
    df = pd.DataFrame(formatted_schedule, columns=["Day", "Subject", "Class", "Invigilators"])
    
    # Teacher workload summary
    workload_summary = [[teacher, workload] for teacher, workload in sorted(teacher_workload.items(), key=lambda x: x[1], reverse=True)]
    workload_df = pd.DataFrame(workload_summary, columns=["Teacher", "Total Sessions"])
    
    return df, workload_df

def main():
    # Generate schedule
    print("Generating invigilation schedule...")
    schedule, teacher_workload = generate_invigilation_schedule()
    
    # Format for display
    schedule_df, workload_df = format_schedule(schedule, teacher_workload)
    
    # Display results
    print("\n=== INVIGILATION SCHEDULE ===\n")
    print(tabulate(schedule_df, headers='keys', tablefmt='grid', showindex=False))
    
    print("\n=== TEACHER WORKLOAD SUMMARY ===\n")
    print(tabulate(workload_df, headers='keys', tablefmt='grid', showindex=False))
    
    # Export to Excel (uncomment if needed)
    # with pd.ExcelWriter('invigilation_schedule.xlsx') as writer:
    #     schedule_df.to_excel(writer, sheet_name='Schedule', index=False)
    #     workload_df.to_excel(writer, sheet_name='Workload', index=False)
    # print("\nSchedule exported to 'invigilation_schedule.xlsx'")

if __name__ == "__main__":
    main()