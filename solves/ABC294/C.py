N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = sorted(A + B)
get_index = {c: i + 1 for i, c in enumerate(C)}
for a in A:
    print(get_index[a])
for b in B:
    print(get_index[b])
