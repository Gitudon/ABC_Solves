N, M = map(int, input().split())
A = [0] * M
B = [0] * M
for i in range(M):
    A[i], B[i] = map(int, input().split())
    A[i] -= 1
    B[i] -= 1
K = int(input())
C = [0] * K
D = [0] * K
for i in range(K):
    C[i], D[i] = map(int, input().split())
    C[i] -= 1
    D[i] -= 1
c = []


def rekkyo(a):
    b = len(a)
    if b == K:
        sara = [0] * N
        for i in range(K):
            sara[a[i]] = 1
        ans = 0
        for i in range(M):
            if sara[A[i]] == 1 and sara[B[i]] == 1:
                ans += 1
        c.append(ans)
        return
    rekkyo(a + [C[b]])
    rekkyo(a + [D[b]])


a = [C[0]]
rekkyo(a)
a = [D[0]]
rekkyo(a)
print(max(c))
