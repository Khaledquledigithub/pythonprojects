n=int(input("enter value="))
s=[]
s.append(n)
while n>=1:
	n=int(input("another value="))
	if n!=0:
		s.append(n)
s.sort(reverse=True)
print(s)