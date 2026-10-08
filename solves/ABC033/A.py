N = input()
ans = 0
for i in range(1, len(N)):
    if N[0] == N[i]:
        ans += 1
if ans != 3:
    print("DIFFERENT")
else:
    print("SAME")
