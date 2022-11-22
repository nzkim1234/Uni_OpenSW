r, g, b = input().split()

print(format(int(r) * int(g) * int(b) / 8 / 1024 / 1024, "0.2f"), "MB")