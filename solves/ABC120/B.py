A, B, K = map(int, input().split())

A_Divisor = []
B_Divisor = []
for i in range(1, A + 1):
    if A % i == 0:
        A_Divisor.append(i)
for i in range(1, B + 1):
    if B % i == 0:
        B_Divisor.append(i)
Common_Divisor = []
for a in A_Divisor:
    for b in B_Divisor:
        if a == b:
            Common_Divisor.append(a)
Common_Divisor.sort(reverse=True)
print(Common_Divisor[K - 1])
