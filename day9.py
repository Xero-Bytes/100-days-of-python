# Type casting 
''' the conversion of one data type into another is called type casting in python
python support a varaiety of functions or methods like int(),float(),str(),ord()
,hex(),oct(),tuple(),set(),list(),dict(),etc for the type casting in python.
1--->Explicit Type casting(Conversion)
2--->Implicit Type casting(conversion)
Python provides various built-in functions for type casting, such as int(), float(), 
str(), ord(), tuple(), list(), set(), dict(), hex(), and oct().
• Explicit type casting is done manually by the developer using these functions.
• Implicit type casting occurs automatically by the Python interpreter based on data type 
hierarchy.
'''

# a="2"
# b="3"
# print(a+b)we cannot perform addition on a and b because a and b both are strings
# but when we convert their data type into int by using typecasting we can perform 
# addition


# explicit type casting

a="2"
b="3"
print(int(a)+int(b))
print("---------------------")

string="15"
number=7
string_number=int(string) #throws an error if the string is not a valid integer.
sum=number+string_number
print("The sum of both numbers is ",sum)

print("----------------------")

# implicit Type casting 
# python automatically convert d into float 
c=1.9
d=8
print(c+d)