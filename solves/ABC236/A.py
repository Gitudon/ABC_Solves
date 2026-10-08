S = input()
a, b = map(int, input().split())

c = S[a - 1]
d = S[b - 1]

print(S[: a - 1] + d + S[a : b - 1] + c + S[b:])
