N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

buf = 0
for i in range(N):
    buf += A[i] * B[i]

if buf == 0:
    print("Yes")
else:
    print("No")
