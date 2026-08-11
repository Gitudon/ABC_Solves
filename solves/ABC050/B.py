N = int(input())
T = list(map(int, input().split()))

base = sum(T)
M = int(input())
for _ in range(M):
    P, X = map(int, input().split())
    print(base - T[P - 1] + X)
