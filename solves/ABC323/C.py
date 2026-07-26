N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [input() for _ in range(N)]

tokuten = [0] * N
for i in range(N):
    score = 0
    for j in range(M):
        if S[i][j] == "o":
            score += A[j]
    tokuten[i] = score + (i + 1)

number_one = max(tokuten)
number_one_num = 0
for i in range(N):
    if tokuten[i] == number_one:
        number_one_num += 1

for i in range(N):
    current_score = tokuten[i]
    if current_score == number_one and number_one_num == 1:
        print(0)
    else:
        not_answered = []
        for j in range(M):
            if S[i][j] == "x":
                not_answered.append(A[j])
        not_answered.sort(reverse=True)
        ans = 0
        for na in not_answered:
            current_score += na
            ans += 1
            if current_score > number_one:
                break
        print(ans)
