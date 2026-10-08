N = int(input())
S = [input() for _ in range(N)]
flag = True
for i in range(N - 1):
    if S[i] == S[i + 1] and S[i] == "sweet" and i != N - 2:
        flag = False
        break
if flag:
    print("Yes")
else:
    print("No")
