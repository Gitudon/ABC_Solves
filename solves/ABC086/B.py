a, b = map(str, input().split())

arg = int(a + b)

left = 0
right = arg
ans = "No"

while left <= right:
    mid = (left + right) // 2
    if mid * mid == arg:
        ans = "Yes"
        break
    elif mid * mid < arg:
        left = mid + 1
    else:
        right = mid - 1

print(ans)
