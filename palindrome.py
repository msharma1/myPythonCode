"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
1.5
1.6
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)
"""

s = "Taxt Coa"


hashTable = [0] * 150

for i in s:
  print(f"i: {i}")
  #i = ord(i)
  print(f"ord(i): ", ord(i))
  if ord(i) > 90:
    i = ord(i)-32
  else:
    i = ord(i)
  print(f"new ord(i): ", i)
  if i != 32:
    hashTable[i] += 1
  print(f'{hashTable}')
  print("hashTable[i]: ", hashTable[i])

middlecount = 0
print(hashTable)
for j in hashTable:
  if (j == 0 or j ==2) and (middlecount == 0 or middlecount == 1):
    continue
  elif j == 1:
    middlecount += 1
  else:
    print("not a palindrome")
    break
else:
  print("palindrome")