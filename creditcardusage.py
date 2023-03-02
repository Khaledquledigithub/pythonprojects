#credit card user
credit=int(input("enter num of card"))
if credit<=23:
	print("student=freshmen")
elif credit >=24 and credit<=53:
	print("sophomore")
elif credit>=54 and credit <=83:
	print("junior")
else:
	print("senior")