S = input()
ans = 0
focus = "A"
points = [0] * len(S)
for s in S:
    for i in range(len(S)):
        if s == S[i]:
            points[ord(s) - ord("A")] = i
            break
while focus != "Z":
    next = chr(ord(focus) + 1)
    ans += abs(points[ord(next) - ord("A")] - points[ord(focus) - ord("A")])
    focus = next
print(ans)
