class Student:
    def __init__(self,name,sureName,age,logics,
                 group,login,password,telegram):
        self.name = name
        self.sureName = sureName         
        self.age = age
        self.logics = logics
        self.group = group
        self.login = login
        self.password = password
        self.telegram = telegram

    def allInfo(self):
        print("all info of student:")
        print("name:",self.name)
        print("sureName:",self.sureName)
        print("age:",self.age)
        print("group:",self.group)
        print("logics:",self.logics)
        print("password:",self.password)
        print("telegram:",self.telegram)    
    def lodgicInfo(self):
        print("students logics:")
        lg = ""
        for logik in self.logics:
            lg += str(logik)+", "
        all_lg = sum(self.logics) 
        print(lg)
        print("all logics:", all_lg)
        print("=================")


students = list()
student = Student("Yrik","gorbatyuk",13,[1,2,3,4,4,4,4],"python","yril","123","yriak")      
student1 = Student("Oleg","Shevchenco",23,[1,3,1,6,6,1,1],"Scratch","Shevchuk","231","Sheva") 
student2 = Student("Olga","Volga",123,[2,1,2,3,1,2,1],"java","OlgaVolga","321","Valuna") 
students.append(student)
students.append(student1)
students.append(student2)
print("all students:")
for i in range(len(students)):
    print(students[i].sureName)
while True:

    do = int(input("What do you want? 1 - all info, 2 - logics, 3 - exit"))
    who = int(input("enter number of student"))
    if do == 1:
        Student.allInfo(students[who-1])
    if do == 2: 
        Student.lodgicInfo(students[who-1])
    if do == 3:
        break    

