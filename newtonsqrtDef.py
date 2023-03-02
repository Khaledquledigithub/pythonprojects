def newton(num,tol):
	guess=num#initialize guess same with num
	attempt=0
	while True:
		attempt+=1
		root=0.5*(guess+(num/guess))
		if (abs(root-guess)<0.001):
			break
		else:
			guess=root#updating guess
			print("---------------------------------")
			print(f"Attempt {attempt}")
			print("guess :",guess)
	return root

print(newton(16,0.00001))
		