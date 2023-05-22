## 9946 o
cnt = 0
while True:
    cnt += 1
    before, after = [input().rstrip() for _ in range(2)]
    if before == 'END' and after == 'END': pass; break
    before, after = sorted(list(before)), sorted(list(after))
    if len(before) != len(after):
        print(f'Case {cnt}: different')
    else:
        if before == after: print(f'Case {cnt}: same')
        else: print(f'Case {cnt}: different')
        
## 11652 o
from collections import Counter
cards=[int(input()) for _ in range(int(input()))]
c = Counter(cards)
cnt_cards = sorted(c.most_common(), key=lambda x: (-x[1], x[0]))
print(cnt_cards[0][0])

'''
시간초과 풀이
from collections import Counter; import sys
cards=[int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
c = Counter(cards)
cnt_cards = sorted(list(filter(lambda x: c[x]==max(list(c.values())), c.keys())))
print(cnt_cards[0])
'''

#------------------------------------
## 1940 o
# input()보다는 시간이 더 빠름.
import sys
n, m = map(int, [sys.stdin.readline().rstrip() for _ in range(2)])
ing = list(map(int, sys.stdin.readline().split()))

beg, cnt = 0, []
while beg <= len(ing) -1:

    idx = 0
    while idx <= len(ing)-1:
        if m - ing[beg] == ing[idx] and ing[beg] not in cnt and ing[idx] not in cnt:
            if ing[beg] == ing[idx]: pass

            else:
                cnt += [ing[beg], ing[idx]]

        idx += 1

    if beg >= idx: break
    beg += 1

print(len(cnt)//2)

## 10769 o
txt = input()
h, s = txt.count(':-)'), txt.count(':-(')
if h == 0 and s == 0: print('none')
elif h == s: print('unsure')
elif h > s: print('happy')
elif h < s: print('sad')

## 25024 o
for _ in range(int(input())):
    x, y = map(int, input().split())
    if 0 <= x <= 23:
        if 0 <= y <= 59:
            print('Yes', end= ' ')
        else: print('No', end= ' ')
    else: print('No', end= ' ')
    if 1 <= x <= 12:
        if x == 2 and 1 <= y <= 29:
            print('Yes')
        elif x in [1, 3, 5, 7, 8, 10, 12] and 1 <= y <= 31:
            print('Yes')
        elif x in [4, 6, 9, 11] and 1 <= y <= 30:
            print('Yes')
        else: print('No')
    else: print('No')

## 3004 o
n = int(input())
if n % 2 == 0:
    print((n-((n-2)//2))**2)
else:
    print((n+1)//2 *((n+1)//2+1))

## 2740 o
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(m)]

multi_mat = [[0 for _ in range(k)] for _ in range(n)]

for i in range(n):
    for j in range(k):
        for c in range(m):
            multi_mat[i][j] += a[i][c] * b[c][j]

for mm in multi_mat:
    print(*mm)

#################################
## 5666 o
while True:
    try:
        h, p = map(int, input().split())
        print('{:.2f}'.format(h/p))
    except: pass; break

## 11006 o
for _ in range(int(input())):
    n, m = map(int, input().split())
    print(m*2-n, m-(m*2-n))
