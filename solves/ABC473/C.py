N, K = map(int, input().split())
A = list(map(int, input().split()))

classes = [0] * K

for i in range(N):
    classes[A[i] - 1] += 1

max_member = max(classes)

ans = 0
for i in range(K):
    if classes[i] + 1 >= max_member:
        ans += 1
print(ans)
