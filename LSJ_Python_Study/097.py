a = []
h, w = map(int, input().split())

for i in range(h):
    a.append([])
    for j in range(w):
        a[i].append(0)
n = int(input())

for i in range(n):
    l, d, x, y = map(int, input().split())
    for j in range(l):
        a[x-1][y-1] = 1
        if d == 0:
            y += 1
        else:
            x += 1
            
for i in range(h):
    for j in range(w):
        print(a[i][j], end = ' ')
    print()
