class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class employee:
    def __init__(self,id,salary):
        self.id = id
        self.salary = salary

class manager(person,employee):
    def __init__(self):
        return self.name,self.age,self.salary

emp1 = manager("Kakashi",25,1,25_000)

print(emp1.id,emp1.name,emp1.age,emp1.salary)