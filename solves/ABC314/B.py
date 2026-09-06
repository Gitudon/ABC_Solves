N = int(input())
C = [0] * N
A = [0] * N
for i in range(N):
    C[i] = int(input())
    A[i] = list(map(int, input().split()))
X = int(input())
kiroku = [0] * N
for i in range(N):
    if X in A[i]:
        kiroku[i] = len(A[i])
kekka = []
saisyo = 10000
for i in range(N):
    if 0 < kiroku[i] < saisyo:
        saisyo = kiroku[i]
for i in range(N):
    if kiroku[i] == saisyo:
        kekka.append(i + 1)
print(len(kekka))
print(*kekka)
