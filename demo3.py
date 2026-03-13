#wap for simple interest
# principal=100000
# roi= 10
# time =1
# si=(principal*roi*time)/100
# print("simple interest =",si)
# wap to accept c temp into far temp
# c=110
# f=(9/5*c)-32
# print(f)

#swapping of two number
# val1=input("enter no 1 ")
# val2=input("enter no 2" )
# temp=val1
# val1=val2
# val2=temp
# print(val1)
# print(val2)
# a=int(input("enter val"))
# b=int(input("enter val"))
# a=a+b #(100+200=300 // a=300)
# b=a-b  #(300-200=100 ///b=100)
# a=a-b # (300-100=200 // a=200)
# print(a)
# print(b)

# height=float(input("enter h")) 
# inch=height*12
# cm=inch*2.54
# print(inch)
# print(cm)

# reverse num 
# num=123
# a=num %10
# num=num // 10 # float division num =12
# b=num % 10 
# c= num //10 # num=1
# rev= a*100 + b*10 + c*1 # 300+200+1
# print(rev)

# num=1234567
# rev=0
# for num in range(7):
#     lastdig=num%10
#     rev=rev*10+lastdig
#     num=num//10
# print(rev)    

mylist=[ "prashant", 77 ,60.52,"beta","baap",6,10,5,"aditi","khizra"]
# print(mylist)
# print(type(mylist))
# print(mylist[0])

# print(mylist[-1])
# print(mylist[2:5])

# print(mylist[:])
# print(mylist[1:2:5])
# print(mylist[::-1])
# print(mylist[1:8:2])# 1 is start pt 8 is end pt 2 is the increment pt 
# mylist.append('isha')
# mylist.append("vedika")
# print(mylist)
#particular index mai insert kar na 
# mylist.insert(1,"sanika")# 1 is the index insert use to replace the value
# print(mylist)
# mylist.remove("baap")
# print(mylist)
#clone of array
# newlist=mylist.copy() #cloning
# print(mylist)
# print(newlist)


#nested list 
# mylist=[['khizra','aditi'],['38','25'],['440022',"yyyy"]]
# print(mylist[0][0])
# print(mylist[2][1])
# #print(mylist[row][cols])
# print(mylist[1][0])

# list1=["khizra","aditi"]
# print(list1*2)#it  will print two times

# list2=[50,25.50]
# print(list1+list2)

# list2=[50,25.50,"khizra"] # delete specific index using del
# del list2[2]
# print(list2)

# del list2
# print(list2)# the list2 is delete so we can't print it it show error


#clear function is used to clear the value int the list they dont delete the list 

# list2=[50,25.50,"khizra"]
# list2.clear()
# print(list2)

# name="khizra" #str
# print(name)
# myname=list(name)#typecasting
# print(myname)

#sorting example
# mylist=[44,22,77,0,9,88]
# #reverse=True it print in decreasing 
# mylist.sort(reverse=True)
# #mylist.sort()#ascending
# print(mylist)
#default sorting order for number is ascending order
#default sorting order for string is alphabetical order
#we should khow that the list shold contain homogenious
#data othewrwise we will get typerror


# math=10
# phy=10
# eng=20
# print(id(math))# id function is used to return the address of variable
# print(id(phy))
# print(id(eng))
# #interpreted check the value is exist or not 


# mylist=[44,22,77,0,9,88]
# newlist=mylist#alising if we change in any of the list it will reflect in other list
# print(id(mylist))
# print(id(newlist))
#alising means assigning one variable reference 


#looping
#there ar 2 type of operator in  py 1 memebership operator is me bhi 2 type hai
#1 in & 2 not in 
# name="khizra"
# print('z' in name)
# print('b'in name)
# print('b' not in name)


# for i in range(6):
#     print(i)
#     #i=0,1 2 3 4 5 

# for i in range(2,6):
#     print(i)

# for i in range(1,10,2):
#     print(i)

# for i in range(5,0,-1):
#     print(i)
    
# for i in range(1,11):
#     print(i*2)

# for i in range(1,11):
#     print(i*2," ",i*3," ",i*4," " ,i*5," ")
# print()
# for i in range(1,11):
#     print(i*11," ",i*12," ", i*13," ",i*14," ")

# no= int(input("enter any digit"))
# if no>0:
#     print('positive')
# if no<0:
#     print('negative')
# if no==0:
#     print('zero')

#wap to accept days and check the working day and weekend

# day=input("enter the day : ")
# if day=="sunday"or "SUNDAY" or "saturday" or "SATURDAY":
#     print("weekend")
# else:
#     print("working day")

#wap to accept 3 paper marks and calculate total,% ,and if percentsge is greater than or equal to 60 then he/she is eligible for placement

# no1= int(input("enter any marks "))
# no2= int(input("enter any marks "))
# no3= int(input("enter any marks "))
# total=no1+no2+no3
# print(total)
# per=(total/300)*100
# print(per)
# if per>=60:
#     print("eligible for placement")
# else:
#     print("not eligible")

#wap to accept five different value in 5 different var and check max value and print by using simple if statement 

no1= int(input("enter any marks "))
no2= int(input("enter any marks "))
no3= int(input("enter any marks "))
no4= int(input("enter any marks "))
no5= int(input("enter any marks "))

