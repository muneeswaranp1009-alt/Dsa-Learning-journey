'''
Pattern 2 Question in Take u Forward

Given an integer n. You need to recreate the pattern given below for any value of N.
Let's say for N = 5, the pattern should look like as below:

*
**
***
****
*****

Print the pattern in the function given to you.

'''

def pattern2(n):
    for i in range(n+1):
        for j in range(i):
            print('*',end="")
        print()
pattern2(5)