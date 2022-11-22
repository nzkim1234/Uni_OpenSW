a, m, d, n = input().split()
a = int(a)

for i in range(int(n)-1):
    a = a * int(m) + int(d)
    
print(a)
