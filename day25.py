# operations on tuple...
'''
You can not change and add new things in tuple 
tuples are immutable 
if you want to add,remove and change items in tuple then first you convert 
it into list and perform some operation on list then you convert back it into 
tuple '~' (simple haha)
'''
countries=("Spain","Italy","India","Europe","Germany")
temp=list(countries)     #---->make temp list & convert tuple into list
temp.append("Russia")    #---->Add item in list
temp.pop(3)              #---->Remove item in list
temp[2]="Finland"        #---->Change item
countries=tuple(temp)
print(countries)

#Count maethod:
#check how many time a number occur in tuple
tuple1=(0,1,2,3,4,3,1,3,2,1,2,3)
res=tuple1.count(3)
print('Count of 3 in Tuple 1 is :',res)
res=len(tuple1)

#index maethod:
#it return the first occurences of the given element from the tuple
#tuple.index(element,start,end)
tuple1.index(3)
print('index of 3 in Tuple 1 is :',res)