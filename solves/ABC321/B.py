N, X = map(int, input().split())
A = list(map(int, input().split()))
for i in range(0, 101):
    B = A + [i]
    x = sum(B) - max(B) - min(B)
    if x >= X:
        print(i)
        exit()
print(-1)
