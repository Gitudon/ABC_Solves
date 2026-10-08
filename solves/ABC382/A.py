N, D = map(int, input().split())
S = input()
cookie = 0
for s in S:
    if s == "@":
        cookie += 1
print(N - cookie + D)
