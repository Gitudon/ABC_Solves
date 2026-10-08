N = int(input())
S = [0] * N
for i in range(N):
    S[i] = input()
for i in range(N):
    print(S[N - 1 - i])
