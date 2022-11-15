## 2684 o
for _ in range(int(input())):
    a = input(); coins = [0]*8
    for i in range(len(a)-2):
        if a[i:i+3] == 'TTH': coins[1] += 1
        elif a[i:i+3] == 'THT': coins[2] += 1
        elif a[i:i+3] == 'THH': coins[3] += 1
        elif a[i:i+3] == 'HTT': coins[4] += 1
        elif a[i:i+3] == 'HTH': coins[5] += 1
        elif a[i:i+3] == 'HHT': coins[6] += 1
        elif a[i:i+3] == 'HHH': coins[7] += 1
        else: coins[0] += 1
    print(*coins)

## 10990 o
h = int(input())
for i in range(1, h+1):
    if i >= 2: print(' '*(h-i)+'*'+' '*(2*i-3)+'*')
    else: print(' '*(h-i)+'*')

## 10811 o
n, m = map(int, input().split())
basket = [b for b in range(1, n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    basket[i-1:j] = basket[i-1:j][::-1]
print(*basket)

## 10707 o
a, b, c, d, p = map(int, [input().rstrip() for _ in range(5)])
x, y = a*p, 0
if p <= c: y += b
else: y += b + (p-c) * d

if x <= y: print(x)
else: print(y)

## 7523 o
for _ in range(int(input())):
    print(f"Scenario #{_+1}:")
    n, m = map(int, input().split())
    hap = (n+m)*(m-n+1)//2
    print(hap)
    print()
    
## 11944 o
n, m = input().split(); answer = n*int(n)
print(answer[:int(m)])

## 3062 o
for _ in range(int(input())):
    num = input()
    chg_num = str(int(num) + int(num[::-1])) 
    if chg_num == chg_num[::-1]: print('YES')
    else: print('NO')
    
## 1748 o
import math
n = input(); p = 9
if int(n) < 10: print(int(n))
else:
    for i in range(1, int(math.log10(int(n)))+1):
        if len(n)-1 == i: p += (int(n) - (10**i) + 1) * len(n)
        else: p += 90*(10**(i-1)) * (i+1)
    print(p)

## 9094 o
for _ in range(int(input())):
    n, m = map(int, input().split()); cnt = 0
    for a in range(1, n):
        for b in range(a, n):
            if a < b and (a**2+b**2+m) % (a*b) == 0:
                cnt += 1
    print(cnt)

## 5618 o
def aliqot(num):
    aliq = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            if num // i == i: aliq.append(i)
            else:
                aliq.append(i); aliq.append(num // i)
    return aliq

def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

n = int(input())
nums = list(map(int, input().split()))
if n == 2:
    for a in sorted(aliqot(gcd(nums[0], nums[1]))): print(a)
else:
    if gcd(nums[0], nums[1]) == gcd(nums[1], nums[2]) == gcd(nums[0], nums[2]):
        for a in sorted(aliqot(gcd(nums[0], nums[1]))): print(a)
    else:
        for a in sorted(list(set(aliqot(nums[0])) & set(aliqot(nums[1])) & set(aliqot(nums[2])))):
            print(a)

## 15649 o
n, m = map(int, input().split())
arr, s, visit = [], [], [0]*(n+1)

def backtrack_comb(cnt):
    if m == cnt:
        arr.append(s[:])
        return 

    for w in range(1, n+1):
        if visit[w] != 1:
            s.append(w)
            visit[w] = 1
            backtrack_comb(cnt+1)
            visit[w] = 0
            s.pop()
    
    return arr

for bc in backtrack_comb(0):
    print(*bc)

## 1788 o
def fibo_minus(num):
    f, s = 0, 1; m_f, m_s = f, s-f

    if num < 0:
        for _ in range(2, abs(num)+1):
            m_f, m_s = m_s, m_f - m_s
        return m_s
    
    else:
        for _ in range(2, num+ 1):
            f, s = s, f + s
        return m_s if num < 0 else 0 if num == 0 else s

f_n = fibo_minus(int(input()))
print(-1 if f_n < 0 else 0 if f_n == 0 else 1)
print(abs(f_n)%1000000000)

## 9742 o
from itertools import permutations
import math

while True:
    try:
        word, c = input().split(); c = int(c)
        for i, perm in enumerate(permutations(word, len(word))):
            if i == c-1:
                print(f"{word} {c} = {''.join(perm)}")
        if c > math.factorial(len(word)):
            print(f"{word} {c} = No permutation")

    except:
        pass; break

## 10864 o
n, m = map(int, input().split())
friends = {i: [] for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)
friends = dict(sorted(friends.items(), key=lambda x:x))

for v in friends.values():
    print(len(v))
    
''' extra code - BFS
def student_friends(v, graph):
    f, relation = [], []
    relation.append(v)
    while relation:
        v = relation.pop(0)
        if v not in f:
            f.append(v)
            for i in graph[v]:
                relation.append(i)
    # f.pop(0)
    return f
for _ in range(1, n+1):
    print(student_friends(_, friends))'''
    
## 1731 o
elements = [int(input()) for _ in range(int(input()))]

if elements[-1] % elements[-2] == 0:
    ratio = elements[-1] // elements[-2]  
    print(elements[-1] * ratio)    
else:
    diff = elements[-1] - elements[-2]
    print(elements[-1] + diff)
    
## 2846 o
n, arr = int(input()), list(map(int, input().split()))

from collections import defaultdict
over_roads=defaultdict(list); cnt = 1; max_size = 0

for a in range(len(arr)-1):
    if arr[a+1] > arr[a]: 
        over_roads[cnt].extend([arr[a], arr[a+1]])
    else: over_roads[cnt].append(arr[a]); cnt += 1

for v in over_roads.values():
    max_size = max(max(v)-min(v), max_size)

print(max_size)

## 1715 o
import heapq

arr = list(map(int, [input() for _ in range(int(input()))]))

h = []
for i in range(len(arr)):
    heapq.heappush(h, arr[i])

card_cnt = 0
if len(h) == 1: print(0)
else:
    while True:
        card = heapq.heappop(h)
        card += heapq.heappop(h)
        card_cnt += card
        heapq.heappush(h, card)
        if len(h) == 1: break
    print(card_cnt)
