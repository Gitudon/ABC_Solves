N, K = map(int, input().split())
S = input()

a = []
for i in range(N):
    a.append(S[i])
b = ord(a[K - 1])
a[K - 1] = chr(b + 32)
c = ""
for i in range(N):
    c += a[i]
print(c)
