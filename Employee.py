class Employee():
    id = '01'
    name = 'Harry'
    salary = 100000

employee1 = Employee()
employee2 = Employee()

print(employee1.name, employee1.salary, employee1.id)
employee2.name = 'John'
employee2.salary = 200000
employee2.id = '02'
print(employee2.name, employee2.salary, employee2.id)
