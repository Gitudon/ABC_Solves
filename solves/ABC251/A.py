S = input()

a = len(S)
if a == 1:
    print(S + S + S + S + S + S)
elif a == 2:
    print(S + S + S)
else:
    print(S + S)
