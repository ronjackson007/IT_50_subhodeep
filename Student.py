class Student:
    name = 'Subhodeep'
    branch = 'IT'
    sem = 4
    def info(self):
        print(f"{self.name}:{a.branch}:{a.sem}")

s1 = Student()
a = Student()
a.info()
print('Name: ',s1.name,' branch: ',s1.branch,' sem: ',s1.sem)
s1.name = 'Ram'
s1.branch = 'CS'
s1.sem = 3
print('Name: ',s1.name,' branch: ',s1.branch,' sem: ',s1.sem)

