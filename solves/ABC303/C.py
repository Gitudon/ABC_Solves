N, M, H, K = map(int, input().split())
S = input()
z = {}
for i in range(M):
    x, y = map(int, input().split())
    z[f"{x} {y}"] = True
X = 0
Y = 0
for i in range(N):
    H -= 1
    if H < 0:
        print("No")
        exit()
    if S[i] == "R":
        X += 1
    elif S[i] == "L":
        X -= 1
    elif S[i] == "U":
        Y += 1
    elif S[i] == "D":
        Y -= 1
    if f"{X} {Y}" in z and H <= K:
        H = K
        del z[f"{X} {Y}"]
print("Yes")
