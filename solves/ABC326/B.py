N = int(input())

buf = []
for i in range(1, 10):
    for j in range(10):
        for k in range(10):
            if i * j == k:
                buf.append(i * 100 + j * 10 + k)
buf.sort()
for b in buf:
    if b >= N:
        print(b)
        break
