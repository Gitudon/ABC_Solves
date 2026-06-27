N = int(input())

dictionary = {}
dictionary_rev = {}
ans = "satisfiable"
for i in range(N):
    S = input()
    if S[0] == "!":
        dictionary_rev[S] = True
    else:
        dictionary[S] = True
for key in dictionary:
    if "!" + key in dictionary_rev:
        ans = key
print(ans)
