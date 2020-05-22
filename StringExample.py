# name = "kod factory"

# Finding character
# Length
# Concate
# Vowels
# Indexing / slicing
# convert to upper / lower case

# print(name.index('f'))

# print(name.upper())
# print(name.lower())

# print(name.title())

# print(name.capitalize())

# German letter ß is equivalent to ss so you can compare that as well.

# firstString = "der Fluß"
# secondString = "der Fluss"

# # caseless compare
# # ß is equivalent to ss
# if firstString.casefold() == secondString.casefold():
#     print('The strings are equal.')
# else:
#     print('The strings are not equal.')

# S = 'Das straße'
# x = S.casefold()
# print(x)
# a = 'kodß'
# b = 'kodss'

# print(a.casefold() == b.casefold())

# print(len(name))

# in operator (membership operator)

# if 'o' in name:
#     print('character exist')
# else:
#     print("character doesn't exist")

# name = "kod factory"

# Slicing
# print(name[2:7])

# print(name[4:])

# print(name[:6])

# print(name[:])

# print(name[-3 : -1])

#### String operators
# %, in / not in, +, r/R

# firstName = "Jayesh"
# lastName = "Dhandha"

# print(firstName + lastName)

# print("Hello\nWorld")

# \n is used to print the new line

# print("\\n is used to print the new line")

# path = r"C:\Users\Kod Factory\Desktop\Desktop Backup\PythonExercise\newfolder\test.txt"

# it will escape the special characters like \n, \t etc
# print(r"\n is used to print the new line \n")

name1 = 'Elia otito'
name2 = 'James otitos'

# print(name1.endswith('otito'))
# print(name2.endswith('otito'))

# print(name1.startswith('Elia'))
# print(name2.startswith('ames'))

# a = '   hellow how are   '

# print(a.strip())

# print(a.rstrip() +'*')

# print(a.lstrip() +'*')

# password = '1234'

# print(password.isalnum())
# print(password.isnumeric())

# message = "Welcome"

# print(message.center(50, '*'))

# print(message.rjust(30, '*'))

# print(message.ljust(30, '*'))

userInput = "jayesh,nikita,kodfactory"

print(userInput.split(","))

# print(userInput.split(",")[1])
