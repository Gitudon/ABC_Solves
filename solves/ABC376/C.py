N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B)

if min(B) < min(A):
    print(-1)
    exit()

ans = -1
flag = False
for i in range(1, N + 1):
    if i == N:
        if not flag:
            ans = A[0]
        break
    if A[-i] > B[-i]:
        if not flag:
            ans = A[-i]
            if i == 1:
                B = B + [ans]
            else:
                B = B[:-i] + [ans] + B[-i:]
            flag = True
        else:
            ans = -1
            break
print(ans)
