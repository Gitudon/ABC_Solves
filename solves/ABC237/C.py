def is_kaibun(S):
    return S == S[::-1]


S = input()
if is_kaibun(S):
    print("Yes")
else:
    a_count_front = 0
    a_count_back = 0
    i = 0
    while i < len(S) and S[i] == "a":
        a_count_front += 1
        i += 1
    j = len(S) - 1
    while j >= 0 and S[j] == "a":
        a_count_back += 1
        j -= 1
    if a_count_front > a_count_back:
        print("No")
    else:
        S = S[a_count_front : len(S) - a_count_back]
        if is_kaibun(S):
            print("Yes")
        else:
            print("No")
