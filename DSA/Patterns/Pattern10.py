'''
Pattern 10(Half Diamond) question in take u forward

Given an integer n. You need to recreate the pattern given below for any value of N.
Let's say for N = 5, the pattern should look like as below:

*
**
***
****
*****
****
***
**
*

Print the pattern in the function given to you.

'''

#Solution

def pattern10(n):
    for i in range(n):
        for j in range(i):
            print('*',end="")
        print()
    for i in range(1,n+1):
        for j in range(n-i+1):
            print('*',end="")
        print()
pattern10(4)
