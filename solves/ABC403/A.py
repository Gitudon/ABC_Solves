S, T = map(str, input().split())
if S == "AtCoder" and T == "Land":
    print("Yes")
else:
    print("No")

N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    if i % 2 == 0:
        ans += A[i]
print(ans)
