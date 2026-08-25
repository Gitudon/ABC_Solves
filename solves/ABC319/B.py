N = int(input())
ans = ""
for i in range(N + 1):
    tmp = []
    for j in range(1, 10):
        if N % j == 0:
            if i % (N / j) == 0:
                tmp.append(j)
    if tmp != []:
        ans += str(min(tmp))
    else:
        ans += "-"
print(ans)
