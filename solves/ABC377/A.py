from itertools import permutations

S = input()

narabikae = []
for p in permutations(S):
    narabikae.append(p)
ans = []
for i in range(len(narabikae)):
    ans.append("".join(narabikae[i]))
if "ABC" in ans:
    print("Yes")
else:
    print("No")
