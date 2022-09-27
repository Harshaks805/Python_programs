dic1={}
class employe:
  name=input("enter the name of employ\n")
  adress=input("enter thr adress\n")
  pan=int(input("enter the pan number\n"))
  basic=int(input("enter the basic salary\n"))
  tds=int(input("enter the tds\n"))
  diduct=int(input("enter the deduct value\n"))
  hra=int(input("enter the hra\n"))
  da=int(input("enter the da\n"))
  gross=(basic+tds+hra+da)
  net=(gross-diduct)

emp=employe()
dic1["NAME"]=emp.name
dic1["ADRESS"]=emp.adress
dic1["PAN"]=emp.pan
dic1["BASIC"]=emp.basic
dic1["TDS"]=emp.tds
dic1["DIDUCT"]=emp.diduct
dic1["HRA"]=emp.hra
dic1["DA"]=emp.da
dic1["GROSS"]=emp.gross
dic1["NET"]=emp.net

print(dic1)




choice="yes"

while choice=="yes":

  print("1.update information\n 2.perticular information \n 3.display all  details\n")

  ch=int(input("enter the choice\n"))


  if ch==1:
    f1=input("enter which fild you alter\n")
    v1=input("enter the new value\n")
    dic1[f1]=v1
    print("value updated\n") 
    print(dic1)


  elif ch==2:
    print("enter the detail you need from employ\n")
    d1=input()
    d2=dic1.get(d1)
    print(d2)



  elif ch==3:

    print("****EMPLOY-DETAILS******")

    print("name:%s"%dic1["NAME"])
    print("adress:%s"%dic1["ADRESS"])
    print("pan:%s"%dic1["PAN"])
    print("basic:%s"%dic1["BASIC"])
    print("tds:%s"%dic1["TDS"])
    print("da:%s"%dic1["DA"])
    print("diduct:%s"%dic1["DIDUCT"])
    print("hra:%s"%dic1["HRA"])

    print("gross:%s"%dic1["GROSS"])

    print("net:%s"%dic1["NET"])
 

  choice=input("do you like to continue\n")
