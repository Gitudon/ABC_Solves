N = int(input())
T = input()
A = input()

ans = "No"
for i in range(N):
    if T[i] == A[i] and T[i] == "o":
        ans = "Yes"

print(ans)
