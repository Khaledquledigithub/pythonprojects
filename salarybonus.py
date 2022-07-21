#salary with bonus
salary=int(input("enter salary="))
exp=int(input("enter years="))
if exp> 10:
	net=(salary/100)*10 #bonus= salary×0.1
	print("Net bonus=",net)
elif exp>=6 and exp<10:
	net=(salary/100)*8 
	print("Net bonus",net)
else :
	net=(salary/100)*5
	print("Net bonus",net)