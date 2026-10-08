A, B, C, D = map(int, input().split())

ans = "Yes"

if C > A:
    ans = "No"
elif C == A:
    if D > B:
        ans = "No"
else:
    pass

print(ans)
