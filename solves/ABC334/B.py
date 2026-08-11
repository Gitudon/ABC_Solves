A, M, L, R = map(int, input().split())
const = 10**18
A += const
L += const
R += const
ans = 0

if L != R:
    if A <= L:
        res = (L - A) // M
        start = A + res * M
        ans = (R - start) // M
        if (L - A) % M == 0:
            ans += 1
    elif L < A < R:
        right = (R - A) // M
        left = (A - L) // M
        ans = right + left + 1
    elif R <= A:
        res = (A - R) // M
        start = A - res * M
        ans = (start - L) // M
        if (A - R) % M == 0:
            ans += 1
else:
    if abs(A - L) % M == 0:
        ans = 1
print(ans)
