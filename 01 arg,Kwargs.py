# *args          =allows u to pass multiple non-
#                        key arguments.It take argm as        #                          tuples.
# **kwargs   =allow u to pass multiple keyword                                 argument.Its take argm as dict.

# ARBITRARY ARGUMENTS.
def arg(*args):
	print("the type of arg is ",type(args))
	# here the type of argument is a tuple.
arg()	

def add(*arg):
	count=0
	for x in arg:
		count+=x
	return count
	
print(add(1,2,3))

#KEYWORD ARGUMENT

def paste(**kwargs):
	for k,v in kwargs.items():
		print(f"key is {k} and value is {v}")
	if "area" not in kwargs:
		print("area is not available")
		print(f"{kwargs.get('locality')}")
		
	
	
paste(city="xyz",pincode="5xxxxxxx5")