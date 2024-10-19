# List Method
# List.Sort()
list=[1,2,34,3,54,8,0]
list.sort()

l=["Mango","Orange","Watermelon","Apple"]
l.sort()
print(l)

# Desending Sorting
list=[1,2,34,3,54,8,0]
list.sort(reverse=True)
print(list)

# Reverse()
# It reverse the pattern
l.reverse()
print(l)

# index
print(l.index("Mango"))

# Count()
# it check how many times the given element is present in list
print(list.count(2))

# Copy()
# m=list.copy()
# m[0]=11
# print(m)

# Insert
list.insert(2,32)
print(list)

# Extend
# Add other list at the end of the previous list
li=[12,30,60,80,45]
# list.extend(li)
# print(list)


# Concatenate Two Lists
k=list+li
print(k)
