'''After applying all the rotations the FIRSTCHARSTRING string will be "rcr"
which is not anagram of any sub string of original string "carrace".
input:
carrace
3
L 2
R 2
L 3
output:
NO

original = input()
k = int(input())
operations = []
for _ in range(k):
    op, num = input().split()
    operations.append((op, int(num)))

firstcharstring = list(original)
for op, num in operations:
    if op == "L":
        firstcharstring = firstcharstring[num:] + firstcharstring[:num]
    else:
        firstcharstring = firstcharstring[-num:] + firstcharstring[:-num]

result = "NO"
for i in range(len(original)):
    for j in range(i + 1, len(original) + 1):
        substring = original[i:j]
        if sorted(substring) == sorted("".join(firstcharstring)):
            result = "YES"
            break

print(result)

data=input()
rot=int(input())
res=''
for i in range(rot):
    di,mag=input().split()
    if di.upper()=='L':
        res += (data[int(mag):]+data[:int(mag)])[0]
        print(res)
    elif di.upper()=='R':
        res += (data[:int(mag)]+data[int(mag):])[0]
        print(res)
#anagram
subList=[data[i:i+rot] for i in range(0,len(data)-rot+1)]
print(subList)
for subele in subList:
    if sorted(subele)==sorted(res):
        print("YES")
        break
else:
    print("NO")'''

#using double ended queue

from collections import deque
data=input()
qStr=deque(data)
rot=int(input())
res=''
for i in range(rot):
    di,mag=input().split()
    if di=='L' or di=='l':
        qStr.rotate(-int(mag))
        res+=qStr[0]
    elif di=='R' or di=='r':
        qStr.rotate(int(mag))
        res+=qStr[0]
#anagram
subList=[data[i:i+rot] for i in range(0,len(data)-rot+1)]
print(res,subList)
for subele in subList:
    if sorted(subele)==sorted(res):
        print("YES")
        break
else:
    print("NO")

