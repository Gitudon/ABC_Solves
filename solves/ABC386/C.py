K = int(input())
S = input()
T = input()

lens = len(S)
lent = len(T)
s = list(S)
t = list(T)
ans = "Yes"

if S != T:
    if abs(lens - lent) > K:
        ans = "No"
    else:
        # S中の一文字を変更
        if lens == lent:
            buf = 0
            for i in range(lens):
                if s[i] != t[i]:
                    buf += 1
            if buf > K:
                ans = "No"
        else:
            kiroku_s = [0] * 26
            kiroku_t = [0] * 26
            for i in range(lens):
                kiroku_s[ord(s[i]) - ord("a")] += 1
            for i in range(lent):
                kiroku_t[ord(t[i]) - ord("a")] += 1
            buf = 0
            for i in range(26):
                if kiroku_s[i] != kiroku_t[i]:
                    buf += 1
            if buf > K:
                ans = "No"
print(ans)
