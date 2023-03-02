#To show which triangle
s1=int(input("enter side1="))
s2=int(input("enter side2="))
s3=int(input("enter side3="))
if s1==s2 and s2==s3:
	print("EQUILATERAL TRIANGLE")
elif s1==s2 and s1!=s3 or s2==s3 and s2!=s1 or s1==s3 and s2!=s3 :
	print("ISOSLES TRIANGLR")
else :
	print("SCALANCE TRIANGLE")