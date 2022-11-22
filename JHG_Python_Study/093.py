a = []
n = int(input())
c = input().split()

for i in c:
    a.append(i)
    
a.reverse()

for i in range(n):
    print(a[i], end=' ')
