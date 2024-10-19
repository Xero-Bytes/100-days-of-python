# Tuple In python
# we cannot change tuple,ordered collections of data items
tup=(1,2,3,"Apple")
print(type(tup),tup)
print(len(tup))
# tup[0]=40        <-----Error    we can't do this b/c tuple elements are unchangeable
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[-1])
if 3 in tup:
    print("Yes 3 is present in tuple ")
    tup2=tup[1:3]    #Slicing   
print(tup2)