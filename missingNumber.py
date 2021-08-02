"""
find missing in an array
"""
M = {}
L = [3,0,1]
L.sort() #[0,1,3]:
max = 0
for i in L:
  M[i] = True
  if i > max:
    max = i
    
for j in range(max):
  if j in M:
    continue
  else:
    print(j)