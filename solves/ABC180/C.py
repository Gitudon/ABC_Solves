N = int(input())

border = int(N ** (0.5))
ans = []
big = []
for i in range(1, border + 1):
    if N % i == 0:
        ans.append(i)
        big.append(N // i)
if border == N ** (0.5):
    big.pop()
ans += big[::-1]
for a in ans:
    print(a)
