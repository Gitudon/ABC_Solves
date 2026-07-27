S = input()
ans = "Yes"
appeared = [0] * 26
if len(S) % 2 == 1:
    ans = "No"
for i in range(len(S) // 2):
    if S[2 * i - 2] != S[2 * i - 1]:
        ans = "No"
        break
for i in range(len(S)):
    appeared[ord(S[i]) - ord("a")] += 1
for i in range(26):
    if appeared[i] not in [0, 2]:
        ans = "No"
        break
print(ans)
