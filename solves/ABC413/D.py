def is_geometric_sequence(A):
    if A.count(A[0]) == len(A):
        return True
    if (
        A.count(A[0]) + A.count(-A[0]) == len(A)
        and min(A.count(A[0]), A.count(-A[0])) == N // 2
    ):
        return True
    for i in range(len(A) - 2):
        if A[i] * A[i + 2] != A[i + 1] * A[i + 1]:
            return False
    return True


T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(A, key=abs, reverse=True)
    if is_geometric_sequence(A):
        print("Yes")
    else:
        print("No")
