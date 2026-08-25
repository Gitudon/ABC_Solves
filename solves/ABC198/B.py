N = input()

zero_count = 0
i = -1
while N[i] == "0" and i > -len(N):
    zero_count += 1
    i -= 1
ans = "No"
N = "0" * zero_count + N
if N == N[::-1]:
    ans = "Yes"
print(ans)
