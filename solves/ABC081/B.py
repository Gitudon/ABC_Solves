N = int(input())
A = list(map(int, input().split()))


def gusu(A):
    for a in A:
        if a % 2 == 1:
            return False
    return True


ans = 0
while gusu(A):
    A = [a // 2 for a in A]
    ans += 1
print(ans)
