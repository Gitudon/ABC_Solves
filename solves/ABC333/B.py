alphabet = ["A", "B", "C", "D", "E"]
S1S2 = input()
T1T2 = input()
kyori1 = abs(alphabet.index(S1S2[0]) - alphabet.index(S1S2[1]))
if kyori1 == 3:
    kyori1 = 2
elif kyori1 == 4:
    kyori1 = 1
kyori2 = abs(alphabet.index(T1T2[0]) - alphabet.index(T1T2[1]))
if kyori2 == 3:
    kyori2 = 2
elif kyori2 == 4:
    kyori2 = 1
if kyori1 == kyori2:
    print("Yes")
else:
    print("No")
