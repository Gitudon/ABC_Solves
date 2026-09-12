N = int(input())
A = list(map(int, input().split()))

kiroku = [0] * (N + 1)
for a in A:
    kiroku[a] += 1
for i in range(1, N + 1):
    if kiroku[i] == 3:
        print(i)
