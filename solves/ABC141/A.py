S = input()

a = ["Sunny", "Cloudy", "Rainy"]
for i in range(3):
    if S == a[i]:
        if i == 2:
            print(a[0])
        else:
            print(a[i + 1])
