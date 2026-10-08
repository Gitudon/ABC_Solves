N = int(input())
A = list(map(int, input().split()))

C = sorted(list(set(A)))
print(len(C))
print(*C)
