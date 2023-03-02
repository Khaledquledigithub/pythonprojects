n=int(input("Enter="))
s=[]
for i in range(1,n+1):
		if n%i==0:
			print(i)
			if i!=n:
				s.append(i)
print(s)
if sum(s)==n:
	print("The num is perfect")
else:
	print("Not a perfect num")