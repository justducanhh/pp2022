list_student = []
list_course = []
student = {"name":None,"id":None,"DoB":None}
course = {"id":None,"name":None}

def input_no_students():
        no_students = int(input('Enter the number of students : '))
        return no_students


def input_student_info():
    no_student= input_no_students() 
    for i in range(0,no_student):
        sid=input('Enter student id : ')
        sname=input('Enter student name : ')
        sDoB=input('Enter student DoB : ')
        student_info = {"id":sid,"name":sname,"DoB":sDoB}
        list_student.append(student_info)
        print('\n')
               
def input_no_courses():
        no_courses = int(input('Enter the number of courses : '))
        return no_courses
    
def input_course_info():
    no_courses = input_no_courses()
    for i in range(0,no_courses):
            course_id=input('Enter course id : ')
            course_name=input('Enter course name : ')
            course_info ={"course_id":course_id,"course_name":course_name}
            list_course.append(course_info)
            print('\n')
            
def input_marks_course():
        for i in range(0,len(list_student)):
            print('Name : ',list_student[i].get("name"))
            print('ID : ',list_student[i].get("id"))
            print('DoB : ',list_student[i].get("DoB"))
            mark = float(input('Enter student mark: '))
            course_mark_dict = {"course_mark":mark,"course_selected":course_selected}
            list_student[i].update(course_mark_dict)
            list_course[i].update(course_mark_dict)
            print('\n')
            break
                
def list_courses():
    for i in range(0,len(list_course)):
        print('COURSE NUMBER ',i+1)
        print('Name: ',list_course[i].get("course_name"))
        print('ID: ',list_course[i].get("course_id"))

def list_students():
    for i in range(0,len(list_student)):
        print('Name: ',list_student[i].get("name"))
        print('ID: ',list_student[i].get("id"))
        print('DoB: ',list_student[i].get("DoB"))
        print('Course id: ',list_student[i].get("course_selected"))
        print('MARK: ',list_student[i].get("course_mark"))
        print('\n')

print('\n')
input_student_info()
input_course_info()

course_selected = input('Enter course id: ')
input_marks_course()
"listing all the courses".upper()
list_courses()
"listing all the students".upper()
list_students()