# match case
x=int(input("Enter thr number: "))
match(x):
    case 0:
        print("x is zero")
    case 4:
       print("x is four")
    case _:
        print(x)   
print("________________________________________")   
# we can add if-else in match case
x=int(input("Enter thr number: "))
match(x):
    case 0:
        print("x is zero")
    case 4:
       print("x is four")
    case _ if(x!=90):
        print(x,"is not 90")
    case _ if(x!=80):
        print(x,"is not 80") 
    case _ :
        print(x)          