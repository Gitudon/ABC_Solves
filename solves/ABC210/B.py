N = int(input())
S = input()
i = 0
while S[i] == "0":
    i += 1
if i % 2 == 0:
    print("Takahashi")
else:
    print("Aoki")
