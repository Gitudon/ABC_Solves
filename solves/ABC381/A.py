N = int(input())
S = input()
hantei = (N + 1) // 2
ans = "Yes"
if N % 2 == 0:
    ans = "No"
if N == 1:
    if S != "/":
        ans = "No"
else:
    for i in range(hantei - 1):
        if S[i] != "1":
            ans = "No"
            break
    for i in range(hantei, N):
        if S[i] != "2":
            ans = "No"
            break
    if S[hantei - 1] != "/":
        ans = "No"
print(ans)
