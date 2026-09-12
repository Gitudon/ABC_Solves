N, M = map(int, input().split())
A = [0] * N
for i in range(N):
    A[i] = int(input())
B = [0] * M
for i in range(M):
    B[i] = int(input())
kyogi = [0] * N
for i in range(M):
    for j in range(N):
        if B[i] >= A[j]:
            kyogi[j] += 1
            break
a = max(kyogi)
for i in range(N):
    if kyogi[i] == a:
        print(i + 1)
