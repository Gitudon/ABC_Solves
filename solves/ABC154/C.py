N = int(input())
A = list(map(int, input().split()))
A = set(A)
if len(A) == N:
    print("YES")
else:
    print("NO")
