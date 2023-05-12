#function = A block of reusable code
#                    place () after the function to invoke

def greeting():
	print("Goodmorning ")
	
greeting()

def greeting1(x):
	print(f"Goodmorning {x} ")
	
greeting1("sir")
greeting1("madam")

#Return = statement used to end a function 
#                and send result back to caller.

def add(x,y ):
	z=x+y
	return z
	
print("   ",add(1,2))

def fullname(first, last):#position should be same.
	return first+" "+last
	
print("bro","code")