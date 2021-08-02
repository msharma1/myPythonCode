"""
Maximum water container
input: [1,8,6,2,5,4,8,3,7]
output: 54
"""
L = [1,8,6,2,5,4,8,3,7]
def calArea(L):
  left = 0
  right = len(L) -1
  areaHolder = []
  while(left < right):
    areaHolder.append((min(L[left],L[right]))*(right-left))
    if L[left] < L[right]:
      left += 1
    else:
      right -= 1
  print(areaHolder) #[8,49,18,40,16,15,4,6]
  print(max(areaHolder))
  
calArea(L)