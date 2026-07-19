N, K = map(int, input().split())
S = input()

katamari_start = []
katamari_end = []

i = 0
while i < N:
    if S[i] == "0":
        i += 1
        continue
    start = i
    while i < N and S[i] == "1":
        i += 1
    end = i - 1
    katamari_start.append(start)
    katamari_end.append(end)
print(
    S[: katamari_end[K - 2] + 1]
    + S[katamari_start[K - 1] : katamari_end[K - 1] + 1]
    + S[katamari_end[K - 2] + 1 : katamari_start[K - 1]]
    + S[katamari_end[K - 1] + 1 :]
)
