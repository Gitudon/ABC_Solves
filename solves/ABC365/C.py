N, M = map(int, input().split())
A = list(map(int, input().split()))

if sum(A) <= M:
    print("infinite")
    exit()

A.sort()
left, right = 0, max(A)
result = 0

while left <= right:
    mid = (left + right) // 2
    total = sum(min(a, mid) for a in A)

    if total <= M:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)
