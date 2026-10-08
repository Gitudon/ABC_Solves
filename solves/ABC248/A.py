S = input()

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(0, 9):
    if int(S[i]) in lst:
        lst.remove(int(S[i]))
print(*lst)
