N = int(input())
A = list(map(int, input().split()))

l = []
for i in range(N):
    l.append(A[i])
    while len(l) > 1 and l[-1] == l[-2]:
        a = l[-1] + 1
        l.pop()
        l.pop()
        l.append(a)

print(len(l))
