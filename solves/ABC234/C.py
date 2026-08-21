K = int(input())

ans = ""
while K > 0:
    if K % 2 == 1:
        ans = "2" + ans
    else:
        ans = "0" + ans
    K //= 2

print(ans)
