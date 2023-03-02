str1=input("Enter a string without spaces: ")
vowels=("a","e","i","o","u")
for i in str1:
	if i in vowels:
		print(f"The vowels are {i} at index: ",str1.index(i))
	else:
		print("No vowels")
		
#Another method.

for i in str1:
	if i=="a" or i=="e" or i=="o" or i=="u":
		print(f"the alphabet {i} is vowel")
	else:
		print(f"{i} is not a vowel")
	