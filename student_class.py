''' Write a student class that keeps track of all created students. It should implement:
instance attrivute : name
property grade that returns grade of student.  If new grade is not between 0 and 100, raise ValueError
static method calculate_average_grade(students) that accepts list of all student objects and returns average grade(or -1 if no student in list)
class variable called all_students that stores all student objects that have been created in list.
get_average_grade() returns average grade of all created students.
get_best_student() returns student object with best grade out of all created students. if no student, return None. Assume there will be always one student with best grade.
'''
class Student:
    all_students=[]

    def __init__(self,name,grade):
        self.name=name
        self._grade=grade
        Student.all_students.append(self)   # appends object to student as soon as it is initialized
    
    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self,grade):
        if grade<1 or grade>99:
            raise ValueError("New grade not in the accepted range of [0-100].")
        self._grade=grade
        return self._grade
    
    @staticmethod
    def calculate_average_grade(students):   #accepts list of student objects
        if len(students)==0:
                return -1   #useful way to return -1 if there are no students in list
        sum_grade=0
        for student in students:
            sum_grade+=student.grade
        average_grade=sum_grade/len(students)
        return average_grade
    
    @classmethod
    def get_average_grade(cls):
        average_all_students=cls.calculate_average_grade(cls.all_students)
        return average_all_students

    @classmethod
    def get_best_student(cls):
        best_student=None      # for returning none if no student present in all_students
        for student in cls.all_students:
            if best_student==None or student.grade>best_student.grade:
                best_student=student
        return best_student

#self.assertEqual(average, 78)
#self.assertEqual(best_student, student2)
#self.assertEqual("Tim", best_student.name)
#self.assertEqual(average, 75)
#self.assertEqual(best_student, student1)
#self.assertEqual("Antoine", best_student.name)


'''
##checks done##:

average_grade_without_students = Student.get_average_grade()
self.assertEqual(average_grade_without_students, -1)
self.assertEqual(Student.get_best_student(), None)

student1 = Student("Antoine", 75)
average = Student.get_average_grade()
best_student = Student.get_best_student()
self.assertEqual(average, 75)
self.assertEqual(best_student, student1)
self.assertEqual("Antoine", best_student.name)

student2 = Student("Tim", 81)
average = Student.get_average_grade()
best_student = Student.get_best_student()
self.assertEqual(average, 78)
self.assertEqual(best_student, student2)
self.assertEqual("Tim", best_student.name)

student3 = Student("Clement", 30)
average = Student.get_average_grade()
best_student = Student.get_best_student()
self.assertEqual(average, 62)
self.assertEqual("Tim", best_student.name)

best_student = Student.get_best_student()
best_student.grade = best_student.grade - 10
new_best_student = Student.get_best_student()
self.assertEqual("Antoine", new_best_student.name)

best_student = Student.get_best_student()
with self.assertRaises(ValueError):
best_student.grade = 150

students = [
            Student("Simon", 55),
            Student("Alex", 69),
            Student("James", 8),
        ]
self.assertEqual(44, Student.calculate_average_grade(students))
'''        
        


    


