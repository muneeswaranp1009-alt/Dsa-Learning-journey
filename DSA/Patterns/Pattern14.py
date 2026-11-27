'''
Pattern 14(Row Character Triangle) question in take u forward

Given an integer n. You need to recreate the pattern given below for any value of N.
Let's say for N = 5, the pattern should look like as below:

A
AB
ABC
ABCD
ABCDE

Print the pattern in the function given to you.

'''

#Solution

def pattern14(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(ord('A')+j),end="")
        print()
pattern14(5)
