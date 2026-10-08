N = int(input())
S = [0] * N

for i in range(N):
    S[i] = input()
X, Y = map(str, input().split())

if S[int(X) - 1] == Y:
    print("Yes")
else:
    print("No")
