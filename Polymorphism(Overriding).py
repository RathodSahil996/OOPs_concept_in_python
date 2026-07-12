class employee:
    def get_designation(self):
        print("designation = employee")

class Teacher:
    def get_designation(self):
        print("designation = Teacher")

class proffesor:
    def get_designation(self):
        print("designation = Proffesor")
    

d1 = Teacher()
d1.get_designation()
d2 = employee()
d2.get_designation()