N, K = map(int, input().split())
S = input()
A = [True] * N
for i in range(N):
    if S[i] == "o":
        A[i] = True
    else:
        A[i] = False
tmp = 0
T = ""
for i in range(N):
    if A[i] and tmp < K:
        T += "o"
        tmp += 1
    else:
        T += "x"
print(T)
