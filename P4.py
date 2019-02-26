# Problema 4 de Project Euler

import sys
def is_palindrome(n):
    n=str(n)
    x=[int(i) for i in n]
    y=x.copy()
    y.reverse()
    return x==y
def product(n):
    resultado=False
    i=100
    while not resultado and i<1000:
        if n%i==0 and n/i<1000:
            resultado=True
        else:
            i+=1
    return resultado
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    palindromo=False
    n-=1
    while not palindromo:
        if is_palindrome(n) and product(n):
            palindromo=True
            resultado=n
        else:
            n=n-1
        if n<=101101:
            palindromo=True
            resultado=101101
    print(resultado)
        
        
        
        