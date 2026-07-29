N = int(input())
A = list(map(int, input().split()))
B = sorted(A)
foo = B[-2]
for i in range(N):
    if A[i] == foo:
        print(i + 1)
