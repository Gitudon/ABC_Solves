X = int(input())

uresisa = 0

uresisa += X // 500 * 1000
X %= 500
uresisa += X // 5 * 5
print(uresisa)
