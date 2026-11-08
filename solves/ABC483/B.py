N, Q = map(int, input().split())
K = list(map(int, input().split()))

target = [i for i in range(1, N + 1)]

for i in range(Q):
    zenhan = [0] * K[i]
    kohan = target[K[i] :]
    for i in range(K[i]):
        zenhan[-(i + 1)] = -target[i]
    target = zenhan + kohan

for t in target:
    print(t)
