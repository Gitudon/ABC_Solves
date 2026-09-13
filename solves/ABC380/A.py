kiroku = [0] * 3
N = input()
for i in range(len(N)):
    if N[i] == "1":
        kiroku[0] += 1
    elif N[i] == "2":
        kiroku[1] += 1
    elif N[i] == "3":
        kiroku[2] += 1
if kiroku[0] == 1 and kiroku[1] == 2 and kiroku[2] == 3:
    print("Yes")
else:
    print("No")
