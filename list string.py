
"""We are giving string input and it will show given input only once"""

n=input("enter value=")
s=[]
s.append(n)
while n!=" ":
	n=input("another value=")
	if n!=" ":
		if n not in s:
			s.append(n)
print(s)