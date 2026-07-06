N = int(input())
d = list(map(int, input().split()))

d = sorted(d)
mannaka = N // 2

print(d[mannaka] - d[mannaka - 1])
