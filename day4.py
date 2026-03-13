
# i = 1 
# while i<=5: 
#     print(i)
#     i = i+1
# username = ""
# password = ""
# while username != "admin" and password != "hello":
#     username = str(input("enter username"))
#     password = str(input("enter password"))
# n = int(input("Enter num: "))
# sum = 0
# i = 1

# while i <= n:
#     sum = sum + i
#     i = i + 1

# print("Sum of first", n, "numbers is", sum)/

#              removing same characters from a string 
# name = "prashant"
# newname = ""

# for ch in name:
#     if ch not in newname:
#         newname += ch

# print( name)
# print( newname)
#            revesrse the string using loop (for / while )     print(name[::-1])
# name = "prashant"
# namerev = ""
# # using for loop
# i = len(name) - 1   # start from last index
# while i >= 0:
#     namerev = namerev + name[i]
#     i = i - 1

# print("Reversed string:", namerev)

# name = "prashant"
# rev = ""

# for ch in name:
#     rev = ch + rev   # add character in front

# print("Reversed string:", rev)
# mycart = [10,20,2000,50,65,5,558]
# for i in mycart:
#     # if i in mycart:
#     if  i>400:     
#         print("h'ojfg")
#         continue
#     print(i)
# name = "palindrom syndrome"
# strrev = ""
# for ch in name:
#     strrev = ch + strrev 

# if name == name[::-1] :   
#     print("yes")
# else: 
# name1 = "listen"
# name2 = "silent"

# if len(name1) == len(name2):
#     for ch in name1:
#         if name1.count(ch) != name2.count(ch):
#             print("Not anagrams")
#             break
#     else:
#         print("They are anagrams")
# else:
#     print("Not anagrams")
# #     print("no")   
    # checking if ther string in anagram (does the words use the same lettetrs in the string )
# name1 = "listen"
# name2 = "silent"
# if len(name1) == len(name2):
#     for ch in name1:
#         if name1.count(ch) != name2.count(ch):
#             print("Not anagrams")
#             break
#     else:
#         print("They are anagrams")
# else:
#     print("Not anagrams")
#    function to add key value pain into dictionart use pop or del mstatement
# create empty dictionary
# mydict = {}

# mydict["name"] = "Prashant"
# mydict["age"] = 25
# print("After adding:", mydict)

# mydict.pop("age")
# print("After pop:", mydict)

# del mydict["name"]
# print("After del:", mydict)

# for i in range(1,4):
#     for j in range(1,4):
#         print(i, end="")
#     print()
# n=int(input("enter num of rows"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i),end = "")
#     print()

# n=int(input("enter num of rows"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#          print((n+1-i),end ="")
#     print()
n=int(input("enter num of rows"))
for i in range(1,n+1):
    for j in range(1,n+2-i):
         print("*",end ="")
    print()
