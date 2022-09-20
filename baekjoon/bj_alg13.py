## 24086 o
a, b = map(int, [input().strip() for _ in range(2)]); print(b-a)

## 4714 o
while True:
    weight = float(input())
    if weight < 0: pass; break
    else: print('Objects weighing {:.2f} on Earth will weigh {:.2f} on the moon.'.format(weight, weight*0.167))

## 6778 o
antenna, eyes = map(int, [input().strip() for _ in range(2)])
if antenna >= 3 and eyes <= 4: print('TroyMartian')
if antenna <= 6 and eyes >= 2: print('VladSaturnian')
if antenna <= 2 and eyes <= 3: print('GraemeMercurian')
else: pass

## 11943 o
a, b = map(int, input().split())
c, d = map(int, input().split())
print(min(a+d, b+c))

## 2501 o
n, k = map(int, input().split()); prime_n = [0] * (n+1)
for i in range(1, int(n**(0.5))+1):
    if n % i == 0: prime_n[i] = i; prime_n[n//i] = n//i
    else: pass
prime_n = [i for i in prime_n if i != 0]
if len(prime_n) >= k: print(prime_n[k-1])
else: print(0)

## 1350 o
files = [0 for i in range(int(input()))]
for idx, f in zip(range(len(files)), list(map(int, input().split()))): files[idx] = f
clusters = int(input()); space = 0
for f in files:
    if f != 0: 
        if f >= clusters:
            if f % clusters == 0: space += f // clusters
            else: space += (f // clusters + 1)
        else:
            if clusters % f == 0: space += (f // clusters + 1)
            else: space += (f // clusters + 1)
       
print(space* clusters)

## 2476 o
prize_money = []
for _ in range(int(input())):
    c1, c2, c3 = map(int, input().split())
    if c1 == c2 == c3: prize_money.append(10000 + c1 * 1000)
    elif c1 == c2 != c3: prize_money.append(1000 + c1 * 100)
    elif c2 == c3 != c1: prize_money.append(1000 + c2 * 100)
    elif c1 == c3 != c2: prize_money.append(1000 + c3 * 100)
    else: prize_money.append(max(c1, c2, c3) * 100)
print(max(prize_money))

## 1834 o
N = int(input()); M = 0
for a in range(1, N):
    M += a * (N+1)
print(M)

## 5335 o
for _ in range(int(input())):
    tn = input().split(); tn_val = float(tn[0])
    for t in tn[1:]:
        if t == '@': tn_val *= 3
        elif t == '%': tn_val += 5
        else: tn_val -= 7
    print('{:.2f}'.format(tn_val))
    
## 10162 o
t = int(input()); a, b, c = 0, 0, 0
m, s = t // 60, t % 60; a += m // 5; b += m % 5; c += s // 10
if t <= 60:
    if t % 10 == 0: print(a, b, c)
    else: print(-1)

elif t <= 300:
    if s % 10 == 0: 
        if m < 5: print(a, b, c)
        else: print(a, b, c)
    else: print(-1)

else:
    if m % 5 == 0: 
        if s % 10 == 0: print(a, b, c) 
        else: print(-1)
    else:
        if s % 10 == 0: print(a, b, c) 
        else: print(-1)

## 2566 o
matrix = [[0 for i in range(9)] for j in range(9)]
for a in range(9):
    for b, n in zip(range(9), list(map(int, input().split()))):
        matrix[a][b] = n

max_val = 0; idx = []
for i in range(9):
    max_val = max(max(matrix[i]), max_val)
print(max_val)

for i in range(9):
    for j in range(9):
        if matrix[i][j] == max_val: idx.append([i+1, j+1])
print(*idx[0])

## 1769 o
x = input(); cnt = 0
while True:
    if len(str(x)) == 1: 
        print(cnt); break
    else: 
        y = 0; cnt += 1
        for i in x: y += int(i)
        x = str(y)
if cnt == 0: y = int(x)
if y == 3 or y == 6 or y == 9: print('YES')
else: print('NO')

'''x = input(); cnt = 0
while True:
    y = 0
    for i in x: y += int(i)
    x = str(y); cnt += 1
    if len(str(x)) == 1: break
print(cnt)
if y % 3 == 0 and y != 1: print('YES')
else: print('NO')'''

## 5565 o
price = int(input()); buy_price = 0
for _ in range(9):
    buy_price += int(input())
print(price - buy_price)

## 2490 o
for _ in range(3):
    play = list(map(int, input().split()))
    d = play.count(1); b = play.count(0)
    if d == 3 and b == 1: print('A')
    elif d == 2 and b == 2: print('B')
    elif d == 1 and b == 3: print('C')
    elif d == 4: print('E')
    else: print('D')

## 1977 o
m, n = map(int, [input().strip() for _ in range(2)])
perfect_double = [0] * (n+1)
for i in range(int(m**0.5), int(n**0.5)+1):
    if i**2 // i == i: perfect_double[i**2] = i**2
perfect_double = [i for i in perfect_double if i != 0 and m <= i <= n]
if len(perfect_double) == 0: print(-1)
else: print(sum(perfect_double)); print(min(perfect_double))

## 1408 o
h1, m1, s1 = map(int, input().split(':')) # 현재 시간
h2, m2, s2 = map(int, input().split(':')) # 시작 시간

if s2 - s1 < 0:
    s = (60+s2)-s1

    if m2 - m1 <= 0: 
        m = (60+m2)-m1-1

        if h2 - h1 <= 0: h = (24 + h2)-h1-1
        else: h = h2-h1-1

    else: 
        m = m2-m1-1

        if h2 - h1 < 0: h = (24 + h2)-h1
        else: h = h2-h1

else: 
    s = s2-s1

    if m2 - m1 < 0: 
        m = (60+m2)-m1

        if h2 - h1 <= 0: h = (24 + h2)-h1-1
        else: h = h2-h1-1

    else: 
        m = m2-m1

        if h2 - h1 < 0: h = (24 + h2)-h1
        else: h = h2-h1

if 0 <= h < 10: h = "0"+str(h)
else: h = str(h)

if 0 <= m < 10: m = "0"+str(m)
else: m = str(m)

if 0 <= s < 10: s = "0"+str(s)
else: s = str(s)

print(f'{h}:{m}:{s}')

# ---------------------------------
## 2921 o
from itertools import combinations_with_replacement
domino = [i for i in range(int(input())+1)]; points = 0
for _ in combinations_with_replacement(domino, 2):
    points += sum(_)
print(points)

## 2693 o
for _ in range(int(input())):
    arr = sorted(list(map(int, input().split())), reverse=True)
    print(arr[2])
    
#--------------------------------
## 9325 o
for _ in range(int(input())):
    s = int(input()); opts = 0
    for i in range(int(input())):
        q, p = map(int, input().split())
        opts += q * p
    print(s + opts)
    
## 1951 o
'''DP 사용시 메모리 초과됨'''
n = input(); cnt_num = 0
for i in range(1, len(n)+1):
    if int(n) // 10**(i-1) < 10:
        cnt_num += len(n) * (int(n) - 10**(i-1) + 1)
    else: cnt_num += i * (9*10**(i-1))
print(cnt_num)
