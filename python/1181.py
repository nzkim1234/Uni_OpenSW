from sys import stdin
N = int(stdin.readline())
list_dic = [stdin.readline().strip() for i in range(N)]
list_sort = sorted(set(list_dic),key=lambda x : (len(x), x))
for i in list_sort:
    print(i)
