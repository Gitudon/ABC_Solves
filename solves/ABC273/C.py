import bisect

N = int(input())
A = list(map(int, input().split()))

A_dash = sorted(list(set(A)))
N_dash = len(A_dash)
dictionary = {}
for a in A:
    idx = bisect.bisect(A_dash, a)
    key = str(N_dash - idx)
    if key in dictionary:
        dictionary[key] += 1
    else:
        dictionary[key] = 1

for K in range(N):
    k = str(K)
    if k in dictionary.keys():
        print(dictionary[k])
    else:
        print(0)
