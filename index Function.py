def num(a):
	list1=[1,2,3,4]
	list2=["one","two","three","four"]
	if a in list1:
		b=list1.index(a)
		print(f"   {a} :",list2[b])

num(4)