d=dict()
for i in range(1,6):
	d[i]=i*i
print(d)
print(d.values())
s=0
for k,v in d.items():
	s+=v
print(s)
for k,v in d.items():
	if v%2==0:
		print(f"keys is: {k} and","value:",v)
day=dict(key="value",key2="value2")
print(day)
for i in d.keys():
	print(i,d[i])
for i in sorted(d, reverse=True):
	print(i,d[i])
	
x={y:y**2 for y in (1,2,3)}
print(x)
f=dict(a='apple',b=["banana","bro","baby"],c="carrot")
print(f)
s=input("enter str: ")
for k,v in f.items():
	if s in v:
		print(k)
	