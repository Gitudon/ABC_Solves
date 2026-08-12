S = input()

A = []

i = 0
cnt = 0
while i < len(S):
    if S[i] == "-":
        cnt += 1
    else:
        A.append(cnt)
        cnt = 0
    i += 1

print(*A[1:])
