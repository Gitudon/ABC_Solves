N, L, R = map(int, input().split())
A = []
for i in range(N):
    A += [i + 1]
hidari = A[: L - 1]
migi = A[R:]
mannaka = A[L - 1 : R]
mannaka2 = []
for i in range(len(mannaka)):
    mannaka2 += [mannaka[len(mannaka) - 1 - i]]
new_A = hidari + mannaka2 + migi
print(*new_A)
