N = int(input())
A = list(map(int, input().split()))
i = 0
while i < len(A) - 1:
    if abs(A[i] - A[i + 1]) == 1:
        i += 1
    else:
        b = []
        if A[i] < A[i + 1]:
            for j in range(A[i] + 1, A[i + 1]):
                b.append(j)
        else:
            for j in range(A[i + 1] + 1, A[i]):
                b.append(j)
            b = reversed(b)
        A = A[: i + 1] + list(b) + A[i + 1 :]
        i += 1
print(*A)
