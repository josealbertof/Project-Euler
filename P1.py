# Problema 1 de Project Euler

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    n_3=(n-1)//3
    n_5=(n-1)//5
    m=(n-1)//15
    num=3*n_3*(n_3+1)//2+5*(n_5*(n_5+1)//2-3*m*(m+1)//2)
    print(num)
