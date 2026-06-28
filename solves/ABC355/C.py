N, T = map(int, input().split())
A = list(map(int, input().split()))

yoko = [0] * N
tate = [0] * N
naname_1 = 0
naname_2 = 0

ans = -1
for i in range(T):
    a = A[i] - 1
    j = a // N
    k = a % N
    tate[j] += 1
    yoko[k] += 1
    if j == k:
        naname_1 += 1
    if j + k == N - 1:
        naname_2 += 1
    if yoko[k] == N or tate[j] == N or naname_1 == N or naname_2 == N:
        ans = i + 1
        break
print(ans)
