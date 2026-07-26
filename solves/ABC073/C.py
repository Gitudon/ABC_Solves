N = int(input())

paper = {}

for _ in range(N):
    A = int(input())
    if A in paper and paper[A] == 1:
        paper[A] = 0
    else:
        paper[A] = 1

ans = 0
for key in paper:
    if paper[key] != 0:
        ans += 1
print(ans)
