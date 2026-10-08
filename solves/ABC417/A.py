N, A, B = map(int, input().split())
S = input()
ans = ""
for i in range(A, N - B):
    ans += S[i]
print(ans)
