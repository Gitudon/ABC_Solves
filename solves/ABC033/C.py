S = input()

# 数式を項ごとに分割する
terms = []
buf = ""
for i in range(len(S)):
    if S[i] == "+":
        terms.append(buf)
        buf = ""
    else:
        buf += S[i]
terms.append(buf)

ans = 0
for term in terms:
    if "0" not in term:
        ans += 1
print(ans)
