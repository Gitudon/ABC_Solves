N = int(input())
H = list(map(int, input().split()))

a = max(H)
for i in range(N):
    if H[i] == a:
        print(i + 1)
