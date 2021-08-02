L = [1,2,3,4,5,6]
n = 4

def BS(L,n):
  start = 0
  end = len(L)-1
  #mid = len(L)//2
 # print(mid)
  while(start <= end):
    mid = (start+end)//2
    if n == L[mid]:
      return mid
    if n > L[mid]:
      start = mid+1
      #mid = (start+end)//2
#    BS(L[mid:end],n)
    if n < L[mid]:
      end = mid-1
  return -1
      #mid = (start+mid)//2
    #BS(L[start:mid],n)
    
res = BS(L,n)
print(res)