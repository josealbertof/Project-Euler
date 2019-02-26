# Problema 3 de Project Euler

import sys
import math

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    raiz=int(math.sqrt(n))
    i=2
    factor=n
    repetir=True
    while n!=1 and repetir:
        if n%i==0:
            n=n//i
            factor=i
        else:
            i+=1
        if i>math.sqrt(n):
            factor=n
            repetir=False
    print(factor)