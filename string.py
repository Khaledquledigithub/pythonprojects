
x="string is here"
print("Printing ever 2nd char: ",x[::2])
print("Printing char in reverse: ",x[::-1])#Reverse 
print("Length of str: ",len(x))
#Checking elemenet in str.
if "is" in x:
	print("its there")
else:
	print("not in string")

#Function in str.
#------------------------------------‐-3	
print(x.replace(" ",""))#removing spaces
print("Length without spaces: ",len(x.replace(" ","")))
print("".join(x.split()))
print(x.strip())#strip used to remove front n back spaces.

print("x befor upper: ",x)
print("x befor upper: ",x.upper())#Uppercase
print("x in a list: ",x.split())#convert elemt into List.
print(x.capitalize())#first alpha to uppercase.
print(x.find("e"))#find the index  alphabet.
print(x.rfind("e"))


