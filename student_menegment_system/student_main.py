# import classes from other file
from student import Student
from student_menegment_system import StudentMeneger


# creating objects
manager=StudentMeneger()
manager.load_students()

#creating user interfce
while True:
    print('======student menegment system=======')
    print(' 1: add student')
    print(' 2: update student')
    print(' 3: delete student')
    print(' 4: list student')
    print(' 5: save student')
    print(' 6: Exit')
    
    choice=int(input('enter choice: '))
    
    if choice ==1:
        id=int(input('enter student id : '))
        name =input('enter student name : ')
        gread=input('enter gread of student : ')
        student=Student(id,name,gread)
        manager.add_student(student)
    elif choice ==2:
        id=int(input('enter student id : '))
        name=input('enter new name : ')
        gread=input('enter new gread : ')
        manager.update_student(id,name,gread)
    elif choice ==3:
        id=int(input('enter id of student ,that you want to delete'))
        manager.delete_student(id)
    elif choice ==4:
        manager.list_students()
    elif choice ==5:
        manager.save_students()
    elif choice ==6:
        manager.save_students()
        break
    else:
        print('invailid choice')