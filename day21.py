# function Arguments
# we can pass function arguments as a tuple or as a dictionary
# Parameters are the variables listed inside the parentheses in the
#  function definition.
# Arguments are the values you pass to the function when calling it.
# there are 4 tpes of arguments.
# --->Default Parameters:
# You can provide default values for parameters,
# which are used if no argument is provided when
# the function is called.
def greet(name="Taqdees"):
    return f"Hello, {name}!"

print(greet())          # Output: Hello, Guest!
print(greet("Saman"))   # Output: Hello, Alice!

# EXAMPLE2
def name(fname="",mname="Fatima",lname="Bukhari"):
    print("Hello,",fname,mname,lname)

name("Taqdees")
#2. ---->KeyWords Arguments
# Keyword arguments allow you to pass arguments to a function by explicitly
# specifying the name of the parameter. This way, you can pass arguments in 
# any order, and it improves the readability of the code.you can change the order

def introduction(name,age,city):
    print("my name is",name,"my age is",age,".","my city is",city,)
introduction(name="Syeda Taqdees Bukhari.",age=18,city="Muzzaffarabad.")
introduction(city="Muzzaffarabad.",name="Syeda Taqdees Bukhari.",age=18)

# Variable length argument
def name(**name):
    print("Hello,",name["fname"],name["mname"],name["lname"])

name(mname="Batool",lname="Bukhari",fname="Saman")