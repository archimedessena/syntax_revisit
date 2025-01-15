from datetime import datetime, timedelta
import random
from collections import defaultdict

class Course:
    def __init__(self, name, department, duration=3, students=None):
        self.name = name
        self.department = department
        self.duration = duration  # hours
        self.students = students or []  # list of student IDs

class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

class ExamScheduler:
    def __init__(self):
        # Initialize departments and their courses
        self.courses = {
            'Humanities': [
                Course('History', 'Humanities', students=['H1', 'H2', 'H3']),
                Course('Literature', 'Humanities', students=['H2', 'H3', 'H4']),
                Course('Philosophy', 'Humanities', students=['H1', 'H4', 'H5']),
                Course('Languages', 'Humanities', students=['H3', 'H5', 'H6'])
            ],
            'Science': [
                Course('Physics', 'Science', students=['S1', 'S2', 'S3']),
                Course('Chemistry', 'Science', students=['S2', 'S3', 'S4']),
                Course('Biology', 'Science', students=['S1', 'S4', 'S5']),
                Course('Mathematics', 'Science', students=['S3', 'S5', 'S6'])
            ],
            'Business': [
                Course('Economics', 'Business', students=['B1', 'B2', 'B3']),
                Course('Marketing', 'Business', students=['B2', 'B3', 'B4']),
                Course('Accounting', 'Business', students=['B1', 'B4', 'B5']),
                Course('Finance', 'Business', students=['B3', 'B5', 'B6'])
            ],
            'Arts': [
                Course('Fine Arts', 'Arts', students=['A1', 'A2', 'A3']),
                Course('Music', 'Arts', students=['A2', 'A3', 'A4']),
                Course('Theatre', 'Arts', students=['A1', 'A4', 'A5']),
                Course('Dance', 'Arts', students=['A3', 'A5', 'A6'])
            ]
        }
        
        # Available rooms
        self.rooms = [
            Room('Room A101', 30),
            Room('Room B201', 25),
            Room('Room C301', 35)
        ]
        
        self.time_slots = ['09:00 AM', '02:00 PM']
    
    def check_conflicts(self, course1, course2):
        """Check if two courses have any students in common"""
        return bool(set(course1.students) & set(course2.students))
    
    def generate_timetable(self, start_date_str):
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        timetable = {}
        scheduled_exams = []
        student_schedule = defaultdict(list)  # Track each student's exams
        
        # Create list of all courses
        all_courses = []
        for dept_courses in self.courses.values():
            all_courses.extend(dept_courses)
        
        # Shuffle courses for random scheduling
        random.shuffle(all_courses)
        current_date = start_date
        
        while all_courses:
            # Skip weekends
            if current_date.weekday() >= 5:
                current_date += timedelta(days=1)
                continue
            
            date_str = current_date.strftime('%Y-%m-%d')
            if date_str not in timetable:
                timetable[date_str] = {time: [] for time in self.time_slots}
            
            for time_slot in self.time_slots:
                # Try to schedule as many non-conflicting exams as possible
                available_rooms = self.rooms.copy()
                
                for course in all_courses[:]:
                    can_schedule = True
                    
                    # Check for student conflicts with already scheduled exams
                    for student in course.students:
                        if (date_str, time_slot) in student_schedule[student]:
                            can_schedule = False
                            break
                    
                    if can_schedule and available_rooms:
                        room = available_rooms.pop(0)
                        timetable[date_str][time_slot].append({
                            'course': course,
                            'room': room
                        })
                        
                        # Update student schedules
                        for student in course.students:
                            student_schedule[student].append((date_str, time_slot))
                        
                        all_courses.remove(course)
            
            current_date += timedelta(days=1)
        
        return timetable
    
    def print_timetable(self, timetable):
        print("\nEXAM TIMETABLE")
        print("=" * 100)
        print(f"{'Date':<12} {'Time':<10} {'Department':<12} {'Course':<15} {'Room':<10} {'Students'}")
        print("-" * 100)
        
        for date in sorted(timetable.keys()):
            for time_slot in self.time_slots:
                exams = timetable[date][time_slot]
                if exams:
                    for exam in exams:
                        course = exam['course']
                        room = exam['room']
                        students_str = ', '.join(course.students[:3]) + \
                                     ('...' if len(course.students) > 3 else '')
                        print(f"{date:<12} {time_slot:<10} {course.department:<12} "
                              f"{course.name:<15} {room.name:<10} {students_str}")
        print("=" * 100)

# Example usage
if __name__ == "__main__":
    scheduler = ExamScheduler()
    
    # Generate timetable starting from May 1st, 2025
    timetable = scheduler.generate_timetable('2025-05-01')
    
    # Print the generated timetable
    scheduler.print_timetable(timetable)




scheduler = ExamScheduler()
timetable = scheduler.generate_timetable('2025-05-01')
scheduler.print_timetable(timetable)