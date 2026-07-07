N = int(input())
A = [0] * N
for i in range(N):
    A[i] = int(input())

B = sorted(A)
max_value = B[-1]
sesond_max_value = B[-2]

for i in range(N):
    if A[i] == max_value:
        print(sesond_max_value)
    else:
        print(max_value)
