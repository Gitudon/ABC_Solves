N = int(input())
A = list(map(int, input().split()))

if max(A) != 9:
    print(-1)
else:
    print(min(A))
