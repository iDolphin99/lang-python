'''
일반적인 사람을 나타내는 Person 클래스를 정의한다. 
Person 클래스를 상속받아서 학생을 나타내느 클래스 Student와 
선생님을 나타내는 클래스 Teacher를 정의한다 
'''


class Person :
    def __init__(self, name, number):
        self.name = name
        self.number = number
        
class Student(Person) :
    UNDERGRADUATE = 0
    POSTGRADUATE = 1 
    
    def __init__(self, name, number, studentType):
        super().__init__(name, number)
        self.studentType = studentType
        self.gpa = 0
        self.classes = []
    def enrollCourse(self, course) : # 과목 등록 
        self.classes.append(course)
    def __str__(self):
        return "\n이름 = " + self.name + "\n주민번호 = " + self.number + "\n수강과목 = " + str(self.classes) + "\n평점 = " + str(self.gpa)
        
class Teacher(Person) :
    def __init__(self, name, number):
        super().__init__(name, number)
        self.courses = []
        self.salary = 300000
    def assignTeaching(self,course) : 
        self.courses.append(course)
    def __str__(self):
        return "이름 = " + self.name + "\n주민번호 = " + self.number + "\n강의과목 = " + str(self.courses) + "\n월급 = " + str(self.salary)
    
hong = Student("홍길동","12345678", Student.UNDERGRADUATE)
hong.enrollCourse("자료구조")
print(hong)

kim = Teacher("김철수", "123456790")
kim.assignTeaching("Python")
print(kim)        

        