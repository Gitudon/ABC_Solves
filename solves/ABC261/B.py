N = int(input())
A = [input() for i in range(N)]
ans = 0
for i in range(N):
    for j in range(N):
        if A[i][j] == "D" and A[j][i] != "D":
            ans += 1
        elif A[i][j] == "W" and A[j][i] != "L":
            ans += 1
        elif A[i][j] == "L" and A[j][i] != "W":
            ans += 1
if ans > 0:
    print("incorrect")
else:
    print("correct")
