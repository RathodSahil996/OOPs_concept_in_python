class Student:
    def __init__(self,name,age,password):
        self.name = name
        self._age = age
        self.__password = password
        
    def get_password(self):
        return self.__password

std1 = Student("ABC","20","EnterAnyPassword")
print(std1.name,std1._age,std1.get_password())