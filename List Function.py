
#Assigning value to empty list.

y="apple,banana,grape,pineapple"
list1=list(y.split(","))
print(list1)

#Assigning new value apple to peach.
list1[0] = "peach"
list1.insert(2,"plum") #Using insert(index,value).
list1.append("melon")#add element at last.
list1.extend(["mango"])
print(list1)

#Iterating a list
for i in list1:
	print(i)
print("--------------------")
for x in list1:
	x=x.title()
	print(x)
print("------------------------")
for y in list1:
		y=y.upper()
		print(y)
		
#Removing elements .
list1.pop()#Remove last element.
list1.remove("grape")#Remove using name.
list1.remove(list1[0])#Remove using index
print(list1)

#Counting elements.
print("apple in list: ",list1.count("apple"))
print("banana in list:",list1.count("banana"))
print("Slicing: ",list1[0][0:3])
print(print(list1),"elements in list:",len(list1))

