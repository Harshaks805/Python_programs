class student:
    def __init__(self):
       self.name=" "
       self.usn=" "
       self.age=" "
    def getdata(self):
       self.name=input("enter the name")
       self.usn=input("enter the usn no")
       self.age=input("enter the age")

    def display(self):
          print("name:",self.name)
          print("usn:",self.usn)
          print("age:",self.age)





class student1(student):
    
    def __init__(self):
        self.sub1=0
        self.sub2=0
        self.sub3=0
        self.sub4=0
        self.total=0
        self.percentage=0

    def getcalculate(self):
        self.sub1=int(input("enter the sub1 number"))
        self.sub2=int(input("enter the sub2 number"))
        self.sub3=int(input("enter the sub3 number"))
        self.sub4=int(input("enter the sub4 number"))

        self.total=self.sub1+self.sub2+self.sub3+self.sub4
        self.percentage=self.total/400*100

class student2(student1):
     def displaydata(self):
          print("sub1=",self.sub1)
          print("sub2=",self.sub2)
          print("sub3=",self.sub3)
          print("sub4=",self.sub4)
          print("total=",self.total)
          print("percentage=",self.percentage)



ob1=student2()
ob1.getdata()
ob1.display()
ob1.getcalculate()
ob1.displaydata()

