#!/usr/bin/env python
# coding: utf-8

# # day6

# In[1]:


#list of numbers and add 2 to every value
test_list1 = [1, 5, 7, 11, 15]
res_list = []
for i in range(0, len(test_list1)):
  res_list.append(test_list1[i] + 2)
print("Resultant list is :" + str(res_list))


# In[2]:


#pattern
for i in range(5, 0, -1):
  for j in range(i, 0, -1):
    print(j, end="")
  print()


# In[4]:


#fibonacci sequence

nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0

if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1


# In[5]:


#armstrong number

num = int(input("Enter a number: "))

sum = 0

temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


# In[6]:


#multiplication table of 9
num = int(input("Show the multiplication table of? "))  
# using for loop to iterate multiplication 10 times   
for i in range(1,11):  
   print(num,'x',i,'=',num*i)  


# In[7]:


#number is postive or negative
n=int(input())
if n<0:
    print("n is a negative number")
elif n>0:
    print("n is a positive number")
else:
    print("n is equal to zero")


# In[8]:


#convert number of days into ages
days= 5555  
years= days / 365  
print("Number of years is: ")
print(years)


# In[9]:


#trigonmetery problem
import math

print(math.sin(math.pi/3)) 
print(math.tan(math.pi/3))
print(math.cos(math.pi/6))


# In[10]:


#calculator
print("Calculator")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

ch=int(input("Enter Choice(1-4): "))

if ch==1:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a+b
    print("Sum = ",c)
elif ch==2:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a-b
    print("Difference = ",c)
elif  ch==3:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a*b
    print("Product = ",c)
elif ch==4:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a/b
    print("Quotient = ",c)
else:
    print("Invalid Choice")


# In[ ]:




