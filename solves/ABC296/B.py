a = ["a", "b", "c", "d", "e", "f", "g", "h"]
for j in range(8):
    S = input()
    for i in range(8):
        if S[i] == "*":
            print(a[i] + str(8 - j))
