#Collatz conjecture

choice=input("Type Yes to enter/ zero to quit: ").lower()
lst=list()
if choice=="yes":
	try:
		num=int(input("enter a num: "))
		if num<=0:
			quit()
		else:
			lst.append(num)
			print(lst)
			while num!=0:
				num=int(input("enter another num: "))
				lst.append(num)
				lst.sort()#Sorting the elements
				print(lst)

			
	except:
		print("Error please enter Positive value only")
for i in lst:
		if lst[-1]%2==0:
			last=lst[-1]
			print("Last element ",last)
			fl=last/2
			print("Floor duvision ,",fl)
			lst.append(fl)
			print(lst)
			quit()
else:
	last=lst[-1]
	print("last element,",last)
	add=(last*3)+1
	print("Additional element ",add)
	lst.append(add)
	print(lst)