N = int(input())
X = [0] * N
Y = [0] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())


def euclid_length(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


for i in range(N):
    far = [0, 0]
    for j in range(N):
        l = euclid_length(X[i], Y[i], X[j], Y[j])
        if l > far[0]:
            far[0] = l
            far[1] = j + 1
    print(far[1])
