list_courses = []
class course : 
    def __init__ (self , name , id ,mark,credits):
        self.name = name 
        self.id   = id
        self.mark = mark
        self.credits = credits
    def print_details(self):
        print("Course name:" + self.name)
        print("Course id :" + self.id)
        print("Course mark:" + self.mark)
        print("Course credits:" + self.credits)


def input_number_of_course():
    number_of_course = int(input("Enter number of course: "))
    return number_of_course

def input_course_info():
    number_of_course = input_number_of_course()
    for i in range(0,number_of_course):
        name = input("Enter course's name: ")
        id  = input("Enter course's id: ")
        mark = input("Enter course's mark: ")
        credits = input("Enter course's credits: ")
        course_info = course(name,id, mark,credits)
        list_courses.append(course_info)
        print("\n")     

def list_course():
    for i in range(0,len(list_course)):
        print("Course number ",i+1)
        print("Course name : " + list_course[i].name)
        print("Course id : " + list_course[i].id)
        print("Course mark : " + list_course[i].mark)
        print("Course credits : " + list_course[i].credits)
        print("\n")
 

input_course_info()