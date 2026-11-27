'''
Pattern 15(Reverse Letter Triangle) question in take u forward

Given an integer n. You need to recreate the pattern given below for any value of N.
Let's say for N = 5, the pattern should look like as below:

ABCDE
ABCD
ABC
AB
A

Print the pattern in the function given to you.

'''

#Solution

def pattern15(n):
    for i in range(n):
        for j in range(n-i):
            print(chr(ord("A")+j),end="")
        print()
pattern15(5)
