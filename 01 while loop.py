# While loop is a block of code that execute until a certain condition is met.


name=input("Enter ur name: ")
while name=="":
	#If this statement is True its continue to execte next line.Until name is not null which is False.
	name=input("Enter ur name: ")
print(f" Your name is {name}")

#Using Logical operator.

age=int(input("Enter ur age btw (1-100): "))

while age<1 or age>100:
 	print(f"given age {age} is invalid")
 	age=int(input("Enter ur age btw (1-100): "))
print(f" your age is {age}")
 
subject=input("Enter subject (press q to quint): ")
 	
while not subject=="q":
 	print(f"the subject is {subject} ")
 	subject=input("Enter subject (press q to quint): ")
 	
print("have a nice day")
 	
	
#Breaking while loop with a counter.
c=0
while True:
	#while block executed until condition are met.
	c+=1
	if c==10:#if c=10 while loop will break.
		break
	else:
		print(c)
x=10
y=10	
while x>0:
	x-=1
	while y>0:
		y-=1
		print("do sometging" ,end="-")
	print("about it",end="\t")