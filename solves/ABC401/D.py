n, k = map(int, input().split())
s = input()
n = len(s)
cnt = s.count("o")
ans = [None] * n

for i in range(n):
    if s[i] == "o":
        ans[i] = "o"
    if s[i] == ".":
        ans[i] = "."
    if i and ans[i - 1] == "o":
        ans[i] = "."
    if i < n - 1 and s[i + 1] == "o":
        ans[i] = "."

cnt2 = 0
tmp = 0
st = -1
if k == ans.count("o"):
    for i in range(n):
        if ans[i] == None:
            ans[i] = "."
    print("".join(ans))
    exit()

a = []
for i in range(n):
    if ans[i] == None:
        if st == -1:
            st = i
        tmp += 1
    else:
        if tmp == 0:
            continue
        cnt2 += (tmp + 1) // 2
        a.append((st, i))
        tmp = 0
        st = -1


if tmp:
    cnt2 += (tmp + 1) // 2
    a.append((st, n))


if k < cnt + cnt2:
    for i in range(n):
        if ans[i] == None:
            ans[i] = "?"
    print("".join(ans))
    exit()


pos = 0
a.reverse()

for i in range(n):
    if a and a[-1][0] <= i < a[-1][1]:
        if (a[-1][1] - a[-1][0]) % 2 == 0:
            ans[i] = "?"
        else:
            if (i - a[-1][0]) % 2 == 0:
                ans[i] = "o"
            else:
                ans[i] = "."

    elif a and a[-1][1] == i:
        a.pop()

print("".join(ans))
