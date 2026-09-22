N = int(input())
A = list(map(int, input().split()))

buf = sorted(A[:3], reverse=True)
print(buf[-1])

for i in range(3, N):
    buf = sorted(buf + [A[i]], reverse=True)[:3]
    print(buf[-1])
