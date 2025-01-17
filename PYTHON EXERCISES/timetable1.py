from datetime import datetime, timedelta
import random

class ExamScheduler:
    def __init__(self):
        # List of all subjects
        self.subjects = [
            "Accounting 1", "Accounting 2", 
            "Add Math 1", "Add Math 2",
            "Arts and Design 1", "Arts and Design 2",
            "Biology 2", "Biology 4", "Biology 6",
            "Business Studies 1", "Business Studies 2",
            "Chemistry 2", "Chemistry 4", "Chemistry 6",
            "Economics 1", "Economics 2",
            "English 1", "English 2",
            "French 1", "French 2", "French 4",
            "Geography 1", "Geography 2", "Geography 4",
            "History 1", "History 2", "History 4",
            "ICT 1", "ICT 2", "ICT 3",
            "Literature 1", "Literature 3", "Literature 4",
            "Core Math 1", "Core Math 3",
            "Extended Math 2", "Extended Math 4"
        ]
        
        # Define time slots
        self.morning_slot = "9:00 AM - 12:00 PM"
        self.afternoon_slot = "2:00 PM - 5:00 PM"
        
    def check_subject_conflict(self, subject1, subject2):
        """
        Check if two subjects might have conflicts (same subject area, same level)
        """
        # Extract subject base name and level
        def get_subject_info(subject):
            parts = subject.split()
            return ' '.join(parts[:-1]), parts[-1]
        
        subject1_base, level1 = get_subject_info(subject1)
        subject2_base, level2 = get_subject_info(subject2)
        
        # Don't schedule same subject area in one day
        return subject1_base == subject2_base
    
    def generate_timetable(self, start_date_str):
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        timetable = {}
        remaining_subjects = self.subjects.copy()
        random.shuffle(remaining_subjects)
        
        current_date = start_date
        
        while remaining_subjects:
            # Skip weekends
            if current_date.weekday() >= 5:
                current_date += timedelta(days=1)
                continue
                
            date_str = current_date.strftime('%Y-%m-%d')
            
            # Get morning subject
            morning_subject = remaining_subjects.pop(0)
            
            # Find suitable afternoon subject (no conflicts with morning subject)
            afternoon_subject = None
            for i, subject in enumerate(remaining_subjects):
                if not self.check_subject_conflict(morning_subject, subject):
                    afternoon_subject = remaining_subjects.pop(i)
                    break
            
            # If no suitable afternoon subject found, put morning subject back and try next day
            if afternoon_subject is None:
                remaining_subjects.append(morning_subject)
                current_date += timedelta(days=1)
                continue
                
            # Add to timetable
            timetable[date_str] = {
                'morning': morning_subject,
                'afternoon': afternoon_subject
            }
            
            current_date += timedelta(days=1)
            
        return timetable
    
    def print_timetable(self, timetable):
        print("\nEXAMINATION TIMETABLE")
        print("=" * 90)
        print(f"{'Date':<12} {'Morning Session':<35} {'Afternoon Session':<35}")
        print("-" * 90)
        
        for date in sorted(timetable.keys()):
            print(f"{date:<12} "
                  f"{timetable[date]['morning']:<35} "
                  f"{timetable[date]['afternoon']:<35}")
        
        print("=" * 90)
        print(f"\nTotal examination days: {len(timetable)}")
        
    def export_to_text(self, timetable, filename):
        """Export timetable to a text file"""
        with open(filename, 'w') as f:
            f.write("EXAMINATION TIMETABLE\n")
            f.write("=" * 90 + "\n")
            f.write(f"{'Date':<12} {'Morning Session':<35} {'Afternoon Session':<35}\n")
            f.write("-" * 90 + "\n")
            
            for date in sorted(timetable.keys()):
                f.write(f"{date:<12} "
                       f"{timetable[date]['morning']:<35} "
                       f"{timetable[date]['afternoon']:<35}\n")
            
            f.write("=" * 90 + "\n")
            f.write(f"\nTotal examination days: {len(timetable)}")

# Example usage
if __name__ == "__main__":
    scheduler = ExamScheduler()
    
    # Generate timetable starting from a specific date
    timetable = scheduler.generate_timetable('2025-05-01')
    
    # Print the timetable
    scheduler.print_timetable(timetable)
    
    # Export to text file
    scheduler.export_to_text(timetable, 'exam_timetable.txt')