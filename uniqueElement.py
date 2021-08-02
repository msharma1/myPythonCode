"""
Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.
"""

s1 = "abcdeap"
s2 = "cdeabax"
dFinal = {}
def findPermutation(s1,s2):
  hashTable = [0] * 256
  hashTableBefore = hashTable
  print(f'hashTable now: {hashTable}')
  for i in s1:
    print(f'ord(i): {ord(i)}')
    hashTable[ord(i)] += 1
  for j in s2:
    hashTable[ord(j)] -= 1
  print(f'hashTable after: {hashTable}')
  for v in hashTable:
    if v != 0:
      return False
  return True

result = findPermutation(s1,s2)
print(result)