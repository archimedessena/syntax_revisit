# Title: Online Course Management System

# Description: The code represents an online course management system that helps keep track of online courses, students, and their grades. it allows you to do things like enroll students, see course details, and calculate average grades.

class OnlineCourse:
    def __init__(self, course, instructor):
        self.course = course
        self.instructor = instructor
        self.students = []
              
    def enroll_students(self, student):
        self.students.append(student)
        print(f"{student.name} has been enrolled in the {self.course} course.")
    
    def course_details(self):
        print(f"Course: {self.course}")
        print(f"Instructor Name:", self.instructor)
        print(f"Enrolled Students: {', '.join(self.students)}")
        
    def completed_course(self, name):
        if name in self.students:
            self.students.remove(name)
            print(f"{name} has completed course!")
        else:
            print(f"{name} is not enrolled in this course.")
                      
    def avg_grade(self, grades):
        total = sum(grades)
        average = total / len(grades)
        print(f"The average grade is: {average}")
        
        

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
        
   
        
course_input = input("Enter a course: ").lower()
name = input("Enter an Instructor: ").lower()
student = input("Enter name of student: ").lower()

#course = OnlineCourse(course_input, name) 
#grades = [90, 85, 92, 78, 80]
#
#course.avg_grade(grades)
#course.enroll_students(student)
#course.course_details()
#course.completed_course(name="Emelia")

course_input = input("Enter a course: ").lower() 
name = input("Enter an instructor: ").lower()
course = OnlineCourse(course_input, name)



num_students = int(input("Enter number of students"))

for _ in range(num_students):
    student_name = input("Enter student name: ").lower()
    grades = []
    for _ in range(3):
        grade = int(input("Enter grade: "))
        grades.append(grade) 
    student = student(student_name, grades)
    course.enroll_students(student)
    course.avg_grade(student)
course.course_details()











