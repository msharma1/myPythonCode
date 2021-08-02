"""
Longet substring without repition
"""
s = "abaacad"
def findPattern(L):
  left = 0
  right = 0
  lTemp = []
  d = {}
  ans = 0
  while(left < len(L) and right < len(L)):
    if L[right] in d:
    #d[ele] = ind
      left = max(left,d[L[right]] + 1)
      d[L[right]] = right
    else:
      d[L[right]] = right 
    ans = max(ans,right-left+1)
    right += 1
  print(d)
  print(left)
  print(right)
  print(ans)
findPattern(s)
      