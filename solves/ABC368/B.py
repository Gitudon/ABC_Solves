def checker(A):
    cnt = 0
    for i in range(len(A)):
        if A[i] > 0:
            cnt += 1
        if cnt > 1:
            return False
    return True


N = int(input())
A = list(map(int, input().split()))
ans = 0
while not checker(A):
    A.sort(reverse=True)
    A[0] -= 1
    A[1] -= 1
    ans += 1
print(ans)
