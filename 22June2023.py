#!/usr/bin/env python
# coding: utf-8

# In[1]:


x=10


# In[2]:


print(x)


# In[3]:


#operators
#-->syymbol-->perform particular functionality ++, --, /
#operands -->a+b , 10-12
#assignment, comparision,logical, bitwise, membership, identity


# In[4]:


#arithmetic +,-,* , /
10/2


# In[5]:


type(5.0)


# In[6]:


1.0+5


# In[7]:


10//2
#floor division


# In[8]:


11%2
#modulus


# In[9]:


13%2


# In[10]:


13.0%2


# In[11]:


2**3
#2*2*2


# In[12]:


4**3


# In[13]:


10+4-2*4/1+9


# In[14]:


#comparision-->give boolean answer
x=10

# ==, !=, >,  <, >=, <=
x>10


# In[15]:


x==10


# In[16]:


#assignment
#unary

age=10


# In[17]:


#variable=litral(value)
#variable=expression

age=10

salary=age*20


# In[18]:


salary=100
#salary=salary*5
salary*=5

print(salary)


# In[19]:


num=5
num **= 4

#num= num**4
print(num)


# In[20]:


#bitwise operators-->works on numbers--> converted into bit(0,1){less space requried}
10&9


# In[21]:


7|5


# In[22]:


18&11


# In[23]:


18|11
11


# In[24]:


11>>1


# In[25]:


11>>2


# In[26]:


44<<2


# In[27]:


x=10 
y=20


# In[28]:


x==10


# In[29]:


y>=20


# In[30]:


x==10 and y>=20


# In[31]:


x==10 and y>20


# In[32]:


#membership-->in,not in
"R" in "RAJASTHAN"


# In[33]:


"r" in "RAJASTHAN"


# In[34]:


"RAJT" in "RAJASTHAN"


# In[35]:


"RAJT" not in "RAJASTHAN"


# In[36]:


"RAJA" not in "RAJASTHAN"


# In[37]:


#identity-->whether it tell its identity or not{kya kissi class ka koi object hh, kya kissi ka datatype hh ya nhii}
#identity: identification (class ka object, datatype)
x=10
print(type(x))


# In[38]:


age=20

type(age) is int


# In[39]:


type(age) is str


# In[40]:


type(age) is not int


# In[41]:


#conditional statements
#if-else
'''
if(condition):
    print()     --> extra space is called indentation(using tab button)
'''


# In[42]:


age =5

if(age==18):
    print("age is greater than 18")
else:
    print("age is less than 18")


# In[43]:


age =18
if(age==10):
    print("age is greater than 18")
elif(age==19):
    print("age is 19")
else:
    print("age is less")


# In[44]:


num1=15
num2=10
num3=30
if(num1>num2 and num1>num3):
        print("num1 is greater")
elif(num2>num1 and num2>num3 ):
    print("num2 is greater")
else:
    print("num3 is greater")


# In[45]:


a="arpita"
if(type(a)==str):
    print(a,len(a))
else:
   print("input is not string type")


# In[46]:


a=32
if(a%2==0 and a%3==0):
    print("number is divisible by 6")
else:
    print("not divisible by 6")


# In[47]:


age=18
name="tushar"
if(age==18):
    if(name=="tushar"):
        print("name is :",name, age )
    else:
        print("name is not tushar")
else:
    print("age is not equal to 18")


# In[48]:


x=input("enter a number")
print(x)


# In[49]:


#take a input from user...if inputt==int and num is 6 to to then print num
num=int(input("enter a number : "))
if(type(num) is int):
    if(num>=6 and num<=20):
        print(num,type(num))
    else:
        print("num is not between 6 and 20")
else:
    print("num is not int type")


# In[50]:


#WAP to check if (num>18) print num is greater than  18..
#if num is between 24 and 30 then print num is greater than24 and less than 30   . 
#if num=30 then print num is 35

n1=int(input("Enter number"))
print(n1)
if(n1>18):
    print(n1," :number is greater than 18")
if(24<n1<30):
    print(n1, " : number is greater than 24 and less than 30")
if(n1==35):
    print(n1," : number is 35")


# In[51]:


#loops-->help in repeatitive execute a task
#for, while
#for loop--> when we know stating and ending point...used when numberof iterations are known...
#for(i=0;i<cond;i++)
#range(start,stop,[step=1])--> generate value(ending position not include)

for count in range(1,4,1):
    print(count)


# In[52]:


for count in range(1,6,2):
    print(count)


# In[53]:


for count in range(6,1,-2):
    print(count)


# In[54]:


for count in range(4,10,-1):
    print(count)


# In[55]:


for chr in "hello":
    print(chr)


# In[56]:


data="jaipur"
for chr in data:
    print(chr,end="")


# In[57]:


print("hello",end=" ")
print("user")


# In[58]:


city="jaipur"
len(city)


# In[59]:


for index in range(0,len(city)):
    print(index,city[index])


# In[60]:


#create a num 10 to 25 but step size =3 
for num in range(10,25,3):
    if(num%2==0):
        print("num is even",num)
    else:
        print("num is odd ",num)
        


# In[61]:


#take input fron user and check if the index is even then print which char. is present atnthat index position
#input int type from use. if input= int loop chalana from 0 to num and print all odd numbers
#loop from 1 to 100 and find prime numbers
a=input("enter a number ")
print(len(a))
for index in range(0,len(a)):
    if(index%2==0):
    
        print(index,a[index])
    


# In[62]:


x=int(input("enter a number "))
print(x)
if(type(x) is int):
    for i in range(0,x,1):
        if(i%2 !=0):
            print(i)
        


# In[63]:


def is_prime(n):
    if(n<2):
        return False
    g=int(n*0.5)
    for i in range(2,g+1):
        if(n%i==0):
            return False
    return True

print("prime numbers between 1 to 100 : ")
for num in range(1,101):
    if is_prime(num):
        print(num)

    
        


# In[64]:


#nested loops
for var in range(1,5):
    for count in range(14,16):
        print(count,var)


# In[65]:


#patterns
for rows in range(1,5):
    for col in range(1,rows+1):
        print('*',end=" ")
    print(" ")


# In[66]:


for rows in range(1,5):
    for col in range (5,rows,-1):
        print('*',end=" ")
    print(" ")


# In[67]:


for rows in range(1,5):
    for col in range (1,rows+1):
        print(col,end=" ")
    print(" ")


# In[68]:


for rows in range(1,5):
    for col in range (4,rows-1,-1):
        print(col,end=" ")
    print(" ")


# In[69]:


r=int(input("enter nomber of rows"))
c=int(input("enter number of columns"))
num=1
for rows in range(1,r+1):
    for col in range (1,rows+1):
        print(num,end=" ")
        num +=1
    print(" ")


# ### 23June,2023

# In[70]:


count=1
while(count<3):
    print(count)
    count+=1


# In[71]:


data="rajasthan"
index=0
while(index<len(data)):
    print(index,data[index])
    index+=1


# In[72]:


#slicing--> extrcting a portion of a string 
#indexing
city='RAJASTHAN'

city[0]


# In[73]:


city[-1]


# In[74]:


#slicing[start : stop : [step=1] ]
#stoping position is exclusive
city[0:3]


# In[75]:


city[0:6]


# In[76]:


city[0:]


# In[77]:


city[2:]


# In[78]:


city[:4]


# In[79]:


city[2:7]


# In[80]:


city[1:1]


# In[81]:


city[-1:-4]


# In[82]:


city[-1:-4:-1]


# In[83]:


city[-4:-2]


# In[84]:


city[-4::1]


# In[85]:


city[-4::-1]


# In[86]:


city[:4:-1]


# In[87]:


city[1::-1]


# In[88]:


#palindrome
#saras , naman
name="saras"
name[::-1]

if(name==name[::-1]):
    print("its palindrome")
else:
    print("not")


# In[89]:


#check a string is palindrome for any string using for loop(starting and ending character is same)
x=input("enter a string : ")
y=''
for i in x:
    y=i+y
if(x==y):
    print(x," is an palindrome")
else:
    print(x ," is not an palindrome")


# In[90]:


# take input from user and count how many vowels are their inside it ..total count
x=input("Type Input : ")
count=0
for i in x:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        count+=1
print(count)



# In[91]:


#take a input from user and count number of individual vowels...a=0,e=2,i=1,u=3
x=input("type input : ")
j=0
k=0
l=0
m=0
n=0
for i in x:
    if(i=='a'):
        j+=1
    if(i=='e'):
        k+=1
    if(i=='i'):
        l+=1
    if(i=='o'):
        m+=1
    if(i=='u'):
        n+=1
print("a=",j," ,e=",k," ,i=",l," ,o=",m," ,u=",n)


# In[92]:


#take a input from user and wherever we find vowel then replace it with #
x=input("type input : ")
for i in x:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        x=x.replace(i,'#')
print(x)


# In[93]:


# list--> a sought of array type
# data type in python
# multiple data element is stored
# ordered collection of element(index)
#mutable datatype
#[]

myList=[10,20,30,'hey']
type(myList)
myList


# In[94]:


myList[0]


# In[95]:


myList[1::]


# In[96]:


#myList=[10,20,30,'hey']

#update element
myList[0]=90
myList


# In[97]:


myList=[10,20,30,'hey']
myList[0:2]=[99,88,77]
myList


# In[98]:


myList=[10,20,30,'hey']
myList[2:4]=[22,31,44,55,66]
myList


# In[99]:


myList


# In[100]:


myList.append(100)


# In[101]:


myList


# In[102]:


myList.extend([1,2,3])   #iterable data is inserted


# In[103]:


myList


# In[104]:


#iterable-->jiske upar hum loop chala sakte hh
for i in "hey":
    print(i)


# In[105]:


myList.insert(1,"ABC")


# In[106]:


myList


# In[107]:


myList.pop(1)  # index of element is given


# In[108]:


myList


# In[109]:


myList.remove(55)           #element is itself given


# In[110]:


myList


# In[111]:


del myList[-1]
print(myList)


# In[112]:


help(myList)


# In[113]:


#agar list me data int hh to appaend it otherwise not
myList=[11,22,33,44,55,'arpita']
newList=[]
for i in myList:
    if(type(i) is int):
        newList.append(i)


# In[114]:


print(newList)


# In[2]:


#list in which all are int...if element is int then square of that no. and appnd in new list and if other type of data then 
#append in new list using while loop
mylist=[10,20,30,40,'arpita']
sqlist=[]
newlist=[]
len(mylist)
i=0
while(i<len(mylist)):
    if(type(mylist[i]) is int):
        sqlist.append(mylist[i]**2)
        i+=1
    else:
        newlist.append(mylist[i])
        i+=1
print(sqlist)
print(newlist)
   


# In[ ]:


print(sqlist)


# #### take a input from a user if input is string datatype then get all the unique (no duplicate words)word from that string
# #### no regular expression/ no inbuilt -->alphanumeric, unique,(x)

# In[7]:


mylist=[]
newlist=[]
x=input("Type input ")
for i in x:
    mylist.append(i)
print(mylist)
for j in x:
    for k in range(1,len(mylist)):
        if(j!=k):
            newlist.append(j)
        
    break
print(newlist)


# ## 
