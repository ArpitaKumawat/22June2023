#!/usr/bin/env python
# coding: utf-8

# ### ASSIGNMENT(22June2023)
# #### 1) Take a input from user. and if input is integer and number is present between 6 to 20 then print that number.

# In[1]:


num=int(input("enter a number : "))
if(type(num) is int):
    if(num>=6 and num<=20):
        print(num,type(num))
    else:
        print("num is not between 6 and 20")
else:
    print("num is not int type")


# #### 2) WAP to check if (num>18) print num is greater than  18 and if num is between 24 and 30 then print num is greater than24 and less than 30 and if num=35 then print num is 35

# In[3]:


n1=int(input("Enter number"))
print(n1)
if(n1>18):
    print(n1," :number is greater than 18")
if(24<n1<30):
    print(n1, " : number is greater than 24 and less than 30")
if(n1==35):
    print(n1," : number is 35")


# #### 3)Take input fron user and check if the index is even then print which character is present at that index position.

# In[1]:


a=input("Type Input : ")
print(len(a))
for index in range(0,len(a)):
    if(index%2==0):
    
        print(index,a[index])


# #### 4) Take input integer type from user. and if input is integer then from 0 to that input number using a loop, print all odd numbers.

# In[2]:


x=int(input("enter a number "))
print(x)
if(type(x) is int):
    for i in range(0,x,1):
        if(i%2 !=0):
            print(i)


# #### 5) Find all prime numbers between 1 to 100 using loop.

# In[3]:


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


# #### 6) Print different types of patterns.

# In[4]:


for rows in range(1,5):
    for col in range(1,rows+1):
        print('*',end=" ")
    print(" ")


# In[5]:


for rows in range(1,5):
    for col in range (5,rows,-1):
        print('*',end=" ")
    print(" ")


# In[6]:


for rows in range(1,5):
    for col in range (1,rows+1):
        print(col,end=" ")
    print(" ")


# In[7]:


for rows in range(1,5):
    for col in range (4,rows-1,-1):
        print(col,end=" ")
    print(" ")


# In[9]:


r=int(input("enter nomber of rows: "))
c=int(input("enter number of columns: "))
num=1
for rows in range(1,r+1):
    for col in range (1,rows+1):
        print(num,end=" ")
        num +=1
    print(" ")

