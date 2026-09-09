S = input()
mozi = []

mozisu = 1
while mozisu <= len(S):
    for i in range(len(S) - mozisu + 1):
        tmp = ""
        for j in range(mozisu):
            tmp += S[i + j]
        mozi.append(tmp)
    mozisu += 1

print(len(list(set(mozi))))
