N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
L = int(input())
C = list(map(int, input().split()))
Q = int(input())
X = list(map(int, input().split()))

zisyo = {}
for a in A:
    for b in B:
        for c in C:
            if a + b + c not in zisyo:
                zisyo[a + b + c] = 1

for i in range(Q):
    if X[i] in zisyo:
        print("Yes")
    else:
        print("No")
