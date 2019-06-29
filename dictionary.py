def create_student():
    name = input("Please enter the new student name: ")
    student_data = {
        'name':name,
         'marks':[]
    }
    return student_data
s=create_student()
def add_mark(student,mark):
    student['marks'].append(mark)
add_mark(s,5)
print(s)  # passing by reference
z=4
def add_number(x,y):
    x=x+y
add_number(z,10)        
print(z)
print(s)