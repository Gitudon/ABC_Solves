S = input()
T = ""
for i in range(len(S)):
    T += chr(ord(S[i]) - 32)
print(T)
