while True:
	try:
		print("Press 1 for circle")
		num=int(input("enter num of sides: "))
	
		if num==1:
			r=int(input("enter radius: "))
			area=3.14*(r**2)
			print("Area of circle: ",area)
		if num==3:
			height=int(input("enter height: "))
			length=int(input("enter length: "))
			area=1/2*(length*height)
			print("Area of triangle :",area)
		elif num==4:
			print("If all sides are equal :")
			print("1.Square .\n2.Rectangle.\n3.Parallogram. \n4.Trapezoid.\n5.Rhombus")
		q1=int(input("enter option: "))
		if q1==1:
			side=int(input("Enter sides of squar: "))
			area=side**2
			print("Area of square: ",area)
		elif q1==2 or q1==3:
			side1=int(input("enter length: "))
			side2=int(input("enter width: "))
			area=(side1*side2)
			print(f"Area of parallelogram: ",area)
			
		elif q1==4:
			s=int(input("enter length= "))
			h=int(input("enter height= "))
			w=int(input("enter width="))
			area=((s+w)/2)*h
			print(f"Area of Trapezoid: ",area)
		elif q1==5:
			s=int(input("enter length: "))
			h=int(input("enter height: "))
			area=(s*h)/2
			print("Area of Rhombus: ",area)
		
			
	except Exception as e:
		print(f"{e}")