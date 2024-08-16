# Strings
name1="Taqdees"
name2='fatima'
print("name1 is "+name1)
print("name2 is ",name2)

print('He said ,"I want to eat an apple".')


# MULTILINE STRINGS
# ----->> By using triple single quotes (''' ''')or triple double quotes(""" """)
str="""
Python is a versatile and powerful programming language that is widely used in 
various fields such as web development, data analysis, artificial intelligence,
 and automation. It is known for its simple and readable syntax, which makes it 
 an excellent choice for both beginners and experienced developers. Python's 
 extensive standard library and supportive community contribute to its popularity,
allowing developers to easily find resources and tools for their projects. Whether 
you're building a web application, analyzing data, or creating 
machine learning models, Python offers the flexibility and functionality
needed to accomplish your goals efficiently.
"""
str1='''
Python is a versatile and powerful programming language that is widely used in 
various fields such as web development, data analysis, artificial intelligence,
 and automation. It is known for its simple and readable syntax, which makes it 
 an excellent choice for both beginners and experienced developers. Python's 
 extensive standard library and supportive community contribute to its popularity,
allowing developers to easily find resources and tools for their projects. Whether 
you're building a web application, analyzing data, or creating 
machine learning models, Python offers the flexibility and functionality
needed to accomplish your goals efficiently.

'''
print(str)
print(str1)

# print indexes of string----->>LIKE AN ARRAY OF CHARACTERS
print(name1[0])
print(name1[1])
print(name1[2])
print(name1[3])
print(name1[4])
print(name1[5])
print(name1[6])


# use for loop to print characters in string
for characters in str1:
    print(characters)