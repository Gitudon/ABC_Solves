N = int(input())
A = list(map(int, input().split()))

kiroku = [0] * (2001)
for a in A:
    kiroku[a] += 1
for i in range(2001):
    if kiroku[i] == 0:
        print(i)
        break
