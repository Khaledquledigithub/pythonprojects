import random
variable_list = [5, "string", 1.4,6]

for number in variable_list:
    try:
        range_list = list(range(number))
        print(number, "-", range_list)

    except:
        print(number, "- not an integer")
        
