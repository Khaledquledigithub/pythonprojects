#Slicing or Indexing =accessing elements of a sequence using [ ] indexing operator
#(start : end : step) its exclude the end element.

string="123-456-789"
print(string[0:3])
print(string[:3])
print(string[4:])

print(string[::2])#every 2nd element.

print(string[-4:])#last for elemt.

print(string[-1])#Last element

print(string[::-1])#print reverse string.