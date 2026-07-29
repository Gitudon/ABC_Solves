N = int(input())

ans = "No"
for a in range(100):
    for b in range(100):
        if 4 * a + 7 * b == N:
            ans = "Yes"

print(ans)
