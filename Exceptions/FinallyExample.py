# a = 5

# try:
#     print(c)
# except Exception:
#     print("Exception..")
# # Finally block will be always executed whether exception occurs or not
# # All the cleanup code is being used in finally
# finally:
#     print("Finally...")

# name = 'Jayesh'
# try:
#     print(names)
# except Exception:
#     print("Exception...")
# # This else block will be executed only when we don't have any exception
# else:
#     print("Else block executed...")


# def div(a,b):
#     try:
#         return a/b
#     except Exception:
#         print("Exception...")
#     finally:
#         print("Finally block...")

# print(div(10,5))


try:  
    age = int(input("Enter the age?"))  
    if age<18:  
        raise ValueError;
    else:
        print("You can vote!")

except ValueError:  
    print("You are not allowed to vote...")  