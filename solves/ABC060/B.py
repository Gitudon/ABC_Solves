A, B, C = map(int, input().split())

ans = "NO"

if A >= B:
    for a in range(1, A):
        if a * A % B == C:
            ans = "YES"
else:
    for a in range(1, B):
        if a * A % B == C:
            ans = "YES"

print(ans)
