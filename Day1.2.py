# problem : https://codeforces.com/group/c3FDl9EUi9/contest/262795/problem/C
n = int(input())

digits = list(map(int, input().split()))
digits.sort()
print(*digits)
