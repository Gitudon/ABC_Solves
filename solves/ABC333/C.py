N = int(input())

repunit_sums = set()

repunits = [0] * 12
for i in range(12):
    repunits[i] = int("1" * (i + 1))

for i in range(12):
    for j in range(12):
        for k in range(12):
            repunit_sum = repunits[i] + repunits[j] + repunits[k]
            repunit_sums.add(repunit_sum)

repunit_sums = sorted(repunit_sums)

print(repunit_sums[N - 1])
