## 11723 o
# 대입값 = int형일 때, clear를 안쓰면 정답처리...(???)
import sys; s = set()
for _ in range(int(sys.stdin.readline())):
    set_cal = sys.stdin.readline().split()
    if len(set_cal) == 2: 
        cal, num = set_cal; num = int(num)
        if cal == 'add':
            if num in s: pass
            else: s.add(num)
        
        elif cal == 'check':
            if num in s: print(1)
            else: print(0)

        elif cal == 'remove':
            s.discard(num)

        elif cal == 'toggle':
            if num in s:
                s.discard(num)
            else:
                s.add(num)

    else: 
        cal = set_cal[0]
        if cal == 'all':
            s = set(); s.update({i for i in range(1, 20+1)})

        else:
            s = set()
            
## 15989 o
test_cases = list(map(int, [input().strip() for i in range(int(input()))]))
def sum_123(num):
    arr = [0 for i in range(num+1)]
    for i in range(1, num+1): arr[i] = i 
    for idx in range(4, len(arr)):
        arr[idx] = arr[idx-3] + idx//2+1
    return arr[num]
for tc in test_cases: print(sum_123(tc))

## 11721 o
word = input()
for w in range(0, len(word), 10):
    print(word[w:w+10])
    
## 9243 o 
n = int(input())
before, after = [list(input()) for _ in range(2)]

for _ in range(n):
    for i in range(len(before)):
        if before[i] == '1': before[i] = '0'
        else:  before[i] = '1'

print('Deletion succeeded' if before == after else 'Deletion failed')

## 11931 o
arr = []
import heapq

for _ in range(int(input())):
    heapq.heappush(arr, int(input()))

for a in sorted(arr, reverse=True):
    print(a)
    
## 10570 o
import heapq
for _ in range(int(input())):
    arr, cnt = [], []

    for i in range(int(input())):
        heapq.heappush(arr, int(input()))
    
    max_cnt = arr.count(arr[0])
    for a in set(arr):
        max_cnt = max(arr.count(a), max_cnt)

    for a in arr:
        if arr.count(a) == max_cnt:
            heapq.heappush(cnt, a)

    print(heapq.heappop(cnt))

## 4101 o
while True:
    n1, n2 = map(int, input().split())
    if n1 == 0 and n2 == 0: pass; break
    if n1 > n2: print('Yes')
    else: print('No')

## 4963 o
dx, dy = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]
def num_islands(x, y):
    if x < 0 or x >= h or y < 0 or y >= w or maps[x][y] != 1: 
        return

    maps[x][y] = 0
    for _ in range(8): 
        num_islands(x+dx[_], y+dy[_])


while True: 
    w, h = map(int, input().split())
    maps = [[0 for _ in range(w)] for _ in range(h)]
    if w == 0 and h == 0: pass; break

    for i in range(h):
        for j, v in zip(range(w), list(map(int, input().strip().split()))):
            maps[i][j] = v

    cnt = 0
    for x in range(h):
        for y in range(w):
            if maps[x][y] == 1: 
                num_islands(x, y)
                cnt += 1
    print(cnt)
    
## 10804 o
cards = [i for i in range(1, 20+1)]
for _ in range(10):
    a, b = map(int, input().split())
    cards[a-1:b] = cards[a-1:b][::-1]
print(*cards)

## 2563 o
paper = []; max_x, max_y = 0, 0
for _ in range(int(input())):
    x, y = map(int, input().split())
    paper.append([x, y])
    max_x, max_y = max(x, max_x), max(y, max_y)

color_paper = [[0 for i in range(max_x+11)] for j in range(max_y+11)]

for w, h in paper:
    for b in range(h, h+10):
        for a in range(w, w+10):
            if color_paper[b][a] == 1: pass
            else: color_paper[b][a] = 1

cnt = 0
for i in color_paper:
    cnt += i.count(1)
print(cnt)

## 9020 o
# pypy3으로 해야 시간초과 안됨.
def prime_num(num):
    num_arr = [_ for _ in range(2, num+1)]; v = 0
    for i in range(2, int(num**0.5)+1):
        for j in range(v, len(num_arr), i):
            if i != num_arr[j]: num_arr[j] = 0
        v += 1
    num_arr = [n for n in num_arr if n != 0]
    return num_arr

import heapq
for _ in range(int(input())):
    n = int(input()); prime_arr, diff = prime_num(n), []; answer = []

    if n == 0: pass; break
    for i in prime_arr:
        if i <= n and n - i in prime_arr: 
            heapq.heappush(answer, i)
        if i == n-i: heapq.heappush(answer, i)

    for a in range(len(answer)//2):
        diff.append((n-answer[a])-answer[a])
    
    min_diff = min(diff)
    for a in range(len(answer)//2):
        if (n-answer[a])-answer[a] == min_diff: print(answer[a], (n-answer[a]))
        
## 4948 o
def prime_num(num):
    num_arr = [_ for _ in range(2, num*2+1)]; v = 0
    for i in range(2, int((num*2)**0.5)+1):
        for j in range(v, len(num_arr), i):
            if i != num_arr[j]: num_arr[j] = 0
        v += 1
    num_arr = [n for n in num_arr if n != 0 and num < n <= num*2]
    return num_arr

while True:
    n = int(input())
    if n == 0: pass; break
    print(len(prime_num(n)))
    
## 2864 o
a, b = map(int,input().split())
min_a, max_a, min_b, max_b = a, a, b, b

if '5' in str(a) or '5' in str(b):
    new_a5 = int(str(a).replace('5', '6'))
    new_b5 = int(str(b).replace('5', '6'))
else: new_a5 = a; new_b5 = b

if '6' in str(a) or '6' in str(b):
    new_a6 = int(str(a).replace('6', '5'))
    new_b6 = int(str(b).replace('6', '5'))
else: new_a6 = a; new_b6 = b

min_a = min(a, new_a5, new_a6); min_b = min(b, new_b5, new_b6)
max_a = max(a, new_a5, new_a6); max_b = max(b, new_b5, new_b6)
min_hap = min_a + min_b; max_hap = max_a + max_b
print(min_hap, max_hap)

## 2303 o
from collections import defaultdict

def choose_3(arr):
    answer = []; max_sum = 0
    for i in range(len(arr) - 1):
        l = i + 1

        while True:
            r = len(arr) - 1
            if l == r: break
            while True:
                if l == r: break
                card_arr = [arr[i], arr[l], arr[r]]
                if card_arr in answer: pass
                else: answer.append(card_arr)
                r -= 1 
            l += 1
        
        for a in answer:
            max_sum = max(sum(a)%10, max_sum)

    return max_sum

game = defaultdict(int)
for _ in range(int(input())):
    cards = list(map(int, input().split()))
    game[_+1] = choose_3(cards)

max_cards = max(game.values()) 
max_num = sorted([k for k, v in game.items() if v == max_cards], reverse=True)
print(max_num[0])
