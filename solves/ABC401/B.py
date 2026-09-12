N = int(input())

islogin = False

ans = 0
for i in range(N):
    s = input()
    if s == "login":
        islogin = True
    elif s == "logout":
        islogin = False
    elif s == "public":
        pass
    elif s == "private":
        if not islogin:
            ans += 1
