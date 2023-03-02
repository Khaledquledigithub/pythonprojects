#Creating a List of Prime num

num =int(input("Enter range from 2: "))
lt= [ ]

# Putting prime num in empty List
for i in range(2,num+1):
	for j in range(2,i):
		if i%j==0:
			break
	else:
		lt.append(i)

#Printing List
print("Prime num are: ",lt)

		