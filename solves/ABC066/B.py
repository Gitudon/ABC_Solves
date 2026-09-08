S = input()

S = S[:-1]
while True:
    if len(S) % 2 == 1:
        S = S[:-1]
    else:
        mid = len(S) // 2
        if S[:mid] == S[mid:]:
            print(len(S))
            break
        else:
            S = S[:-1]
