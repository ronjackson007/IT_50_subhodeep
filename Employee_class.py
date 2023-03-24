class Employee(object):
    # pass
    no_of_employee = 100
#     def __init__(self, name, salary, pos):
#         self.name = name
#         self.salary = salary
#         self.pos = pos
#     def display(self):
#         print(self.name, self.salary, self.pos)
#
# res1 = Employee('raju', 40000, 'ccc')
# res2 = Employee('Arjun', 10000, 'cdd')
#
# res1.display()
# res2.display()
#
# Employee.display(res1)
# Employee.display(res2)

# r = Employee()
# s = Employee()
# r.name = 'raju'
# r.salary = 40000
# s.salary = 99000
# s.name = 'arjun'
# print(r.name, r.salary, s.name, s.salary)

r = Employee()
Employee.no_of_employee = 500

print(Employee.no_of_employee)