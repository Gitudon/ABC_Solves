S = input()

for i in range(3):
    if S[i] == "R":
        gohan = i
    elif S[i] == "M":
        miso = i
if gohan < miso:
    print("Yes")
else:
    print("No")
