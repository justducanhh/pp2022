list_students = []
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
    
def list_student():
    for i in range(0,len(list_student)):
        print("Student's number ",i+1)
        print("Student's name : " + list_student[i].name)
        print("dob : " + list_student[i].dob)
        print("id : " + list_student[i].id)
        print("\n")

input_student_info()