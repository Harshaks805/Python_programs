class operater:
    
   def __init__(self): 
      self.list=[]
   def getelement(self):
     self.n=input("enter the maximum element")
     if self.n=="":
       self.n=int(input("enter the element greater then 0 \n"))
       for i in range(self.n):
         self.list.append(int(input("enter the element")))
     elif self.n=="0":
          
       self.n=int(input("enter the element greater then 0 \n"))
       for i in range(self.n):
         self.list.append(int(input("enter the element")))
     else:
       self.n=int(self.n)   
       for i in range(self.n):
         self.list.append(int(input("enter the element")))
     print(self.list)
   def __add__(self,other):
      self.nl=[]
      self.zl=list(zip(self.list,other.list))
      for i in self.zl:
        
        self.nl.append(i[0]+i[1])
      print(self.nl)


   def __sub__(self,other):
       self.nl=[]
       self.zl=list(zip(self.list,other.list))
       for i in self.zl:
         self.nl.append(i[0]-i[1])
       print(self.nl)

   def __mul__(self,other):
      self.nl=[]
      self.zl=list(zip(self.list,other.list))
      for i in self.zl:
            
        self.nl.append(i[0]*i[1])
      print(self.nl)
   


   def __floordiv__(self,other):
       self.nl=[]
       self.zl=list(zip(self.list,other.list))
       for i in self.zl:
         if i[1]==0:
           print("floor division not posible in",i,"posision")  
         else: 
           self.nl.append(i[0]//i[1])
       print(self.nl)

   def __eq__(self,other):
        if self.n != other.n:
           print("number of elements in both  arry are not equal\n")

