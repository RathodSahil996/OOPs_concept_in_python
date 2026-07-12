class Employee:
    def calculate_bonus(self, salary):
        return salary * 0.05

class Manager(Employee):
    def calculate_bonus(self, salary):
        return salary * 0.15

emp = Employee()
mgr = Manager()

base_salary = 50000

print(f"Standard Employee Bonus: {emp.calculate_bonus(base_salary)}")
print(f"Manager Bonus: {mgr.calculate_bonus(base_salary)}")