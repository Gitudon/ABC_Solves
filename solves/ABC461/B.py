N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = "Yes"

for i in range(N):
    if i + 1 != B[A[i] - 1]:
        ans = "No"
        break

print(ans)
