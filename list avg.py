d=int(input("enter vqlue="))
s=[]
s.append(d)
while d>=1:
	d=int(input("enter another value="))
	if d!=0:
		s.append(d)
print(s)
l=len(s)
#print the length of the string:
print("lengthof string=",l)
#print the sum of the elements:
tally=sum(s)
print("sum of list=",tally)
#Taking the avg of the elements
avg=tally/l
print("Avg=",avg)