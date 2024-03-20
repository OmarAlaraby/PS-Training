# problem : https://codeforces.com/group/c3FDl9EUi9/contest/262795/problem/B
from collections import Counter

s = input()
x = Counter(s)
l = []
for key in x.keys():
    l.append(key)

l.sort()
for i in range(len(l)):
    print(l[i], x.get(l[i]))