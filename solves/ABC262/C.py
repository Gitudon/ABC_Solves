N = int(input())
a = list(map(int, input().split()))

front = 0
for i in range(N):
    if a[i] == (i + 1):
        front += 1

kiroku = {}
for i in range(N):
    if a[i] not in kiroku:
        kiroku[a[i]] = [i]
    else:
        kiroku[a[i]].append(i)

back = 0
for i in range(N):
    if a[a[i] - 1] == (i + 1) and (a[i] - 1) in kiroku[i + 1]:
        back += 1

back -= front
back //= 2
print(front * (front - 1) // 2 + back)
