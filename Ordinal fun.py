##ordinal

def num(a):
	lst1=[1,2,3,4,5,6,7,8,9,10,11,12]
	lst2=["first","second","third","fourth","fifth","sixth","seven","eight","nineth","ten","eleven","twelve"]
	if a in lst1:
		b=lst1.index(a)
		print(lst2[b])
x=int(input("enter"))
num(x)
