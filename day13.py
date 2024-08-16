''' Strings Methods in Python
---->Python provide a set of built-in methods that we can use to alter and modify the strings
strings are immutable once we made a string we cannot change it when we use these built-in methods we made
a copy of string which is changaable.
1--->upper()
the upper() method convert a string to upper case 
str1="abbcdefghi"
print(str1.upper())
2--->lower()
the lower() method convert a string to lower case 
str2="ABCDEF"
print(str1.lower())
3--->Strip()
the strip() method remove any white spaces before and after the string
str3="Silver Spoon"
print(str.strip())
4--->rstrip()
the rstrip() removes any triling characters
str4="hello11!!!!!!!!!!!!!!"
print(str4.rstrip("!))
5--->Replace()
replace() method replace all occurences of a string with another string.
str5="Silver Spoon"
print(str5.replace("Sp","m"))
6--->split()
split() method split the given string at the specified instance and returns 
the seperated  strings as list item
str6="Silver Spoon"
print(str6.split(" "))
7--->capitilize()
str7=capitilize() method turns only  the first character of the string to uppercase and 
the rest other character of the string turns to lowercase.the string has no effect
 if the first character is already capital
 str7="hello"
 capstr7=str7.capitilize()
 print(capstr7)
8--->center()
the center method alligns the string to center  as per the parameters given by user
str8="Welcome to the console!"
print(str8.center(50))
9--->Count()
the count() method returns the number of times the given value has occered within the 
given string.
str9="Abracadabra"
str=str9.count("a)
print(str)
10--->endswith()
endswith() method checks if the given string end with a given value.if yes return
 true,then false.
str10="Welcome to the console!!!"
print(str10.endswith("!")) We csn also check a value in-between the strings by 
providing
start and end index position.
 str10="Welcome to the console!!!"
print(str10.endswith("to" ,4,10))
11--->find() if string which we want to find not present it return -1 
12--->index()same function just like find() method but if string which
 we want to find not present it return error 
13--->isalnum() A-Z a-z 0-9(string consist of numbers and alphabets)
14--->isalpha() only(A-Z a-z)if any number or punctuation it return false
15--->islower() return true if all the letters in the strings are in lower
case
16--->isprintable()if all the values within the strings are printable it
 return true.
17--->isspace() it return true only when the strings contain white spaces
 if not it return false.
18--->istitle()return true if only the first letter of each word of string is 
capitilized.
19--->isupper() all words in strings are in upper case then it return true.
20--->startswith() return true if the string starts with a given value.
21--->swapcase() changes the character casing of the string .upper case changes
into lower and lower case changes into upper. 
22--->title() capitilize each letter of the word in string.
'''

a="taqdees Fatima"
print(len(a))
print(a.upper())
print("----------------------------------------------------")
b="TAQDEES BUKHARI"
print(len(b))
print(b.lower())
print("----------------------------------------------------")
c="   Cyber Security    "
print(len(c))
print(c.strip())
print("----------------------------------------------------")
# for both leading and triling
d="!!!!!!!!!i love to solve CTF challenges!!!!!!!!!!!!!!"
print(len(d))
print(d.strip("!"))
print("----------------------------------------------------")
# just for triling its not remove leading
d="!!!!!!!!!i love to solve CTF challenges!!!!!!!!!!!!!!"
print(len(d))
print(d.rstrip("!"))
print("----------------------------------------------------")
e="Taqdees Fatima"
print(len(e))
print(e.replace("Fatima","Bukhari"))
print("----------------------------------------------------")
f="I love cyber security"
print(len(f))
print(f.split(" "))
print("----------------------------------------------------")
g="""capitilize() method turns only  the first character of the string to uppercase and 
the rest other character of the string turns to lowercase.the string has no effect
 if the first character is already capital"""
print(len(g))
print(g.capitalize())
print("----------------------------------------------------")
h="Welcome to the python 100 days of course!"
print(len(h))
print(len(h.center(60)))
print("----------------------------------------------------")
i="Taqdees Bukhari"
strcount=i.count("a")
print(strcount)
print("----------------------------------------------------")
j="Welcome to the visual studio!!!"
print(j.endswith("."))
print(j.endswith("!"))
j="Welcome to the visual studio!!!"
print(j.endswith("to",6,10))
print("----------------------------------------------------")