
"""  Question 1

Write a program that will find all numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a list.

Hint: Consider using the range(#begin, #end) method. """

#---------------------------code----------------------------------------#

result = []
for i in range(2000, 3200):
    if i % 7 == 0 and i % 5 != 0:
        result.append(i)
print(result)


#------------------------------------------------------------------------#

""" Q 2 
 Write a program that can compute the factorial of a given number. (The factorial of n is the product of all positive integers less than or equal to n.) For example: For factorial(5)= 5 x 4 x 3 x 2 x 1 the result is 120 (i.e. factorial (0)=1). """
 
 
 #---------------------------code----------------------------------------#
 n = 5
result = 1
for i in range(1, n+1):
    result *= i
print(result)  

# Answer 120

#------------------------------------------------------------------------#


""" Q 3
With a given integer number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). Then, the program should print the dictionary. Suppose the following input is supplied to the program: 8 Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}  
"""

#---------------------------code----------------------------------------#

n = int(input("Enter a number : "))
dict = {}

for i in range(1, n+1):
    dict[i] = i*i

print(dict)

#------------------------------------------------------------------------#

#Q 4 



#---------------------------code----------------------------------------#


def missing_char(name, n):
    return name[:n] + name[n+1:]

missing_char("hossam",5)
#------------------------------------------------------------------------#



#Q 5  Conver from  array to list

#---------------------------code----------------------------------------#
import numpy as np

new_array = np.array([[0,1],[2,3],[4 ,5]])

list = new_array.tolist()
print(list)

#-----------------------------------------------------------------------#


#Q 6 


array1 = [0, 1 ,2] 

array2 = [2, 1 ,0] 
conv = np.cov(array1,array2)
print(conv)





# Q 7 

C , H = 50 , 30
D = input("enter values comma-separated: ")
D= D.split(",")
Q = []
for i in D:
    q = ((2 * C * int(i)) / H) ** 0.5
    q = round(q)
    Q.append(q)


print(Q)
