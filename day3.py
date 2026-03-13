#wap to accept percentage and if per>90 A ,per>=B,per>60>c fail
# per=int(input("enter percentage"))
# print(per)
# if per>+90:
#     print("A")
# elif per>=80:
#     print("B")
# elif per>=60:
#     print("C")
# else:
#     print("fail")       

#dict {key:value}parenthesis
#duplicate keys are not allowed
#duplicate values are allowed
#dict by nature it is growable
#it is mutable
#unordered data

# mydict={
#     "name":"khizra",
#     "professional":"student",
#     "id":1234
# }
# print(mydict)
# print(type(mydict))

# mydict={
#     101:"khizra",
#     102:"aditi",
#     "103":"neha",
#     "104":"vedika",
#     101:"sanika",
#     104:"isha"
# }
# print(mydict)

# a=mydict[102]
# print(a)

# mydict[102]="patel"
# print(mydict)

#only print key=0,1
# for x in mydict:
#     print(x)

# for x in mydict.values():
#     print(x)

#print key and value both
# for x,y in mydict.items():
#     print(x,y)

# mydict["modile_no"]=1234567
# print(mydict)

# mydict={
#     101:"khizra",
#     "professional":"student",
#     "id":1001
# }
# mydict.pop(101)
# print(mydict)

#string 
# name="khizraRaien"
# print(name[0])
# print(name[1])
# print(name[-1])
# print(name[0:5])
# print(name[1:])
# print(name[:5])
# print(name[:])
# print(name[1:8:2])
# print(name[::-1])


# s="help4code is a best platform for practicing programming"
# print(s.find("python"))#index=-1 because not prsent 
# #space ki bhi index hai
# print(s.find("help4code"))
# print(s.find("programming"))

# s="khizra","aditi","neha"
# m=' '.join(s)
# print(m)

# s="pyhton is a high level programming languague"
# print(s.lower())
# print(s.upper()
# print(s.swapcase())#upper to lower and lower to upper
# print(s.title())#first letter of each wordis cap
# print(s.capitalize())

# print('subject marks')
# phy=50
# chem=60
# math=70
# print("physics={} chemistry={} math={}".format(phy,chem,math))
# print("physics={0} chemistry={1} math={2}".format(phy,chem,math))
# print("physics={x} chemistry={y} math={z}".format(x=phy,y=chem,z=math))
# total=phy+chem+math
# print("total marks",f"{total}")
# print("roll no=","7".zfill(4))

# print('khizraraien44'.isalnum())#true
# print('khizraraien'.isalpha())#true
# print('44f'.isdigit())

# a=50
# b=30
# c=20
# d=10
# print((a+b)*c/d)
# print((a-b)*(c/d))
# print(a+(b*c)/d) 

# name="khizraraien"
# count=0
# count1=0
# for i in name:
#     if i=='a'or i=='e'or i=='i'or i=='u'or i=='o':
#         print("vowel")
#         count=count+1
#     else:
#         print("consonent")
#         count1=count1+1
# print(count)
# print(count1)

