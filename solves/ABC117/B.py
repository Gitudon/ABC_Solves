N = int(input())
L = list(map(int, input().split()))

# sum(L)-max(L)>max(L)を式変形
if sum(L) > 2 * max(L):
    print("Yes")
else:
    print("No")
