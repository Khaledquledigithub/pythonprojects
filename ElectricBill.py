#Electricity bill

unit=int(input("Enter units: " ))
if unit==100: 
#first 100unit free
	print("its free of cost")
elif unit<201 and unit>100:
	amt=(100*0)+(uni-100)*5
#next 100 unit charge 5Rs.
	print("amount: ",amt)
elif unit>201:
#After 200unit its charge 10Rs.
	amt1=(100*0)+(200-100)*5+(unit-200)*10
	print("amount: ",amt1)
	