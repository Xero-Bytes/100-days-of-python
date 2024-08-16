'''       functions in python
functions are blocks of reusable code that 
perform a specific task. They help in organizing 
code,making it more readable and maintainable.
Functions can take inputs (called parameters),
perform some processing, and then return an output.
--->     Defining a Function
You define a function using the def keyword, followed
by the function name, parentheses (), and a colon :.
The code inside the function is indented.
       def function_name(parameters):
           Code block
          return value
'''
def sum(a,b):
    sum=a+b
    return sum
a=10
b=12
addition=sum(a,b)
print(addition)