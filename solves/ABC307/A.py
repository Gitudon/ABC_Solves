N = int(input())
A = list(map(int, input().split()))
i = 0
while i < 7 * N:
    B = 0
    for j in range(7):
        B += A[i]
        i += 1
    print(B)
