ABC = list(map(int, input().split()))
ABC = sorted(ABC)
if ABC[0] == ABC[1] and ABC[1] == ABC[2]:
    print("Yes")
else:
    if ABC[0] + ABC[1] == ABC[2]:
        print("Yes")
    else:
        print("No")
