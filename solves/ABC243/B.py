N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

hit = 0
blow = 0
for i in range(N):
    for j in range(N):
        if A[i] == B[j]:
            if i == j:
                hit += 1
            else:
                blow += 1
print(hit)
print(blow)
