S = input()
A = [
    "tourist",
    "ksun48",
    "Benq",
    "Um_nik",
    "apiad",
    "Stonefeang",
    "ecnerwala",
    "mnbvmar",
    "newbiedmy",
    "semiexp",
]
B = [3858, 3679, 3658, 3648, 3638, 3630, 3613, 3555, 3516, 3481]
for i in range(len(A)):
    if A[i] == S:
        print(B[i])
