w = input()

kiroku = [0] * 26
for i in range(len(w)):
    kiroku[ord(w[i]) - ord("a")] += 1

ans = "Yes"
for i in range(26):
    if kiroku[i] % 2 != 0:
        ans = "No"

print(ans)
