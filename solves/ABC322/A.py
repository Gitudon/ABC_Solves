N = int(input())
S = input()
for i in range(N - 2):
    if S[i] + S[i + 1] + S[i + 2] == "ABC":
        print(i + 1)
        exit()
print(-1)
