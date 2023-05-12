#default arguments = A default value for certain
#                                       parameters, default is use
#                                      when that arg is omitted
#it is used ro make function flexible, reduce of arg

def percentage(number,total):
	return (number/total)*100
	
print(percentage(485,600))

def percentage(number,total=600):
	#total can be add as default value.
	#we can change total by passing arg value.
	return (number/total)*100
print(percentage(485))


#keyword argument =  an argument preceded by #                identifier help with readability.Order of #                 argument matter.it follow positional arg.

def detail(sir,first, last,):
	print(f"{first} {last} u r a {sir}.")
	
detail(first='bob',last='builder',sir='male')


