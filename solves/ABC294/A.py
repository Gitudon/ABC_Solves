N = int(input())
A = list(map(int, input().split()))
ans = []
for i in range(N):
    if A[i] % 2 == 0:
        ans.append(A[i])
b = ""
for i in range(len(ans)):
    b += str(ans[i])
    if i != len(ans) - 1:
        b += " "
print(b)
