import collections

A, B, C, D, E = map(int, input().split())

lst = []
lst.append(A)
lst.append(B)
lst.append(C)
lst.append(D)
lst.append(E)

c = collections.Counter(lst)
print(len(c))
