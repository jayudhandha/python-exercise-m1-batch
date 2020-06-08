print("Start...")

# a = 5
# try:
#     # Piece of code to be tested
#     print(a)
# except Exception:
#     # Piece of code to be executed when exception occurs
#     print("Exception handled...")

# a = 5
# b = 0

# try:
#     # print(a/b)
#     print(c)
# except ZeroDivisionError:
#     print("Zero Devision error, Please check the valud of b...")
# except NameError:
#     print("Please check that variable is defined or not...")

try:
    amount = int(input("Enter the amount: "))
    print(amount/10)
except Exception:
    print("Invalid Input...")

# Exception
print("End...")
