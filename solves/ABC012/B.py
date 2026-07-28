N = int(input())
hour = N // 3600
minute = (N % 3600) // 60
second = (N % 3600) % 60
print(f"{hour:02}:{minute:02}:{second:02}")
