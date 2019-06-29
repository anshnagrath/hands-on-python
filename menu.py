studentsList = []
def add_new_student(studentsList):
    name = input('Add student name')
    marks = int(input('Add student Marks'))
    student = {
        'name':name,
         'marks':[marks] 
    }
    return studentsList.append(student)

def add_marks_to_student(studentsList):
    studentId = int(input('please provide id of student'))
    marks = int(input('please provide marks of student'))
    selectedStudent = studentsList[studentId]
    return selectedStudent['marks'].append(marks)

def calculate_average_marks(student):
    number = len(student['marks'])
    if number == 0:
        print('Please add marks to the student First')
    avg = sum(student['marks'])/number  
    return avg

def print_student_details(student):
    print("{},average marks:{}".format(student['name'],calculate_average_marks(student)))


def print_all_students(students):
    for i,student in enumerate(students):
        print('Student Id is {}'.format(i)) 
        print_student_details(student)

def menu():
    selection = input("Enter 'p' to print students list ,'s' to add a new student ,'a' to add a mark to student and 'q' to quit':")
    while(selection != 'q'):
        if selection == 'p':
           print_all_students(studentsList)
        elif selection == 's':
           add_new_student(studentsList)
        elif selection == 'a':
            add_marks_to_student(studentsList)     
        selection = input("Enter 'p' to print students list ,'s' to add a new student ,'a' to add a mark to student and 'q' to quit':")
menu()

