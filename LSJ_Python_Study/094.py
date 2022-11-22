a = 100000
n = int(input())
c = input().split()

for i in c:
    print(int(i))
    if int(i) < a:
        a = int(i)
        
print(a)
