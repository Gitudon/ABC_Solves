N = input()

N_elem = []
for n in N:
    N_elem.append(int(n))

N_elem.sort(reverse=True)

N_digit = len(N_elem)
ans = 0


def make_number(elements):
    if elements == []:
        return 0
    number = ""
    for element in elements:
        number += str(element)
    return int(number)


def bit_full_search(group_1, group_2, cnt):
    global ans
    if cnt == N_digit:
        group_1.sort(reverse=True)
        group_2.sort(reverse=True)
        res = make_number(group_1) * make_number(group_2)
        ans = max(ans, res)
        return
    bit_full_search(group_1 + [N_elem[cnt]], group_2, cnt + 1)
    bit_full_search(group_1, group_2 + [N_elem[cnt]], cnt + 1)


bit_full_search([], [], 0)
print(ans)
