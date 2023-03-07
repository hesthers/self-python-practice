## 1753 o
import heapq
from collections import defaultdict

V, e = map(int, input().split())
k = int(input())
INF = int(1e9)

graph = defaultdict(list)
dist = [INF] * (V+1) # or defaultdict(list)
for _ in range(e):
        u, v, w = map(int, input().split())
        graph[u].append((v, w)) 
    
def dijkstra(beg):
    q = [(0, k)] #heapq.heappush(q, (0, k))
    dist[beg] = 0
    
    while q:
        weight, node = heapq.heappop(q)
        if dist[node] < weight:
            continue
        for dn in graph[node]:
            cost = weight + dn[1]
            if cost < dist[dn[0]]:
                dist[dn[0]] = cost; heapq.heappush(q, (cost, dn[0]))
    
    
dijkstra(k)

for i in range(1, V+1):  
        if k == i: print(0)
        elif dist[i] == INF : print("INF")
        else: print(dist[i])
        
## 2075 o
import heapq

n = int(input()); arr = []

for _ in range(n):       
    for v in list(map(int, input().split())):
        if len(arr) < n:
                heapq.heappush(arr, v)

        elif len(arr) == n:
            min_val = arr[0]
        
            if v < min_val: continue
            else: heapq.heappop(arr); heapq.heappush(arr, v)

print(heapq.heappop(arr))

#---------------------
## 2178 o
def GetOutMaze(n, m, M):
        answer = [[0 for i in range(m)] for j in range(n)]

        dx, dy = [0, 1, -1, 0], [1, 0, 0, -1]    # 방향을 나타내는 이동방향 (시계방향)
        Q = [(0, 0)] # 시작점 좌표 저장
        
        answer[0][0] = 1        

        while Q:
                x, y = Q.pop(0)        

                if x == n-1 and y == m-1:
                        return answer[x][y]     

                for _ in range(4):  # 상하좌우 방향을 나타냄.
                        X, Y = x+dx[_], y+dy[_]

                        # 해당 지도의 범위를 벗어나는 경우 계산 안하고 넘어가기(건너뛰기)
                        if  X < 0 or X >= n or Y < 0 or Y >= m: 
                                continue
                        
                        else:
                                if M[X][Y] == 1:   
                                        if answer[X][Y] == 0: 
                                                Q.append((X, Y))
                                                answer[X][Y] = answer[x][y] + 1
            

n, m = map(int, input().split())
maze = [[v for v in list(map(int, input()))] for _ in range(n)]

print(GetOutMaze(n, m, maze))

## 16234 o
n, l, r = map(int, input().split())
P = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
        for j, val in zip(range(n), list(map(int, input().split()))):
                P[i][j] = val


def ppl_mvm(x, y):
        dx, dy = [0, 1, -1, 0], [1, 0, 0, -1] 

        Q = [(x, y)]; coord = [(x, y)]
        
        # 국가 간의 연합 확인하기 (BFS)
        while Q:
                x, y = Q.pop(0)         

                for _ in range(4): 
                        X, Y = x+dx[_], y+dy[_]

                        if 0 <= X < n and 0 <= Y < n and country[X][Y] == 1:       
                                if l <= abs(P[X][Y] - P[x][y]) <= r:
                                        country[X][Y] = 0
                                        Q.append((X, Y)); coord.append((X, Y))

        return coord

days = 0
while True:
        f = True
        country = [[1 for i in range(n+1)] for j in range(n+1)] 
        
        for i in range(n):
                for j in range(n):        
                        if country[i][j] == 1:
                                country[i][j] = 0
                                coord = ppl_mvm(i, j)
                                
                        if len(coord) > 1 or country[i][j] == 1:
                                f = False

                                ppl = sum([P[x][y] for x, y in coord])

                                for x, y in coord:
                                        P[x][y] = ppl // len(coord)

        if f: break
        days += 1

print(days)

## 2502 o
'''
문제 풀이 원리
# 1 2 1+2 2+3 3+5 5+8 ...
# a b a+b b+a+b
# i >= 3 
# R[3] = R[2] + R[1]
# R[4] = R[3] + R[2] = (R[2] + R[1]) + R[2]             = 2R[2] + R[1]
# R[5] = R[4] + R[3] = (2R[2] + R[1]) + (R[2] + R[1])   = 3R[2] + 2R[1]
# R[6] = R[5] + R[4] = (3R[2] + 2R[1]) + (2R[2] + R[1]) = 5R[2] + 3R[1]
# R[7] = R[6] + R[5] = (5R[2] + 3R[1]) + (3R[2] + 2R[1]) = 8R[2] + 5R[1]
# R[8] = R[7] + R[6] = (8R[2] + 5R[1]) + (5R[2] + 3R[1]) = 13R[2] + 8R[1]
# (1, 0) (0, 1) (1, 1) (1, 2) (2, 3) (3, 5) (5, 8) (8, 13)
'''
d, k = map(int, input().split())
R = [0 for _ in range(30+1)]; cnt_arr = []
R[1], R[2] = 'a', 'b'
cnt_arr.extend([(0, 0), (1, 0), (0, 1)])

for i in range(3, 30+1):
        R[i] = R[i-1] + R[i-2]
        a_cnt = R[i].count('a'); b_cnt = R[i].count('b')
        cnt_arr.append((a_cnt, b_cnt))

a, b = cnt_arr[d]

rice_cake = []; x = 1
while True: 
        if (k - a*x) % b == 0:
                y = (k - a*x) // b; rice_cake.append((x, y))
        x += 1
        if k - a*x < 0 or x > (k - a*x) // b: break

for i in rice_cake[-1]:
        print(i)
    
## 4447 o
for _ in range(int(input())):
        nm = input(); hero = nm.lower()

        if hero.count('g') > hero.count('b'):
                print(f'{nm} is GOOD')

        elif hero.count('g') < hero.count('b'):
                print(f'{nm} is A BADDY')

        elif (hero.count('g') == 0 and hero.count('b') == 0) or hero.count('g') == hero.count('b'):
                        print(f'{nm} is NEUTRAL')

## 2161 o
# if문이 먼저 안오면 인덱스 오류남.
n = int(input())
cards = [i for i in range(1, n+1)]
while True:
    if len(cards) == 1: print(cards[0]); break
    print(cards.pop(0), end=' ')
    cards.append(cards.pop(0))

## 10858 o
for _ in range(int(input())):
    v, e = map(int, input().split())
    print(2+e-v)
    
## 2605 o
from collections import deque
que = deque(); n = int(input()); cnt = 1
order = list(map(int, input().split()))
while order:
    o = order.pop(0)
    if cnt == 1: que.append(cnt)
    else:
      que.insert(o, cnt)
    cnt += 1
que.reverse()
print(*que)

## 2522 o
n = int(input())
for i in range(1, n+1):
    print(' ' * (n-i)+ '*'*i)
for j in range(n-1, 0, -1):
    print(' ' * (n-j)+'*'*j)
    
## 5523 o
cnt_a, cnt_b = 0, 0
for _ in range(int(input())):
        a, b = map(int, input().split())
        if a > b: cnt_a += 1
        elif a < b: cnt_b += 1
print(cnt_a, cnt_b)

## 9085 o
for _ in range(int(input())):
    cnt = int(input())
    print(sum(list(map(int, input().split()))))
    
## 2460 o
ppl, max_ppl = 0, 0
for _ in range(10):
        get_off, take = map(int, input().split())
        ppl -= get_off; ppl += take; max_ppl = max(ppl, max_ppl)
print(max_ppl)

## 7785 o
company = []
for _ in range(int(input())):
    name, state = input().split()
    if state == 'leave': company.pop(company.index(name))
    else: company.append(name)
for c in sorted(company, reverse=True):
    print(c)
    
## 3058 o
for _ in range(int(input())):
    data = list(map(int, input().split()))
    data = list(filter(lambda x: x%2==0, data))
    print(sum(data), min(data))

## 4458 o
for _ in range(int(input())):
    w = input()
    for idx, s in enumerate(w.split()):
        if idx == 0: print(s[0].capitalize()+s[1:], end=' ') #첫 글자만 대문자로 변환하기 주의 (나머지는 소문자, 만약 나머지 글자도 대문자라면???)
        else: print(s, end=' ')
    print('', end='\n')
    
## 5522 o
print(sum([int(input()) for _ in range(5)]))

## 10179 o
for _ in range(int(input())):
    price = float(input())
    print('${:.2f}'.format(price*0.8))

## 2947 o
arr = list(map(int, input().split()))
while True:
    for i in range(5-1):
        if arr[i] > arr[i+1]: arr[i], arr[i+1] = arr[i+1], arr[i]; print(*arr)
        else: pass
    
    if arr != [1, 2, 3, 4, 5]: continue
    else: break

## 6376 o
import math
e = 0
print('n', 'e')
print('-','-'*11)

for _ in range(10):
    e += 1/math.factorial(_)
    if e - int(e) == 0: print(_, int(e))
    elif _ == 2: print(_, e)
    else: print(_, '{:.9f}'.format(e))
    
## 15688 o
import heapq
n = []

for _ in range(int(input())):
    num = int(input())
    heapq.heappush(n, num)
    
for _ in range(len(n)):
    print(heapq.heappop(n))

## 8974 o
# sys.stdin.readline으로 python3 계산 시 빠름
# 자연수의 합 => 자연수 합이 1000개일 때 마지막 값은 44~45사이
a, b = map(int, input().split())
cnt = [0]
for i in range(1, 45+1):
    cnt += [i] * i

print(sum(cnt[a:b+1]))

## 18870 o
n = int(input())

coord = list(map(int, input().split()))
comp = {v: k for k, v in enumerate(sorted(list(set(coord))))}

print(*[comp[c] for c in coord])

## 6321 o
alpha = {chr(k):chr(v) for k, v in zip(range(ord('A'), ord('Z')), range(ord('A')+1, ord('Z')+1))}
alpha.update({'Z': 'A'})

for _ in range(int(input())):
    nm = input()
    print(f'String #{_+1}')
    for n in nm:
        print(alpha[n], end='')
    print()
    print()

## 5704 o
while True:
    alp = {chr(k): 0 for k in range(ord('a'), ord('z')+1)}
    sents = input().replace(' ', '')
    
    if sents == '*': break

    for s in sents:
        alp[s] += 1

    if list(alp.values()).count(0) >= 1: print('N')
    else: print('Y')
    
## 23972 o
# x-n*(x-k)>=0 
# nk / (n-1) >= x

k, n = map(int, input().split())

if n-1 == 0: print(-1)
else: 
    x = (k*n)//(n-1)
    if (k*n)%(n-1) == 0: print(x)
    else: print(x+1)
    
## 25501 o
def recursion(s, l, r):
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)
    
def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

for _ in range(int(input())):  
    s = input()  
    print(isPalindrome(s), end = ' ')

    l, r = 0, len(s)-1
    cnt = 1
    while True:
        if l >= r or s[l] != s[r]: break
        else: cnt += 1; l += 1; r -= 1
    print(cnt, end='\n')
    
## 1806 o
'''
import sys
n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))'''
n, s = map(int, input().split())
arr = list(map(int, input().split()))

sum_arr, s_a = [0], 0
for a in arr:
    s_a += a
    sum_arr.append(s_a)

beg, idx, min_len = 0, 0, int(1e9)
while True:
    if sum_arr[idx]-sum_arr[beg] >= s:
        min_len = min(min_len, idx-beg)
        beg += 1
        
    else:
        if idx < n: idx += 1
        else: break
    
    if beg > idx: break
    
if min_len == int(1e9): print(0)
else: print(min_len)

## 10768 o
m, d = map(int, [input() for _ in range(2)])
if m < 2: print('Before')
elif m == 2:
    if d < 18: print('Before')
    elif d == 18: print('Special')
    else: print('After')
else: print('After')
