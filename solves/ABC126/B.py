S = input()

zenhan = S[:2]
kohan = S[2:]

if 1 <= int(zenhan) <= 12:
    if 1 <= int(kohan) <= 12:
        print("AMBIGUOUS")
    else:
        print("MMYY")
elif 1 <= int(kohan) <= 12:
    print("YYMM")
else:
    print("NA")
