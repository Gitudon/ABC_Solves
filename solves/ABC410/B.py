N, Q = map(int, input().split())
X = list(map(int, input().split()))

boxes = [0] * N
balls = [0] * Q

for i in range(Q):
    if X[i] >= 1:
        boxes[X[i] - 1] += 1
        balls[i] = X[i]
    else:
        saisyo = min(boxes)
        for j in range(N):
            if boxes[j] == saisyo:
                boxes[j] += 1
                balls[i] = j + 1
                break

print(*balls)
