N = int(input())
A = list(map(int, input().split()))

one = 0
ten = 0
hundred = 0

for a in A:
    maisu = a // 1000 + 1
    otsuri = (maisu * 1000 - a) % 1000
    hundred += otsuri // 100
    otsuri %= 100
    ten += otsuri // 10
    otsuri %= 10
    one += otsuri

print(one, ten, hundred)
