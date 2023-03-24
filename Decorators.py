class Employee:
    noe = 100
    @classmethod
    def change_noe(cls, newemp):
        cls.noe = newemp

r = Employee()
r.change_noe(200)
print(Employee.noe)