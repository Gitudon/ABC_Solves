Q = int(input())
stack = [0] * 100

for i in range(Q):
    query = input().split()
    if int(query[0]) == 1:
        x = int(query[1])
        stack = [x] + stack
    elif int(query[0]) == 2:
        print(stack[0])
        stack = stack[1:]
