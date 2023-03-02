r=list()
num1=(" ","quit","no")
while True:
		try:
			num=input("enter num: ")
			num=int(num)
			if type(num)==int:
				r.append(num)
				r.sort()
				
				print("space/no/quit to quit")
				

		
		except Exception as e:
			print(f"{e}")
		if num in num1:
			break
print('-----------------------------------------------------------------')
print("The list: ",r)
length=len(r)
if length%2==0:
		median1=r[length//2]
		median2=r[length//2-1]
		median=(median1+median2)/2
		print("Length of the list is even: ",length)
		print("-----------------------------------------------------------")
		print("& median :",median)
else:
		median=r[length//2]
		print("Length of the list is odd:",length)
		print("---------------------------------------------------------")
		print("& median: ",median)
		
	