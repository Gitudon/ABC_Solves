import collections

S = input()
list = []

list.append(S[0])
list.append(S[1])
list.append(S[2])

a = collections.Counter(list)
b = len(a)

if b == 1:
    print(1)
elif b == 2:
    print(3)
else:
    print(6)
