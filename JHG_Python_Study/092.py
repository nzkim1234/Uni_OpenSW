a = []

for i in range(23):
    a.append(0)

n = int(input())
c = input().split()

for i in c:
    a[int(i)-1] += 1

for i in range(23):
    print(a[i], end =' ')
