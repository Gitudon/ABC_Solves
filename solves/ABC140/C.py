N = int(input())
B = list(map(int, input().split()))

A = [B[-1]]
for i in range(1, N - 1):
    if B[-i] >= B[-(i + 1)]:
        A = [B[-(i + 1)]] + A
    else:
        A = [B[-i]] + A

A = [B[0]] + A
print(sum(A))
