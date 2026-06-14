N = int(input())

a = str(N)
b = int(a[-1])

c = [2, 4, 5, 7, 9]
d = [0, 1, 6, 8]
e = [3]

if b in c:
    print("hon")
elif b in d:
    print("pon")
else:
    print("bon")
