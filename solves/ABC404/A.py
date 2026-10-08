S = input()

alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in range(26):
    if alphabet[i] not in S:
        print(alphabet[i])
        break
