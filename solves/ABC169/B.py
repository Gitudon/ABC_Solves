N = int(input())
A = list(map(int, input().split()))

if 0 in A:
    print(0)
    exit()

ans = 1
for i in range(N):
    ans *= A[i]
    if ans > 10**18:
        ans = -1
        break

print(ans)
