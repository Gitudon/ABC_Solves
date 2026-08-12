N = int(input())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(N)]

answers = []


def count_diff(S):
    diff = 0
    for i in range(N):
        for j in range(N):
            if S[i][j] != T[i][j]:
                diff += 1
    return diff


def rotate(S):
    buf = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            buf[j][N - 1 - i] = S[i][j]
    return buf


answers.append(count_diff(S))
for i in range(3):
    S = rotate(S)
    answers.append(count_diff(S) + (i + 1))

print(min(answers))
