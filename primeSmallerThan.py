"""
Count number of primes smalled
than a given positive integer

Input: 20
Output: [2,3,5,7,11,13,17,19]
"""
import math
n = 36
LF = []
d = {}
for i in range(2, n):
  d[i] = True
  
print(d)
for i in range(2,int(math.sqrt(n))+1):
  print("i: ",i)
  for j in range(i,n+1):
    if i*j <= n:
      print("i*j: ", i*j)
      if i*j <= n and i*j in d:
        d[i*j] = False
for k in d:
  if d[k] == True:
    print(k)  
print(d)
    
  
    
