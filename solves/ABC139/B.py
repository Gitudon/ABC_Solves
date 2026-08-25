A, B = map(int, input().split())

socket_num = 1
ans = 0
while socket_num < B:
    socket_num -= 1
    socket_num += A
    ans += 1
print(ans)
