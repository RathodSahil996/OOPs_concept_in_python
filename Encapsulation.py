class Student:
    def __init__(self,name,age,gpa,password):
        self.name = name
        self.age = age
        self._gpa = gpa
        self.__password = password
        
    def get_password(self):
        return self.__password

std1 = Student("ABC","20",9.0,"EnterAnyPassword")
print(std1.name,std1.age,std1._gpa,std1.get_password())