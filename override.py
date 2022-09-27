#implimenting over loading

from multipledispatch import dispatch

class over:
  @dispatch(int,int)
  def product(first,secand):
      print("---(int) with two parmeer-----")
      result=first*secand
      print(result)
      print("------------")
 
  @dispatch(int,int,int)
  def product(first,secand,third):
     print("----(int) with three parameter----")
     result=first*secand*third
     print(result)
     print("-------------")

  @dispatch(float,float)
  def product(first,secand):
      print("----(floar) with two parameter----")
      result=first*secand
      print(result)
      print("------------")
  @dispatch(float,float,float)
  def product(first,secand,third):
      print("------(floar) with three opameter----")
      result=first*secand*third
      print(result)
      print("-------------")


ob1=over

while True:

  print("1.(int)2 parameter \n 2.(int) 3.parameter \n 3. (float) 2 parmeter \n 4. (float) 3parameter")
  print("enter the choice \n")
  ch=int(input())
  
  if ch==1:
    ob1.product(2,2)
  elif ch==2:
    ob1.product(2,2,2)
  elif ch==3:
    ob1.product(2.5,2.5)
  elif ch==4:
    ob1.product(2.5,2.5,2.5)
  else:
    print("invalid choice")
