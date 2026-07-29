N = int(input())

flower = set()
ans = 0
for i in range(N):
    A = int(input())
    if A in flower:
        ans += 1
    else:
        flower.add(A)

print(ans)
