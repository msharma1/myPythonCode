"""
a b c
d e f
g h i

after shift
c f i
b e h
a d g

store - [a,b,c,d,e,f,g,h,i]
result - [c,f,i,b,e,h,a,d,g]
"""
import math
L = ['a','b','c','d','e','f','g','h','i']
step = int(math.sqrt(len(L)))
final = []
lRev = L[::-1] #[i,h,g,f,e,d,c,b,a]
for index,element in enumerate(lRev[:3]):
  st = 0
  sf = ""
  indexCount = index + st
  while (indexCount < len(L)):
    indexCount = index + st
    #if indexCount < len(L):
    sf = f"{sf}{lRev[indexCount]}"
    st += step
  final.extend(sf)
print(final)
  
  
