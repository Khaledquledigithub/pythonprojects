#Electric bill
unit=int(input("enter unit value="))
if unit<=100:
	print("0")
elif unit>100 and unit<=200:
	bill=5*(unit-100)
	print("total bill=",bill)
else:
	bill=10*(unit-200)+5*(100)
	print("total bill=",bill)