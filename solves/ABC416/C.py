import itertools

N, K, X = map(int, input().split())
S = [0] * N
for i in range(N):
    S[i] = input()

f_A = []
f_A = list(itertools.product(S, repeat=K))

for i in range(len(f_A)):
    f_A[i] = "".join(f_A[i])
f_A.sort()
print(f_A[X - 1])
