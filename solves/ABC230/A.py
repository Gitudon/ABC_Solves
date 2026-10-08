N = int(input())

if N >= 42:
    print("AGC0" + str(N + 1))
elif 10 <= N < 42:
    print("AGC0" + str(N))
else:
    print("AGC00" + str(N))
