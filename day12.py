# STRING SLICING
# Length of a string -----> we can find length of string using length function  ---->len()

fruit="mango"
len1=len(fruit)
print("mango is a ",len1,"letter word.")

names="Harry,Rohan"
print(len(names))

# String as an array
'''
string as an essentially sequence of characters also called an array.thus we can access
the element of this array.    
'''
# last index of strin is excluded for example if we have a "Apple" its length is 5 but when we print it indexes its
# starting with 0 which is including and end at 5 but 5 is excluded
pie="ApplePie"
print(pie[6])
print(pie[0:5])

name="Taqdees"
print(len(name))
print(name[:7])

password="qwerty"
print(len(password))
print(password[:])

university="kingAbdullah"
print(len(university))
print(university[0:-8])
print(university[0:len(university)-8])
print(university[len(university) -8:len(university) -3])
print(university[-8:-3])
# print(university[-3:-8]) -----> Throw an error because it is not a valid !
nm ="Harry"
print(nm[len(nm) - 4:len(nm) - 2])
print(nm[-4:-2])

# Loop Through A String
# strings are array and arrays are iterable.Thus we can loop through strings
 
Alphabets = "ABCDE"
for i in Alphabets:
    print(i)

    
  