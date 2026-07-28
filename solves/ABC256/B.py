N = int(input())
A = list(map(int, input().split()))
P = 0
mass = [0, 0, 0, 0]
for i in range(N):
    mass[0] += 1
    new_mass = [0, 0, 0, 0]
    for j in range(4):
        if j + A[i] < 4:
            new_mass[j + A[i]] += mass[j]
        else:
            P += mass[j]
    mass = new_mass
print(P)
