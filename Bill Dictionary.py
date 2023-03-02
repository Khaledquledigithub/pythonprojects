bill={}
#Creating empty dictionary 
try:
	while True:
		new_bill=int(input("enter 0 to quit\ serial num: "))
		if new_bill==0:
			break #Escaping while loop.
		bill[new_bill]={}#Nested dict with new_bill as user key_value.
		items=input("Enter item: ")
		price=float(input("Enter price: "))
		quantity=int(input("Enter quantity: "))
		total=price*quantity #Multilplying price with quantity to get total value.
		bill[new_bill]["item"]=items
		bill[new_bill]["price"]=price
		bill[new_bill]["quantity"]=quantity
		bill[new_bill]["total"]=total
except Exception as e:
	print(f"{e}")
print(bill)
#Getting Total Amount of bill by using Function.
def Totalamount(dic, item):
 	amount=0
 	for k,v in bill.items():
 		amount=amount+v.get(item,0)
 	return amount
print("Total Amount: ",Totalamount(bill,"total"))

amounts=0
for k,v in bill.items():
	amounts=amounts+v.get("total",0)
print("Amountsss: ",amounts)
	
