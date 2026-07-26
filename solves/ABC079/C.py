def solve(numbers, operators):
    ans = numbers[0]
    for i in range(len(operators)):
        if operators[i] == "+":
            ans += numbers[i + 1]
        else:
            ans -= numbers[i + 1]
    return ans


ABCD = input()
numbers = []
for i in range(len(ABCD)):
    numbers.append(int(ABCD[i]))
plamai = "+-"
for i in range(2):
    for j in range(2):
        for k in range(2):
            operators = [plamai[i], plamai[j], plamai[k]]
            if solve(numbers, operators) == 7:
                print(
                    str(numbers[0])
                    + operators[0]
                    + str(numbers[1])
                    + operators[1]
                    + str(numbers[2])
                    + operators[2]
                    + str(numbers[3])
                    + "=7"
                )
                exit()
