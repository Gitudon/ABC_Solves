s = list(input())
t = int(input())
n = len(s)

x = 0
y = 0
q = 0
for i in range(n):
    if s[i] == "U":
        y += 1
    elif s[i] == "D":
        y -= 1
    elif s[i] == "L":
        x -= 1
    elif s[i] == "R":
        x += 1
    else:
        q += 1
x = abs(x)
y = abs(y)
if t == 1:
    ans = x + y + q
else:
    if x + y - q >= 0:
        ans = x + y - q
    else:
        ans = (q - (x + y)) % 2
print(ans)
