"""to show the side of shape"""
sides=int(input("enter letter"))
if sides==3:
	print("triangle")
elif sides==4:
	print("square")
elif sides==5:
	print("pentagon")
else :
	print("input is invalid")