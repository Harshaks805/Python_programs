class student:
    def __init__(self):
       self.name=" "
       self.usn=" "
       self.age=" "
    def getdata(self):
       self.name=input("enter the name\n")
       self.usn=int(input("enter the usn number\n"))
       self.age=int(input("enter the age\n"))
    def display(self):
       print("NAME=",self.name)
       print("USN=",self.usn)
       print("AGE=",self.age) 

class pgstudent(student):
    def __init__(self):
       self.semister=" "
       self.fees=" "
       self.stipent=" "
    def getdata_pg(self):
        self.semister=input("enter the semister \n")
        self.fees=int(input("enter the fess \n"))
        self.stipent=int(input("enter the stipent \n"))
    def display_pg(self):
        print("SEMISTER:",self.semister)
        print("FEES:",self.fees)
        print("STIPEND:",self.stipent)

class ugstudent(student):

    def __init__(self):
       self.semister=" "
       self.fees=" "
       self.stipent=" "
    def getdata_ug(self):
        self.semister=input("enter the semister \n")
        self.fees=int(input("enter the fess \n"))
        self.stipent=int(input("enter the stipent \n"))
    def display_ug(self):
        print("SEMISTER:",self.semister)
        print("FEES:",self.fees) 
        print("STIPEND:",self.stipent) 



pg=pgstudent()
ug=ugstudent()

#pg student

pg.getdata()
pg.getdata_pg()
print("-------PG_student-----------")
pg.display()
pg.display_pg()

print("---------------------------")

#ug student
ug.getdata()
ug.getdata_ug()
print("--------UG_student----------")
ug.display()
ug.display_ug()

print("----------------------------")

