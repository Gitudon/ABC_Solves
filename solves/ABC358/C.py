N, M = map(int, input().split())
S = [input() for _ in range(N)]
ans = []
hantei = "o" * M
if hantei in S:
    print(1)
    exit()


def solve(n, c, past):
    if c == hantei:
        ans.append(n)
        return
    for i in range(N):
        if not past[i]:
            d = ""
            for j in range(M):
                if S[i][j] == "o" or c[j] == "o":
                    d += "o"
                else:
                    d += "x"
            past[i] = True
            solve(n + 1, d, past)
            past[i] = False


for i in range(N):
    past = [False] * N
    past[i] = True
    solve(1, S[i], past)
print(min(ans))
