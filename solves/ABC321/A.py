N = input()
ans = True
for i in range(len(N) - 1):
    if N[i] <= N[i + 1]:
        ans = False
if ans:
    print("Yes")
else:
    print("No")
