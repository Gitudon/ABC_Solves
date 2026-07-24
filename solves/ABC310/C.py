N = int(input())
S = set()
for i in range(N):
    s = input()
    t = s[::-1]
    if (t not in S) and (s not in S):
        S.add(s)
print(len(S))
