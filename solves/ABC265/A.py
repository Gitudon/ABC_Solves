X, Y, N = map(int, input().split())

a = N % 3
b = N // 3

s1 = X * a + Y * b
s2 = X * N
print(min(s1, s2))
