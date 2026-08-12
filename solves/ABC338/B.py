S = input()
kiroku = [0] * 26
for s in S:
    kiroku[ord(s) - ord("a")] += 1
m = max(kiroku)
for i in range(26):
    if kiroku[i] == m:
        print(chr(i + ord("a")))
        break
