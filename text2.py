# # # num1= int (input("enter number 1  : "))
# # # num2= int (input("Enter number 2  : "))
# # # print(num1+num2)
# # # print(num1//num2)
# # # print(num1**num2)
# # # print(num1-num2)
# # # print(num1*num2)
# # # print(num1/num2)
# # # print("Number 1 and 2 are respectively",num1,num2)
# # # temp = num1
# # # num1=num2
# # # num2=temp 
# # # del(temp)
# # # print("Number 1 and 2 are respectively",num1,num2)
# # # num1,num2=num2,num1
# # # print("Number 1 and 2 are respectively",num1,num2)
# # # x=1,2,3,4,5,6,7
# # # print(type(x))
# # # c=2+3j
# # # print(type(c))
# # # z= int (input("Enter number   : "))
# # # for i in range(1,11,1):
# # #     print(z,"x",i,"=",z*i)
# # #     print(f"{z}x{i}={z*i}")
# # # k=int (input("enter number"))
# # # for i in range(1,k+1):
# # #     for j in range(1,i+1):
# # #         print(j,end=" ")
# # #     print()
# # # 
# # # x=int(input("enter number"))
# # # rows=x
# # # for i in range (1,x+1):
# # #     print(" "*(rows-i)+ "i+1"* i)
# # # x=[1,2,3,4,5]
# # # for i in x:
# # #     print(i)
# # # y=int(input("Enter a number: "))
# # # for i in range(1,y+1):
# # #     for j in range(y-i):
# # #         print(" ",end=" ")
# # #     for k in range(1,i+1):
# # #         print(k,end="   ")
# # #     print()
# # # x=int(input("enter number: "))
# # # i=1
# # # while(i<11):
# # #      print(f"{x}x{i}={x*i}")
# # #      i=i+1
# # # a=int(input("Enter a number: "))
# # # i=1
# # # while i<11:
# # #     if i==5:
# # #         i=i+1
# # #         continue
# # #     else:
# # #         print(f"{i}x{a}={i*a}")
# # #         i+=1
# # # b=int(input("Enter a number: "))
# # # # 
# # # if b!=0:
# # #     if b>0:
# # #         print("Number is positive")
# # #     if b<0:
# # #         print("Number is Negative")
# # # else:
# # #     print("Number is 0")
# # # x= input("Enter string: ")
# # # rev=""
# # # for i in x:
# # #     rev=i+rev
# # # # print(rev)
# # # x=input("enter string: ")
# # # y=input("Enter string2: ")
# # # # print(x+y)
# # # # print(x*5)
# # # # print(len(x))

# # # # print(x.upper())
# # # # print(y.lower())
# # # # print(x.title())
# # # # print(y.capitalize())
# # # # print(y.swapcase())
# # # # print(y.find("t"))
# # # # print(y.index("S"))
# # # # print(x.count("a"))
# # # # print(x.startswith("sa"))
# # # # print(y.endswith("ng"))
# # # print(x.replace("s","S"))
# # # print(x.strip())
# # # print(x.split(" "))
# # # print(x.join('-'))
# # # a=[1,2,3,4,5]
# # # a.append(6)
# # # print(a)
# # # a.extend([7,8,9])
# # # print(a)
# # # print(len(a))
# # # print(a[0:2])
# # # print(a+[10,11])
# # # num=int(input("Enter the Number: "))
# # # rev=0
# # # while num>0:
# # #     x=num%10
# # #     rev=rev*10+x
# # #     num=num//10
# # # print(rev)
# # # 
# # # a=[1,2,3,4,5,6]
# # # print(a.index(3))
# # # print(a.count(6))
# # # print(2 in a)
# # # n=int(input("enter the size of list: "))
# # # l=[]
# # # t=[]
# # # for i in range(n):
# # #     x=int(input(f"enter the value of{i}"))
# # #     l.append(x)
# # # print(l)

# # # for i in range(n):
# # #     for i in range(n-1): 
# # #         if l[i]>l[i+1]:
# # #          print(end=" ")
# # #         if l[i+1]>l[i]:
# # #          temp= l[i]
# # #         l[i]=l[i+1]
# # #         l[i+1]=temp    
# # # print(l)


# # # 
# # # l
# # # a= input("enter string:  ")
# # # # v=0
# # # # c=0
# # # # for i in a:
# # # #     if i.isalpha()== True:
# # # #         if i in 'aeiouAEIOU':
# # # #             v=v+1
# # # #         else:
# # # #             c=c+1


# # # # print(f"Vovels = {v},consonants = {c}")
# # # print(ord("a"))
# # # print(chr(65))

# # # a= input("Enter the String: ")
# # # b=[]
# # # c=[]
# # # for i in a:
# # #     x=ord(i)
# # #     b.append(x)
# # # print(b)
# # # for j in b:
# # #     if j == 97:
# # #         print(chr(122),end="")
# # #     elif j== 65:
# # #         print(chr(90),end="")
# # #     else:
# # #         print(chr(j-1),end="")
# # # t= 1,2,3
# # # print(t)
# # # a,b,c=t
# # # # print(a,b,c)
# # # a={2,3,4,5}
# # # # print(a)
# # # b={1,2,4,3,4,5}
# # # # print(b)
# # # # print(type(a))
# # # # print(type(b))
# # # # s=set()
# # # # print(s)
# # # # print(len(a))
# # # # y={}
# # # # print(type(y))
# # # # a.add(6)
# # # # print(a)
# # # # a.update([7,8,9])
# # # # print(a)
# # # # a.remove(8)
# # # # print(a)
# # # # a.remove(7)
# # # # print(a)
# # # # a.discard(8)
# # # # print(a)
# # # # a.pop()
# # # # print(a)
# # # # a.clear()
# # # # print(a)
# # # # print(a|b)
# # # # print(a&b)
# # # # print(a-b)
# # # # print(a^b)
# # # # print(b.issubset(a))
# # # # print(b.issuperset(b))
# # # # b=a.copy()
# # # # print(b)
# # # # print(sorted(a))
# # # # print(max(a))
# # # # # print(min(a))
# # # # # print(sum(a))
# # # a={"name":"Sarang","Age":20}
# # # # print(a["name"])
# # # # print(a.get("Age"))
# # # # print(len(a))
# # # a["name"]=["Sarang","Avantika","Sreehari","Mithul"]
# # # a.update({"Age":[20,20,20,20]})
# # # # print(a)
# # # # # print(a.pop("name"))
# # # # # print(a)
# # # # # del a["Age"]
# # # # # print(a)
# # # # # a.clear()
# # # # # print(a)
# # # # print(a.keys())
# # # # print(a.values())
# # # # print(a.items())
# # # # b=a.copy()
# # # # c=dict([(1,'a')])
# # # # print(b)
# # # # print(c)
# # # # print("name" in a)
# # # # print("y" not in a)
# # # for k in a:
# # #     print(k)
# # # for v in a.values():
# # #     print(v)
# # # for k,v in a.items():
# # #     print(k,v)
# # x=('apple',[1,2,3,4,5],2.5,7,{'a':25,'b':74})
# # print(type(x))
# # x[1][2]=10
# # print(x)
# # x[4]["a"]=75
# # print(x)
# x=['name','age','qualification']
# y=['anu',24,'post graduation']
# d={}
# for i in range(len(x)):
#     d.update({x[i]:y[i]})
#     print(end="")

# print(d)
# x=input("Enter a string: ")
# d={}

# for i in x:
#     d[i]=x.count(i)

# print(d)
    
# x= "avantika"
# y="Gay"
# print(x is y)
# x=10
# result = "Even" if x%2 == 0 else "odd"
# print(result)


# a=5
# b=8
# maximum=a if a>b else b
# print(maximum)


# a=["hai"if i%2==0 else i for i in range(10)]
# print(a)
# x=5
# y=7
# z=1
# maximum=x if x>y and z else y if y>z else z
# print(maximum)

# def find_square(num):
#     result = num*num
#     return result

# square = find_square(3)
# print("square : ",square)

# def sum(a,b):
#     return a+b

# x=sum(15,12)
# print(x) 

# def power(a,b):
#     return a**b
# x=int(input("enter the number: "))
# y=int(input("Enter power: "))
# z=power(x,y)
# print(f"{x} raised to {y} is: ",z)

# def strong(a):
#     x= str(a)
#     n=len(x)
#     total=0
#     for i in x:
#         total=total+i**n
#     if total==a:
#         print("Armstrong")
#     else:
#         print ("not armstrong")

# y=int(input("enter number: "))
# strong(y)

# import math
# print(math.pow(2,3))

# def name(**kargs):
#     print(kargs)
# name(name="Anu")
# name(name="Manu",Age="24")

# sum=lambda a,b:a+b
# print(sum(5,4))

# eo=lambda a: a%2
# result=eo(2)
# if result ==0:
#     print("even")
# else:
#     print("Odd")

# a=[1,2,3,4,5]
# double=map(lambda x: x*2,a)
# result=list(double)
# print(result)
# even=list(filter(lambda x:x%2==0,a))
# print(even)
# from functools import reduce
# sum=reduce(lambda x,y:x+y,a)
# print(sum)

# import main 
# print(main.sum(5,4))
# print(main.sub(100,99))
try:
    f=open('sample1.txt','x')
except:
    pass
f=open('sample1.txt','w')
f.write("Hello")
f.write("hai")
for i in range(11):
    z=i*5
    f.write(f"{i}x5={z}\n")
f=open('sample1.txt','a')
f.write("hello")