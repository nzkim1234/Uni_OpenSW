d = []

for i in range(10):
    d.append([])
    for j in range(10):
        d[i].append(0)

for i in range(10):
    d[i] = list(map(int, input().split()))

print(d)
x = 1
y = 1

while True:
    d[x][y] = 9
    if d[x][y] == 2:
        break
    if d[x][y+1] != 1:
        y += 1
    else:
        if d[x+1][y] != 1:
            x += 1
        else:
            break

for i in range(10):
    for j in range(10):
        print(d[i][j], end = ' ')
    print()
