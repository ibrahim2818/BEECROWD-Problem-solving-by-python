x = int(input())

hours = abs(x // 3600)
minutes = abs((x % 3600) // 60)
seconds = abs(x % 60)

print(f"{hours:02}:{minutes:02}:{seconds:02}")
