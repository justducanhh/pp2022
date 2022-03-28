list_students = []
list_course = []

class person:
    def __init__(self, name, age, dob):
        self.name = name
        self.age = age
        self.dob = dob
    def print_details(self):
        print("Name: " + self.name)
        print("Age: " + self.age)
        print("DOB: " + self.dob)


class student :
    def __init__(self, name ,age,dob, id):
        self.name   = name
        self.dob    = dob
        self.age    = age
        self.id     = id 

    def print_details(self):
        print("Student's name: " + self.name)
        print("dob: " + self.dob)
        print("id: " + self.id)
        print("course: " + self.course)

class course : 
    def __init__ (self , name , id , mark):
        self.name = name 
        self.id   = id
        self.mark = mark 
    def print_details(self):
        print("Course name:" + self.name)
        print("Course id :" + self.id)
        print("Student's mark:" + self.mark)
        
def input_number_of_students():
    number_of_students = int(input("Enter number of students: "))
    return number_of_students
 
    
def input_student_info():
    number_of_students = input_number_of_students()
    for i in range(0,number_of_students):
        name = input("Enter student's name: ")
        age = input("Enter student's age: ")
        dob = input("Enter student's dob: ")
        id = input("Enter student's id: ")
        student_info = student(name,age,dob,id)
        list_students.append(student_info)
        print("\n")
        break
    
def list_student():
    for i in range(0,len(list_students)):
        print("Student's number",i+1)
        print("Student's name: " + list_students[i].name)
        print("dob: " + list_students[i].dob)
        print("id: " + list_students[i].id)
        print("\n")
        break
    
def input_number_of_course():
    number_of_course = int(input("Enter number of course: "))
    return number_of_course

def input_course_info():
    number_of_course = input_number_of_course()
    for i in range(0,number_of_course):
        name = input("Enter course's name: ")
        id  = input("Enter course's id: ")
        mark = input("Enter course's mark: ")
        course_info = course(name,id,mark)
        list_course.append(course_info)
        print("\n")
        break 
    
def list_courses():
    for i in range(0,len(list_course)):
        print("Course number",i+1)
        print("Course name: " + list_course[i].name)
        print("Course id: " + list_course[i].id)
        print("Course mark: " + list_course[i].mark)
        print("\n")
        break
    

input_student_info()
input_course_info()
list_student() 
list_courses()
