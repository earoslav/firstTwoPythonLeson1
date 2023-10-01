class Student:
    def __init__(self,name,sureName,age,logics,
                 group,login,password,telegram):
        self.name = name
        self.sureName = surName         
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
        print("telegram:",self.password)    
    def lodgicInfo(self):
        print("students logics:")
        lg = ""
        for logik in self.logics:
            lg += str(logics)+", "
        all_lg = sum(self.logics) 
        print(lg)
        print("all logics:", all_lg)
        print("=================")


students = list()
student = Student("Yrik","gorbatyuk",13,[1,2,3,4,4,4,4],"python","yril","123","yriak")      
students.append(students)
print("all students:")
for i in range(len(students)):
    print(students[i].sureName)
while True:
    print("What do you want? 1 - all info, 2 - logics, 3 - exit") 
    do = int(input(""))
    who = int(input("enter number of student"))
    if do == 1:


