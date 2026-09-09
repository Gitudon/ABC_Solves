N, M, X = map(int, input().split())
A = list(map(int, input().split()))

migi = 0
for i in range(X, N):
    if i in A:
        migi += 1

hidari = 0
for i in range(X - 1, -1, -1):
    if i in A:
        hidari += 1
print(min(migi, hidari))
