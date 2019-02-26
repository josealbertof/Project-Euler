# Problema 5 de Project Euler

import sys
import math
def highest_primes(n):
    x=[]
    primes=[]
    for i in range(n-1):
        if not_divisible(i+2,primes):
            primes.append(i+2)
            x.append((i+2)**int(math.log(n,i+2)))
    return x
def not_divisible(n,x):
    devolver=True
    for i in x:
        if n%i==0:
            devolver=False
    return devolver
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    x=highest_primes(n)
    resultado=1
    for i in x:
        resultado=resultado*i
    print(resultado)
