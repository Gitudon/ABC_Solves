N = int(input())
A = list(map(int, input().split()))
second_largest_index = A.index(sorted(A)[-2])
print(second_largest_index + 1)
