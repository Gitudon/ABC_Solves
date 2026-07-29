S_A = list(input())
S_B = list(input())
S_C = list(input())

now = "a"
while True:
    if now == "a":
        if S_A == []:
            print("A")
            break
        now = S_A[0]
        if len(S_A) != 1:
            S_A = S_A[1:]
        else:
            S_A = []
    elif now == "b":
        if S_B == []:
            print("B")
            break
        now = S_B[0]
        if len(S_B) != 1:
            S_B = S_B[1:]
        else:
            S_B = []
    elif now == "c":
        if S_C == []:
            print("C")
            break
        now = S_C[0]
        if len(S_C) != 1:
            S_C = S_C[1:]
        else:
            S_C = []
