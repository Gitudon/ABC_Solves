N = int(input())
S = input()

mode = 1
ans = 1
one_length = 0
two_length = 0
for i in range(N):
    if mode == 1:
        if S[i] == "1":
            one_length += 1
        elif S[i] == "/":
            mode = 2
        else:
            one_length = 0
            two_length = 0
    elif mode == 2:
        if S[i] == "2":
            two_length += 1
        elif S[i] == "/":
            ans = max(ans, min(one_length, two_length) * 2 + 1)
            mode = 1
            one_length = 0
            two_length = 0
        else:
            ans = max(ans, min(one_length, two_length) * 2 + 1)
            mode = 1
            one_length = 1
            two_length = 0

if mode == 2:
    ans = max(ans, min(one_length, two_length) * 2 + 1)

print(ans)
