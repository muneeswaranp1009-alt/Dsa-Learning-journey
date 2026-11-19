'''
Pattern 1 Question in Take u Forward

Given an integer n. You need to recreate the pattern given below for any value of N.
Let's say for N = 5, the pattern should look like as below:

*****
*****
*****
*****
*****

Print the pattern in the function given to you.'''


def pattern(n):
    for i in range(n):
        for j in range(n):
            print('*',end="")
        print()
pattern(5)