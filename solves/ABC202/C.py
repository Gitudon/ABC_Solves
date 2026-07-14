N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

max_B = max(B)
bc_count = [0] * (max_B + 1)
for i in range(N):
    bc_count[B[C[i] - 1]] += 1

ans = 0
for a in A:
    if a <= max_B:
        ans += bc_count[a]
print(ans)
