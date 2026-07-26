N = int(input())
a = list(map(int, input().split()))

dictionary = {}
for i in range(N):
    koho = [a[i] - 1, a[i], a[i] + 1]
    for j in koho:
        if j not in dictionary:
            dictionary[j] = 0
        dictionary[j] += 1

max_count = 0
for key in dictionary:
    if dictionary[key] > max_count:
        max_count = dictionary[key]
print(max_count)
