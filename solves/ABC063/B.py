S = input()

part = list(set(S))

if len(part) == len(S):
    print("yes")
else:
    print("no")
