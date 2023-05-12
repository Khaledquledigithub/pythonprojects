for i in range(0,11):
	#range btw 1 & 10, 11 is exclude.
	print(i)

count=0#Counting variable for Tally.
for i in range(0,10):
	count+=1
	print("count= ",count, "i : ",i)	


#Nested loop.

print("----------------------------")

for x in range(3):#outer loop.
#execute inner loop 3 times.Rows
	for y in range(1,10):# inner loop.
	#inner loop execute first.Columns
		print(y,end="-")
		# end is used print on a same line.
	print()#outer print used to new line.