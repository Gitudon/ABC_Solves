A = input()

if len(A) >= 2:
    print(A[:-1])
else:
    if A == "a":
        print(-1)
    else:
        print(chr(ord(A) - 1))
