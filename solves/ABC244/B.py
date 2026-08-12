N = int(input())
T = input()

# 0: x+, 1: y-, 2: x-, 3: y+
muki = 0
zahyo = [0, 0]
for i in range(N):
    if T[i] == "S":
        if muki == 0:
            zahyo[0] += 1
        elif muki == 1:
            zahyo[1] -= 1
        elif muki == 2:
            zahyo[0] -= 1
        else:
            zahyo[1] += 1
    elif T[i] == "R":
        muki = (muki + 1) % 4
print(zahyo[0], zahyo[1])
