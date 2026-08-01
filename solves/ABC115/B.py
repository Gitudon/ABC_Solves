N = int(input())
p = [int(input()) for _ in range(N)]
m = max(p)
print(sum(p) - m // 2)
