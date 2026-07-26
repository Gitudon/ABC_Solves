N, K = map(int, input().split())
T = [0] * N
for i in range(N):
    T[i] = list(map(int, input().split()))

ans = "Nothing"


def bit_all_search(n, xor_sum):
    global ans
    if n == N:
        if xor_sum == 0:
            ans = "Found"
        return
    for i in range(K):
        bit_all_search(n + 1, xor_sum ^ T[n][i])


bit_all_search(0, 0)
print(ans)
