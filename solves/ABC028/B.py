S = input()

dictionary = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}

for s in S:
    dictionary[s] += 1

ans = ""
for d in dictionary:
    ans += str(dictionary[d])
    ans += " "
ans = ans[:-1]

print(ans)
