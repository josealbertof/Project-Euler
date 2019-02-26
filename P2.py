# Problema 2 de Project Euler

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    x=[0,0,1]
    sum=0
    while(x[1]<=n):
        sum+=x[1]
        x[0]=x[1]+x[2]
        x[1]=x[2]+x[0]
        x[2]=x[1]+x[0]
    print(sum)
  