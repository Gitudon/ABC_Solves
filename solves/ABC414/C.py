A = int(input())
N = int(input())
ans = 0


def to_base_a(n):
    digits = []
    while n > 0:
        digits.append(str(n % A))
        n //= A
    return "".join(digits[::-1])


def is_parindrome(s):
    return s == s[::-1]


parindromes = set()

for i in range(1, 10):
    parindromes.add(i)

for i in range(1, 10**6):
    buf = int(str(i) + str(i)[::-1])
    parindromes.add(buf)
    if len(str(i)) > 5:
        continue
    for j in range(10):
        buf = int(str(i) + str(j) + str(i)[::-1])
        if buf <= N:
            parindromes.add(buf)

for p in parindromes:
    if is_parindrome(to_base_a(p)) and p <= N:
        ans += p
print(ans)
