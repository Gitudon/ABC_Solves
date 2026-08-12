H = ["H", "2B", "3B", "HR"]
S = [input() for _ in range(4)]
H.sort()
S.sort()
if H == S:
    print("Yes")
else:
    print("No")
