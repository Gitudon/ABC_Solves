M = int(input())
D = list(map(int, input().split()))
middle = (sum(D) + 1) // 2
temp = 0
for i in range(M):
    for j in range(D[i]):
        temp += 1
        if temp == middle:
            print(i + 1, j + 1)
            exit()
