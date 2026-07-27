S = input()
dict = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
ans = ""
for i in range(1, len(S) + 1):
    ans += dict[S[-i]]
print(ans)
