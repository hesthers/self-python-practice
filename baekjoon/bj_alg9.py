## 15974 o
a, b = map(int, input().split())
def cal_ab(a, b):
    a <= 1000; b <= 1000
    return (a+b) * (a-b)
print(cal_ab(a, b))

#---------------------------------
## 5597 o
students = list(map(int, [input().strip() for i in range(28)]))
for i in range(1, 30+1):
    if i not in students: print(i)

#------------------------------
## 15829 o
l = int(input()); strings = input()
def hash_function(strings):
    m = 0
    alphabet = {chr(a):n for a, n in zip(range(ord('a'), ord('z')+1), range(1, 26+1))}
    for idx, alpha in enumerate(strings): m += alphabet[alpha]*(31**idx) 
    return m
print(hash_function(strings)%1234567891)

#-----------------------------------------
## 17219 o
n, m = map(int, input().split())
webaddr_pws = [input().split() for i in range(n)]
web_pws = {w: p for w, p in webaddr_pws}
webs = [input().rstrip() for i in range(m)]

for addr in webs: print(web_pws[addr])

## 1264 o
lower_chr = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
while True:
    sentence = input()
    if sentence == '#': break
    cnt = 0
    for lc in lower_chr:
        if lc in sentence: cnt += sentence.count(lc)
    print(cnt)

#-------------------------------
## 14489 o
a, b = map(int, input().split()); c = int(input())
if 2 * c >= a+b: print(2 * c - (a+b)) 
else: print(a+b)

#-------------------------------
## 1297 o
import math
d, h, w = map(int, input().split())
h_tv = d*(h+w)/ (h**2 + w**2)**(1/2) * h/(h+w)
w_tv = d*(h+w)/ (h**2 + w**2)**(1/2) * w/(h+w)
# print(h_tv, w_tv)
print(math.floor(h_tv), math.floor(w_tv))  

#--------------------------------
## 23278 o
n, l, h = map(int, input().split()); score = [0] * n
for i, j in zip(range(n), list(map(int, input().split()))): score[i] = j
score = sorted(score)

if h == 0:
    except_score = score[l:]
    print(sum(except_score) / len(except_score))
else:
    except_score = score[l:]; except_score = except_score[:-h]
    print(sum(except_score) / len(except_score))

from itertools import combinations
arr =[k for k in range(5)]
for j in range(1, 5+1):
    p = combinations(arr, j)
    for i in p:
        print(" ".join(map(str, i)))

## 10817 o
a, b, c = map(int, input().split())
'''
if a >= b:
    if b >= c: print(b)
    if b < c: 
        if a >= c: print(c)
        if a < c: print(a)
    
if a < b:
    if a >= c: print(a)
    if a < c: 
        if b < c: print(c)
        if b >= c: print(b)'''

print(sorted([a, b, c])[1]) #맞음

#-----------------------------------
## 1058 ?? -> o
from collections import deque
n = int(input()); friends = [[_ for _ in input()] for i in range(n)]

relationship = {i:[] for i in range(n)}
for i in range(n):
    for j in range(n):
        if friends[i][j] == 'Y': relationship[i].append(j)

def graph_relationship(data_dict, famous_person):

    friend_que = deque(); friends_2 = deque()
    friend_que.append((famous_person, 0))

    while friend_que:

        person, close_relationship = friend_que.popleft()

        for x in data_dict[person]:
            if x not in friends_2 and close_relationship < 2 and x != famous_person:
                friend_que.append((x, close_relationship+1)); friends_2.append(x)

    return len(friends_2)

c = 0; cnt_friends = [max(c, graph_relationship(relationship, i)) for i in range(n)]
print(max(cnt_friends))
'''n = int(input()); friends = [[_ for _ in input()] for i in range(n)]
relationship = {i:[] for i in range(n)}
for i in range(n):
    for j in range(n):
        if friends[i][j] == 'Y': relationship[i].append(j)
print(relationship)
def graph_relationship(data_dict):
    famous_person = sorted(data_dict.keys(), key = lambda x:len(data_dict[x]), reverse=True)[0]
    friends_2 = [_ for f2 in data_dict[famous_person] for _ in data_dict[f2] if _ != famous_person]
    for f2 in data_dict[famous_person]: friends_2.append(f2)
    return friends_2
print(graph_relationship(relationship))'''

## 1914 o
#import sys; k = int(sys.stdin.readline());
k = int(input()); tower = []
print(2 ** k - 1)

def hanoi(n, fr, to, aux):
    global tower

    if n == 1:
        tower.append((fr, to))
    else:
        hanoi(n-1, fr, aux, to)
        tower.append((fr, to))
        hanoi(n-1, aux, to, fr)
    return tower


def output(n):
    global tower
    hanoi(n, 1, 3, 2)
    return tower


if k <= 20:
    for op1, op2 in output(k): print(op1, op2)

'''def hanoi(n, fr, to, aux = 2):
    if n == 1:
        print(fr, to)
        return
    hanoi(n-1, fr, aux, to)
    print(fr, to)
    hanoi(n-1, aux, to, fr)

k = int(input())
print(2 ** k - 1)
hanoi(k, 1, 3)

tower = []
def hanoi(n, fr, to, aux):
    global tower

    if n == 1:
        tower.append([fr, to])
    elif n <= 20:
        hanoi(n-1, fr, aux, to)
        tower.append([fr, to])
        hanoi(n-1, aux, to, fr)
    else:
        hanoi(n-1, fr, aux, to)
        hanoi(n-1, aux, to, fr)
    if n <= 20: return tower
    else: pass

def output(n):
    global tower
    print(2 ** n - 1)
    hanoi(n, 1, 3, 2)
    if n <= 20: return tower
    else: pass

k = int(input())
if k <= 20:
    for op1, op2 in output(k): print(op1, op2)
else: output(k)'''

## 11729 o
import sys; k = int(sys.stdin.readline()); tower = []
print(2 ** k - 1)

def hanoi(n, fr, to, aux):
    global tower

    if n == 1:
        tower.append((fr, to))
    else:
        hanoi(n-1, fr, aux, to)
        tower.append((fr, to))
        hanoi(n-1, aux, to, fr)
    return tower


def output(n):
    global tower
    hanoi(n, 1, 3, 2)
    return tower

for op1, op2 in output(k): print(op1, op2)
