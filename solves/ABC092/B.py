N = int(input())
D, X = map(int, input().split())

ans = X
for i in range(N):
    A = int(input())
    current = 1
    chocolate = 0
    while current <= D:
        current += A
        chocolate += 1
    ans += chocolate
print(ans)
