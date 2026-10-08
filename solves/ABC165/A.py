K = int(input())
A, B = map(int, input().split())

c = 0
for i in range(A, B + 1):
    if i % K == 0:
        c += 1
if c >= 1:
    print("OK")
else:
    print("NG")
