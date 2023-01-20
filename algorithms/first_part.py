#recursion

#factorial function - not very efficient function
'''at each recursion python creates pocket space for each n until 1, then it goes to return part where
 all of these multiplications are returned starting from 1 / 1*2 / 2*3/ 6*4 / 24*5'''
def num_fact(n):
    if n==1:
        return n
    else:
        temp=num_fact(n-1)
        return temp*n

print(num_fact(5))

#permutation with recursion

def perm(text, pocket=''):
    if len(text) == 0:
        print(pocket)
    else:
        for i in range(len(text)):
            letter = text[i]
            front = text[:i]
            back = text[i+1:]
            together = front + back
            perm(together, letter+pocket)
print(perm("AB",''))

# permutation - iterative method (more efficient)

from math import factorial
def permutations(text):
    for p in range(factorial(len(str))):
        print("".join(str))
        i=len(str) - 1
        while i > o and str[i-1] > str[i]:
            i -= 1
        str[i:] = reversed(str[i:])
        if i > 0 :
            q = 1
            while str[i - 1] > str[q]:
                q += 1
            temp = str[i-1]
            str[i - 1] = str[q]
            str[q] = temp

s = 'abc'

s = list(s)
permutations(s)

