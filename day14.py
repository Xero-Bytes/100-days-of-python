'''
if else conditions
--->if
--->if-else
--->if-else-elif
--->nested if-else-elif
'''

# if-else statements
a=int(input("Enter your age: "))
print("Your age is: ",a)
if(a>18):
    print("You can drive!")
else:
    print("you cannot drive")

print("----------------------------------------------------")

# if-else-elif statements
Apple_Price=20
Budget=200
if(Apple_Price-Budget>50):
    print("Alexa, add 1 kg of Apples in the cart !")
elif(Apple_Price-Budget>70):
    print("its ok you can buy!")    
else:
   print("Alexa, don't add 1 kg of Apples in the cart !")

print("----------------------------------------------------")

# if-else-elif statements
num=int(input("Enter the value of num: "))
if(num<0):
    print("Number is negative")
elif(num==0):
    print("number is Zero")
else:
    print("number is positive")

print("----------------------------------------------------")  

# nested if statements
num=18
if(num<0):
    print("Number is negative")
elif(num>0):
    if(num<=10):
     print("number is between 1-10")
    elif(num>10 and num<=20):
     print("number is between 11-20")
    else:
       print("number is greater then 20") 
else:
    print("number is zero")

print("----------------------------------------------------") 

