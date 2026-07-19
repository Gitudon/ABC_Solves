def sort_by_second(elem):
    return elem[1]


N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sweet = []
salt = []
for i in range(N):
    sweet.append((A[i], B[i]))
    salt.append((A[i], B[i]))
sweet.sort(reverse=True)
salt.sort(reverse=True, key=sort_by_second)
table1 = [0] * 3
table2 = [0] * 3
table1[0] = N
table2[0] = N
for i in range(N):
    table1[1] += sweet[i][0]
    table1[2] += sweet[i][1]
    if table1[1] > X or table1[2] > Y:
        table1[0] = i + 1
        break
for i in range(N):
    table2[1] += salt[i][0]
    table2[2] += salt[i][1]
    if table2[1] > X or table2[2] > Y:
        table2[0] = i + 1
        break
print(min(table1[0], table2[0]))
