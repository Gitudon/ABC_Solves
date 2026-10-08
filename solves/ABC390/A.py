A = list(map(int, input().split()))

B = sorted(A)
ans = 0
idx1 = -1
idx2 = -1
for i in range(5):
    if A[i] != B[i]:
        ans += 1
        if idx1 == -1:
            idx1 = i
        else:
            idx2 = i
if ans == 2 and abs(idx1 - idx2) == 1:
    print("Yes")
else:
    print("No")
