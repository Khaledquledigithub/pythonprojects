above=int(input("Enter amount: "))
below=int(input("Enter amount: "))
refund=(above*0.25)+(below*0.10)
print("total: ",refund)
#Using a Dictiionary.
x={}
big=int(input("enter num of big bottle: "))
small=int(input("enter num small bottle: "))
x["Big"]=big
x["Small"]=small
print(x)
total=0
amt1=0
amt2=0

for k,v in x.items():
	if k=="Big":
		amt1=0.25*v
	elif k=="Small":
		amt2=0.10*v
		total=amt1+amt2
print("Total amount: ",total)