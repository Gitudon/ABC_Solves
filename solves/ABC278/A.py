N, K = map(int, input().split())
A = list(map(int, input().split()))

for i in range(K):
    A.remove(A[0])
    A.append(0)

a = ""
for i in range(N - 1):
    a = a + str(A[i]) + " "
a = a + str(A[N - 1])
print(a)
