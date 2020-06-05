# File IO READ Operation

# fileObj = open('test1.txt', 'r')

# if fileObj:
#     print("File opened successfully")
# else:
#     print("Issue in opening file")

# print(fileObj.read())

# for line in fileObj:
#     print(line)

# print(fileObj.readline())

# We can modify the filePointer to read from perticular location


# File IO Write Operation
# We can use seek function to modify the file pointer position
# fileObj.seek(9) 

# print(fileObj.readline())

# We cna use tell function to get the current file pointer postion

# print(fileObj.tell())

# fileObj = open('test1.txt', 'w')

# fileObj = open('test1.txt', 'a')

# fileObj.write("\nAppend some more content...")

# fileObj = open('dummy.txt', 'x')

# fileObj.close()

# with statement is handling file closing operation automatically for us

with open('test.txt', 'r') as fileptr:
    print(fileptr.read())
    # fileptr.write("Elia is adding something...")
