N = int(input())
A = list(map(int, input().split()))

dictionary = {}
for i in range(2**N):
    dictionary[str(i + 1)] = A[i]
numbers = [i + 1 for i in range(2**N)]
while len(numbers) > 2:
    next_numbers = []
    for i in range(0, len(numbers), 2):
        if dictionary[str(numbers[i])] < dictionary[str(numbers[i + 1])]:
            next_numbers.append(numbers[i + 1])
        else:
            next_numbers.append(numbers[i])
    numbers = next_numbers

if dictionary[str(numbers[0])] < dictionary[str(numbers[1])]:
    print(numbers[0])
else:
    print(numbers[1])
