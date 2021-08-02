"""
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
"""

s1 = "pale"
s2 = "paled"

#s1 = "zale"
#s2 = "ple"

hashTable = [0] * 130
for i in s1:
  hashTable[ord(i)] += 1
  #print("hashTable 1: ", hashTable)
  print(f"{i}: ", hashTable[ord(i)])

for j in s2:
 # print("j: ", j)
  hashTable[ord(j)] -= 1
  #print("hashTable 2: ", hashTable)
  print(f"{j}: ", hashTable[ord(j)])

insertFlag = 0
deleteFlag = 0
replaceFlag = 0

for k in hashTable:
  #print("k: ", k)
  if k in [1,-1] and insertFlag == 0 and len(s2) == len(s1) + 1:
    if k == -1:
      insertFlag = 1
      print("insertFlag: ", insertFlag)
      break
  if k == [1,-1] and replaceFlag == 0 and len(s2) == len(s1):
    if k == -1:
      replaceFlag = 1
      print("replaceFlag: ", replaceFlag)
      break
  if k == 1 and deleteFlag == 0 and len(s2) == len(s1)-1:
    if k == -1:
      deleteFlag = 1
      print("deleteFlag: ", deleteFlag)
      break
    
if (insertFlag == 1 or replaceFlag == 1 or deleteFlag == 1):
  print("valid")
  if insertFlag == 1:
    print("insertion case")
  if deleteFlag == 1:
    print("deletion case")
  if replaceFlag == 1:
    print("replacement case")
else:
  print("invalid")