class Employee:
    name = "ABC"
    age = 20
    salary = 30000 

class net_pay(Employee):
    def __init__(self, da_percentage, hra_percentage, pf_deduction_percentage):
        
        self.da = (da_percentage / 100) * self.salary
        self.hra = (hra_percentage / 100) * self.salary
        self.pf = (pf_deduction_percentage / 100) * self.salary

    def calculate_net(self):
        net_salary = self.salary + self.da + self.hra - self.pf
        return net_salary

pay_slip = net_pay(da_percentage=10, hra_percentage=15, pf_deduction_percentage=5)

print("--- Salary Slip ---")
print(f"Employee Name: {pay_slip.name}")
print(f"Basic Salary:  {pay_slip.salary}")
print(f"DA (Added):    +{pay_slip.da}")
print(f"HRA (Added):   +{pay_slip.hra}")
print(f"PF (Deducted): -{pay_slip.pf}")
print("-------------------")
print(f"Net Salary:    {pay_slip.calculate_net()}")