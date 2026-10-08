A, B, C = map(int, input().split())

if A > B:
    print("Takahashi")
elif B > A:
    print("Aoki")
elif A == B:
    if C == 0:
        print("Aoki")
    else:
        print("Takahashi")
