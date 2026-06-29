N = int(input())

zisyo = {}

for i in range(N):
    A, C = map(int, input().split())
    if C not in zisyo:
        zisyo[C] = A
    else:
        zisyo[C] = min(zisyo[C], A)

print(max(zisyo.values()))
