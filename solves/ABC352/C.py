N = int(input())
titans = []
A = [0] * N
B = [0] * N
for i in range(N):
    a, b = map(int, input().split())
    titans.append((a, b))
    A[i] = a
    B[i] = b


def custom_compare(t):
    return abs(t[0] - t[1])


s_titans = sorted(titans, key=custom_compare)
ans = 0
for i in range(N - 1):
    ans += s_titans[i][0]
ans += s_titans[N - 1][1]
print(ans)
