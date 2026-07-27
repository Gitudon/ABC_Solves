M = int(input())
A = []


def base_n(num_10, n):
    str_n = ""
    while num_10:
        if num_10 % n >= 10:
            return -1
        str_n += str(num_10 % n)
        num_10 //= n
    return int(str_n[::-1])


m = str(base_n(M, 3))
for i in range(len(m)):
    for j in range(int(m[i])):
        A.append(len(m) - 1 - i)
print(len(A))
print(*A)
