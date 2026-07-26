A = list(map(int, input().split()))

sums = set()
for i in range(len(A)):
    for j in range(i + 1, len(A)):
        for k in range(j + 1, len(A)):
            sums.add(A[i] + A[j] + A[k])

sums = sorted(list(sums))
print(sums[-3])
