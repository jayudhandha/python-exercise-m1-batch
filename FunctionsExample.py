# Functions

# listA = [1,2,2,2,2,2,2,3,3,4,5,6]

# print(set(listA))

# Function defination
# Function body/suite
# Function call

# def greetings():
# 	print("Welcome to Vadodara..!!")


# for i in range(5):
# 	greetings()

# def sum(a,b):
# 	# print(a+b)
# 	return a+b

# c = sum(5,10)

# print(c)

########### Types of arguments in the functions ###########
# 1. required argument

# def msg(name):
# 	print("Hello",name)

# msg("Jayesh")
# msg() # Here this function will throw the error because we have not passed required arguments

# 2. Keyword arguments

# def specificMessage(age, name, msg):
# 	print(f"Hello {name} ({age}) Your message: {msg}")


# specificMessage("Elia", "Kem cho?")

# specificMessage("Kem cho?", "Elia")

# Whenever we use any keyword argument, after that all the remaining arguments should be keyword argument
# specificMessage(25, msg="Kem cho?", name="Elia")

# 3. Default arguments
# def userInfo(name, age=20):
# 	print(f"Hello {name}, You are {age} year old")

# userInfo("Jayesh")
# userInfo("Jayesh", 26)

# 4. Variable-length arguments

# def studentNames(*names):
# 	# print(type(names))
# 	print(names)

# studentNames("Jayesh", "Niki", "Rahi", "Elia")






