# Inline function, 

# def sum(a,b):
#     return a+b

# function called
# Execution
# It returns some value

# x = lambda a,b : a+b

# print(x(10,20))
# def mul(a):
#     return lambda n : a*n
#     # return lambda n : 5*2

# no = 5
# x = mul(no)

# for i in range(1,11):
#     # print(f" {no} x {i} = {no}*{i}")
#     print(f" {no} x {i} =",x(i))

# Filter

listA = [1,2,3,4,5,6,7,8,9]

# listB = list(filter(lambda x: x%2 != 0, listA))

listB = list(filter(lambda x: x%3 == 0, listA))

# print(listB)

# listB = list(map(lambda x: x**2 , listA))

print(listB)