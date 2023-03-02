#Newton sqrt Method
try:
	num=int(input("enter num: "))
	attempt=0
	guess=num
	while True:
		attempt+=1
		root=0.5*(guess+(num/guess))
		if abs(root-guess)<0.001:
			print(f"Attempt: {attempt}")
			print(f"Root of {num} : ",root)
			break
		else:
			guess=root
			print(f"Attempt: {attempt}")
			print(f"Root of {num} : ",root)
except Exception as e:
	print(f"{e}")