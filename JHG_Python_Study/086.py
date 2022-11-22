a = int(input())
s = 0
c = 1

while True:
    s += c
    c += 1
    
    if s >= a:
        break
    
print(s)
