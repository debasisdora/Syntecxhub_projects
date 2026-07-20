#import json and student class for accessing student object
import json
from student import Student

#creat meneger class 
class StudentMeneger:
    def __init__(self):
        self.students=[]
    
    # method to add student to students list
    def add_student(self, student):
        self.students.append(student)
        print('student added succesfully!')

    #methods to update student name and gread by student id
    def update_student(self,student_id,new_name,new_gread):
        for student in self.students:
            if student.student_id==student_id:
                student.name=new_name
                student.gread=new_gread
                print('update successfully')
                return
        print('student not exist')

    #method to delete student data by student id
    def delete_student(self,student_id):
        for student in self.students:
            if student.student_id==student_id:
                self.students.remove(student)
                print('student remove successfuly')
                return
        print('student does not exist')
    
    # method to show the list of students
    def list_students(self):
        if len(self.students)==0:
            print('no student avilable')
            return
        print('id     name      gread')
        for stu in self.students:
            print(stu.student_id,stu.name,stu.gread)
    
    #method to save data of student in json file
    def save_students(self):
        self.data=[]
        for student in self.students:
            self.data.append({
                "student_id": student.student_id,
                "student_name": student.name,
                "student_gread": student.gread
            })
        with open("students.json","w") as file:
            json.dump(self.data,file,indent=4)
    
    #methjod to acces data after refresh or running
    def load_students(self):
        try:
            with open("students.json","r") as file:
                self.std=json.load(file)
                for item in self.std:
                    student=Student(item['student_id'],item['student_name'],item['student_gread'])
                    self.students.append(student)
        except FileNotFoundError:
            print("no saved student file found")