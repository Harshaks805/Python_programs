from operater import *

ov1=operater()
ov2=operater()
ov1.getelement()
ov2.getelement()
ov1==ov2

choice="yes"
while choice=="yes":

  print("1.add \n 2.sub \n 3.mul \n 4.div \n")
  ch=int(input("enter the choice"))
  if ch==1:
    ov1+ov2
  elif ch==2:
    ov1-ov2
  elif ch==3:
    ov1*ov2
  elif ch==4:
    ov1//ov2
  else: 
   print("invalid choice")
  choice=input("do you like to continue\n") 
