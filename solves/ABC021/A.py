N = int(input())
a = [
    [1, 1],
    [1, 2],
    [2, 1, 2],
    [1, 4],
    [2, 1, 4],
    [2, 2, 4],
    [3, 1, 2, 4],
    [1, 8],
    [2, 1, 8],
    [2, 2, 8],
]
for i in range(1, 11):
    if i == N:
        for j in range(len(a[i - 1])):
            print(a[i - 1][j])
