N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))
list1 = [0] * N
list2 = [0] * N
flag = False
win = 0
for i in range(N):
    if C[i] == T:
        flag = True
        list1[i] = R[i]
    if C[i] == C[0]:
        list2[i] = R[i]
if flag:
    win = max(list1)
    for i in range(N):
        if R[i] == win:
            print(i + 1)
            exit()
else:
    win = max(list2)
    for i in range(N):
        if R[i] == win:
            print(i + 1)
            exit()
