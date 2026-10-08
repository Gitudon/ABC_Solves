import collections

A, B, C, D, E = map(int, input().split())

list = []
list.append(A)
list.append(B)
list.append(C)
list.append(D)
list.append(E)

c = collections.Counter(list)
if len(c) == 2:
    d = sorted(list, reverse=True)
    del d[-1]
    e = collections.Counter(d)
    if len(e) == 2:
        print("Yes")
    else:
        print("No")
else:
    print("No")
