## 11098 o
for _ in range(int(input())):
    players = [input().split() for i in range(int(input()))]
    players = sorted(players, key=lambda x: int(x[0]), reverse=True)
    print(players[0][1])

## 2010 o
import sys; n = int(sys.stdin.readline())
cnt_plugs = sum(list(map(int, [input().rstrip() for _ in range(n)])))
print(cnt_plugs-(n-1))

## 9506 o
while True:
    n = int(input()); prime_num = []

    if n == -1: pass; break

    for i in range(1, int(n**0.5)+1):
        if n % i == 0: prime_num.extend([i, n//i])
    prime_num = sorted(list(set(prime_num)))[:-1]
    
    if sum(prime_num) == n: print(f'{n} = ', end = ''); print(*prime_num, sep=' + ')
    else: print(f'{n} is NOT perfect.')
    
## 10214 o
for i in range(int(input())):
    
    y_score, k_score = 0, 0
    for _ in range(9):
        y, k = map(int, input().split())
        y_score += y; k_score += k

    if y_score > k_score: print('Yonsei')
    elif y_score < k_score: print('Korea')
    else: print('Draw')

## 7567 o
plates = input(); h = 10
for i in range(1, len(plates)):
    if plates[i-1] == plates[i]: h += 5
    else: h += 10
print(h) 

## 10820 o
while True:
    try:
        strs = input(); low, cap, num, sp = 0, 0, 0, 0
        for s in strs:
            if s.islower(): low += 1
            elif s.isupper(): cap += 1
            elif s.isdigit(): num += 1
            else: sp += 1
        print(low, cap, num, sp)
    except: break

## 2407 o
n, m = map(int, input().split())
def fact(num):
    if num > 1: return num * fact(num-1)
    else: return 1
print(fact(n) // (fact(n-m)*fact(m)))

## 5598 o
ord_val = []; idx = ord('A')
for i in range(ord('A'), ord('Z')+1):
    if i+3 > ord('Z'): ord_val.append(idx); idx += 1
    else: ord_val.append(i+3)
caesar_code = {chr(k):chr(v) for k, v in zip(ord_val,range(ord('A'), ord('Z')+1))}
for code in input():
    print(caesar_code[code], end='')
    
## 1026 o
n = int(input()); a, b = [0] * n, [0] * n; s = 0
for i, j in zip(range(n), list(map(int, input().split()))): a[i] = j
for i, j in zip(range(n), list(map(int, input().split()))): b[i] = j

for ai, bi in zip(sorted(a, reverse=True), sorted(b)): s += ai * bi
print(s)

## 1793 o
while True:
    try:
        n = int(input()); rect_ways = [0] * (250+1)
        rect_ways[0] = rect_ways[1] = 1
        for i in range(2, n+1):
            rect_ways[i] = rect_ways[i-2] * 2 + rect_ways[i-1]
        print(rect_ways[n])
    except: break

## 10801 o
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_score, b_score = 0, 0

for i, j in zip(a, b):
    if i > j: a_score += 1
    elif i < j: b_score += 1
    else: a_score += 1; b_score += 1

if a_score > b_score: print('A')
elif a_score < b_score: print('B')
else: print('D')

## 3460 o
for _ in range(int(input())):
    n = int(input()); n = str(bin(n)).replace('0b', ''); idx_bin = []
    for i, v in enumerate(n[::-1]):
        if v == '1': idx_bin.append(i)
    print(*idx_bin)

## 10991 o
N = int(input())
for i in range(N):
    print(' '*(N-(i+1))+'* '*(i+1))

## 6764 o
inp = list(map(int, [input().strip() for _ in range(4)])); inc, dec = 0, 0
for i in range(len(inp)-1):
    if inp[i] > inp[i+1]: inc -= 1; dec += 1
    if inp[i] < inp[i+1]: inc += 1; dec -= 1
    if inp[i] == inp[i+1]: inc += 20; dec -= 20

if dec == -3 and inc == 3: print('Fish Rising')
elif dec == 3 and inc == -3: print('Fish Diving')
elif dec == -60 and inc == 60: print('Fish At Constant Depth')
else: print('No Fish')

## 1159 o
nm_list, nms = [], []
for _ in range(int(input())):
    name = input()
    nm_list.append(name[0])
# nm_list = sorted(nm_list, key=lambda x:nm_list.count(x), reverse=True)
for nl in nm_list:
    if nm_list.count(nl) >= 5: nms.append(nl)
if len(nms) == 0: print('PREDAJA')
else: print(*sorted(list(set(nms))), sep='')

## 2163 o
N, M = map(int, input().split())
print(N*M-1)

## 1292 o
num_arr = [0] * (1000+1); a, b = map(int, input().split())
for i in range(44+1):
    num_arr[i + (i-1)*i//2:i + (i-1)*i//2+i+1] = [i+1]*(i+1)
print(sum(num_arr[a-1:b]))

## 8558 o
n = int(input()); val = 1
for i in range(1, n+1):
    val *= i
print(val%10)

## 2436 o
def gcd(a, b):
    if a%b == 0: return b
    return gcd(b, a%b)

n1, n2 = map(int, input().split())
min_sum = 10**9; answer = []

for i in range(int((n2*n1)**0.5)+1, 0, -1):
    a, b = i, n2*n1//i
    if n2 % i == 0 and gcd(a, b) == n1: min_sum= min(min_sum, a+b); answer.append([a,b]); i -= 1
    else: i -= 1

for ans in answer:
    if sum(ans) == min_sum: print(*ans)

## 2720 o
from collections import defaultdict

for _ in range(int(input())):
    c = int(input()); r = c; chg = defaultdict(int)

    for i in [25, 10, 5, 1]:
        m = r//i; r -= m*i
        if m >=0: chg[i] = m
        else: m = 0; chg[i] = m
    print(*chg.values())

## 4766 o
cnt = 1
while True:
    temp = float(input())
    if temp == 999: pass; break
    else:
        if cnt == 1: prev_temp = temp; cnt += 1; pass
        else: print('{:.2f}'.format(temp - prev_temp)); prev_temp = temp; cnt += 1

## 4493 o
for _ in range(int(input())):
    p1_win, p2_win = 0, 0
    for c in range(int(input())):
        p1, p2 = input().split()
        if p1 == p2: p1_win += 1; p2_win += 1
        else:
            if p1 == 'R':
                if p2 == 'P': p2_win += 1
                elif p2 == 'S': p1_win += 1

            elif p1 == 'S':
                if p2 == 'P': p1_win += 1
                elif p2 == 'R': p2_win += 1
            else:
                if p2 == 'R': p1_win += 1
                elif p2 == 'S': p2_win += 1
    if p1_win > p2_win: print('Player 1')
    elif p1_win < p2_win: print('Player 2')
    else: print('TIE')

## 2711 o
for _ in range(int(input())):
    e_idx, e_str = input().split(); words = []
    words += e_str; words.pop(int(e_idx)-1)
    print(''.join(words))

## 2935 o
noise = [input().rstrip() for _ in range(3)]
if noise[1] == '*': print(int(noise[0])*int(noise[2]))
else: print(int(noise[0])+int(noise[2]))

