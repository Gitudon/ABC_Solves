n = int(input())
n = min(n, 10)
ans = "No"
if pow(2, n) > n**2:
    ans = "Yes"
print(ans)
