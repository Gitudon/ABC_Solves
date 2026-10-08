V, A, B, C = map(int, input().split())

a = V // (A + B + C)
for i in range(1, a + 2):
    if V < A:
        print("F")
        break
    V -= A
    if V < B:
        print("M")
        break
    V -= B
    if V < C:
        print("T")
        break
    V -= C
