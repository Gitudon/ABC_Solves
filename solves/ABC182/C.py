N = input()

len_N = len(N)
ans = -1


def bit_all_search(now, count):
    global ans
    if count == len_N:
        if now == "":
            return
        if int(now) % 3 == 0:
            if ans != -1:
                ans = min(ans, len_N - len(now))
            else:
                ans = len_N - len(now)
        return
    bit_all_search(now + N[count], count + 1)
    bit_all_search(now, count + 1)


bit_all_search("", 0)

print(ans)
