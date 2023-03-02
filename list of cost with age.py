while True:
	try:
		age=int(input("Enter age: "))
		cost1=0
		lst=[]
		lst1=[]
		if age<=2:
			cost1=cost1+0
		elif age>=3 and age<=12:
			cost1=cost1+14
		elif age<=65 and age>=15:
			cost1=cost1+18
		else:
			cost1=cost1+23
			
		lst1.append(age)
		lst.append(cost1)
		print("List of age: ",lst1)
		print("List of cost: ",lst)
		cost2=0
		while age!=0:
			age=int(input("Enter another age: "))
			if age==0:
				break
			if age<=2:
				cost2=cost2+0
			elif age>=3 and age<=12:
				cost2=cost2+14
			elif age<=65 and age>=15:
				cost2=cost2+18
			else:
				cost2=cost2+23
			lst.append(cost2)
			lst1.append(age)
			print("List of age: ",lst1)
			print("Total cost: ",lst)
			print("Total amount: ",sum(lst))
	except Exception as e:
		print(f"{e}")
	
