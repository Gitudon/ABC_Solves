N, D = map(int, input().split())
S = input()
cookies = []
for s in S:
    cookies.append(s)
for i in range(D):
    for j in range(1, N + 1):
        if cookies[-j] == "@":
            cookies[-j] = "."
            break
print("".join(cookies))
