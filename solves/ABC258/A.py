K = int(input())

HH = 21 + K // 60
MM = K % 60
if MM < 10:
    MM = "0" + str(MM)
    print(str(HH) + ":" + MM)
else:
    print(str(HH) + ":" + str(MM))
