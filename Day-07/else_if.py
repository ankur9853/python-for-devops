import sys

#type_of_day = sys.argv[0]

type_of_day = sys.argv[1]

if type_of_day == "weekday":
    print("Go to work and keep learning")
elif type_of_day == "weekend":
    print("learn and code and spend time with family")   
else:
    print("Invalid input")