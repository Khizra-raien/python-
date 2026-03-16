#function
# def msg(): #called function
#     print("hello patel")
#     n1=int(input("enter no"))
#     n2=int(input("enter no"))
#     print("ADD=",n1+n1)
# msg()
# 2 type fuct 1. pre defined 2. user defined 

#how to return multiple value
# def calculation():
#     n1=int(input("enter no"))
#     n2=int(input("enter no"))
#     sum=n1+n2
#     mul=n1*n2
#     div=n1/n2
#     sub=n1-n2
#     return sum ,mul ,div, sub
# result=calculation()
# print(result)

# py pass 4 types of argument we can pass
#1.positional argument
#2. keyword   3.default   4. variable length argument / variable number of argument 


# def personalInfo(fname,lname):
#     print("first name ",fname)
#     print("last name ",lname)
# personalInfo("khizra","raien")    

#1.positonal 
# def personalInfo(fname,lname):
#     print("first name ",fname)
#     print("last name ",lname)
# fname="khizra"
# lname="raien"
# personalInfo("fname","lname")

#2. default argument
# def cityName(city="delhi"):
#     print(city)
# cityName("mumbai")
# cityName("Nagpur")
# cityName()

#variable length argument
# def studentName(*name):
#     print(name)
# studentName("khizra","aditi","patel")

# mylist=[5,2,3,9,7]
# def searchElement():
#     for i in range(len(mylist)):
#         print(mylist[i])
# searchElement(7)

# mylist = [5,2,9,7,5,6]
# def searchElement(target):
# for i in range(len(mylist)):
#    if target == mylist[i]:
#       print("elemrny at index " , i)
# searchElement(7)


def searchElement(target):
    for i in range(len(mylist)):
        if target== mylist[i]:
            return i
    return -1
result = searchElement(10)
if result!=-1:
    print("element found at index",result)
else:
    print("element not found",result)

mylist=[2,4,5,6,7,8]
searchElement(mylist)
