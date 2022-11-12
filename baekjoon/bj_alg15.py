## 10178 o
for _ in range(int(input())):
    c, v = map(int, input().split())
    print(f'You get {c//v} piece(s) and your dad gets {c%v} piece(s).')

## 10984 o
for _ in range(int(input())):
    total_gr, total_gpa = 0, 0
    for _ in range(int(input())):
        gr, gpa = map(float, input().split())
        total_gpa += gr * gpa; total_gr += gr
    print('{} {:.1f}'.format(int(total_gr), total_gpa/total_gr))
    
## 11656 o
S = input()
suffix=sorted([S[s:] for s in range(len(S))])
for s in suffix:
    print(s)
    
## 10173 o
while True:
    sents = input()
    
    if sents == 'EOI': pass; break
    else:
        if 'nemo' in sents.lower(): print('Found')
        else: print('Missing')
        
## 2702 o
for _ in range(int(input())):
    a, b = map(int, input().split()); prod_ab = a * b
    while b > 0:
        a, b = b, a%b
    print(prod_ab//a, a)
    
## 2774 o
for _ in range(int(input())):
    beauty = {i for i in input()}
    print(len(beauty))

## 3059 o
alpha = [chr(i) for i in range(ord('A'), ord('Z')+1)]
for _ in range(int(input())):
    s = input(); non_str = []; sum_str = 0
    for a in alpha:
        if a in s: pass
        else: non_str.append(a)
    for ns in non_str:
        sum_str += ord(ns)
    print(sum_str)
    
#------------------------------
## 10867 o
n = int(input()); cases = [0] * n
for _, i in zip(range(n), list(map(int, input().split()))):
    cases[_] = i
print(*sorted(list(set(cases))))

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

## 2789 o
word = input(); answer = ''
for w in word:
    if w in 'CAMBRIDGE': pass
    else: answer += w
print(answer)

## 2754 o
from collections import defaultdict

score = ['A', 'B', 'C', 'D']; sign = ['+', '0', '-']
grade = defaultdict() 

for g, v in zip(score, range(4, 0, -1)): 
    for s in sign:
        if s =='+': v += 0.3
        else: v -= 0.3
        grade[g+s] = round(v, 1)

grade.update({'F':0.0})
print('{:.1f}'.format(grade[input()]))

## 10866 o
from collections import deque; import sys
deq = deque()
for _ in range(int(sys.stdin.readline().rstrip())): 
    inp = sys.stdin.readline().rstrip()
    if ' ' in inp:
        order, num = inp.split(' ')
        if order == 'push_back':
            deq.append(int(num))
        else: deq.appendleft(int(num))
    else: 
        if inp == 'pop_front':
            if len(deq) == 0: print(-1)
            else: print(deq.popleft())
        elif inp == 'pop_back':
            if len(deq) == 0: print(-1)
            else: print(deq.pop())
        elif inp == 'size':
            print(len(deq))
        elif inp == 'empty':
            if len(deq) == 0: print(1)
            else: print(0)
        elif inp == 'front':
            if len(deq) == 0: print(-1)
            else: print(deq[0])
        else:
            if len(deq) == 0: print(-1)
            else: print(deq[-1])

## 5656 o
cnt = 0
while True:
    a, cal, b = input().split()
    a, b = int(a), int(b)  ## important!!!
    if cal == 'E': pass; break
    else:
        if cal == '>':
            cnt += 1
            if a > b: print(f'Case {cnt}: true')
            else: print(f'Case {cnt}: false')
        elif cal == '>=':
            cnt += 1
            if a >= b: print(f'Case {cnt}: true')
            else: print(f'Case {cnt}: false')
        elif cal == '<':
            cnt += 1
            if a < b: print(f'Case {cnt}: true')
            else: print(f'Case {cnt}: false')
        elif cal == '<=':
            cnt += 1
            if a <= b: print(f'Case {cnt}: true')
            else: print(f'Case {cnt}: false')
        elif cal == '==':
            cnt += 1
            if a == b: print(f'Case {cnt}: true')
            else: print(f'Case {cnt}: false')
        else:
            cnt += 1
            if a != b: print(f'Case {cnt}: true')
            else: print(f'Case {cnt}: false')

## 4504 o
n = int(input())
while True:
    num = int(input())
    if num == 0: pass; break
    if num % n == 0:
        print(f'{num} is a multiple of {n}.')
    else:
        print(f'{num} is NOT a multiple of {n}.')

## 2442 o
n = int(input())
for i in range(1, n+1):
    print(' ' * (n-i) +'*'*(2*i-1))
    
## 5054 o
for i in range(int(input())):
    t = int(input()); cases = sorted(list(map(int, input().split())))
    
    distance = [0] * t
    distance[0] = cases[-1] - cases[0]
    
    for j in range(1, len(cases)):
        distance[j] = cases[j] - cases[j-1]
    print(sum(distance))
    
## 2587 o
case = [int(input()) for _ in range(5)]

print(sum(case)//5)
print(sorted(case)[5//2])

## 2309 o
from itertools import combinations, permutations
height = [int(input().rstrip()) for _ in range(9)]

seven_dwarves = [sorted(i) for i in permutations(height, 7) if sum(i) == 100]
for i in seven_dwarves[0]: print(i)

## 3040 o
from itertools import combinations, permutations
hats = [int(input().rstrip()) for _ in range(9)]

seven_dwarves = [i for i in permutations(hats, 7) if sum(i) == 100]
for i in seven_dwarves[0]: print(i)

## 5218 o
alphabets = {chr(k): v for k, v in zip(range(ord('A'), ord('Z')+1), range(1, 26+1))}

for _ in range(int(input())):
    print('Distances: ', end = '')
    w1, w2 = input().split()

    for x, y in zip(w1, w2):
        if alphabets[x] <= alphabets[y]: print(alphabets[y] - alphabets[x], end=' ')
        else: print(alphabets[y] + 26 - alphabets[x], end=' ')
    print(end='\n')
    
#---------------------------
## 1789 o
S = int(input()); s = 0; max_val = 1
for i in range(1, S+1):
    s += i
    if s > S: break
    else: max_val = max(max_val, i)
print(max_val)

## 2948 o
import datetime
wd = {w: n for w, n in zip(range(7), ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])}
d, m = map(int, input().split())
print(wd[datetime.date(2009, m, d).weekday()])

## 1924 o
import datetime
wd = {w: n for w, n in zip(range(7), ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])}
x, y = map(int, input().split())
print(wd[datetime.date(2007, x, y).weekday()])

## 5800 o
for _ in range(int(input())):
    students = list(map(int, input().split()))
    cnt = students[0]; grades = sorted(students[1:])
    max_grade, min_grade, gap = max(grades), min(grades), 0
    
    for g in range(len(grades)-1):
        gap = max(grades[g+1]-grades[g], gap)

    print(f'Class {_+1}')
    print(f'Max {max_grade}, Min {min_grade}, Largest gap {gap}')

[O## 9076 o
for _ in range(int(input())):
    five_grades = sorted(list(map(int, input().split())))
    max_g = five_grades[-1]; min_g = five_grades[-1]
    gr_adj = five_grades[-2] - five_grades[1]
    if gr_adj >= 4: print('KIN')
    else: print(sum(five_grades[1:-1]))

## 11170 o
for _ in range(int(input())):
    n, m = map(int, input().split()); cnt_0 = 0
    for i in range(n, m+1):
            cnt_0 += str(i).count('0')
    print(cnt_0)
    
## 5585 o
p = int(input()); chg, money_cnt = 1000 - p, 0
for c in [500, 100, 50, 10, 5, 1]:
    money_cnt += chg // c
    chg = chg - (chg // c * c)
print(money_cnt)

## 10599 o
while True:
    a, b, c, d = map(int, input().split())
    if a == 0 and b == 0 and c == 0 and d == 0: pass; break
    max_age = d - a; min_age = c - b
    print(min_age, max_age)

## 5176 o
for _ in range(int(input())):
    p, m = map(int, input().split())
    champ = []
    for i in range(p):
        part = int(input())
        if part in champ: pass
        else: champ.append(part)
    print(p-len(champ))

## 3449 o
for _ in range(int(input())):
    p, m = map(str, [input().rstrip() for _ in range(2)]); hamming = 0
    for i in range(len(p)):
        if p[i] != m[i]: hamming += 1
    print(f'Hamming distance is {hamming}.')
    
## 10829 o
print(bin(int(input()))[2:])

## 5347 o
def gcd(a, b):
    while True:
        if b > 0: a, b = b, a % b
        else: break
    return a

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(a*b//gcd(a, b))
    
## 2511 o
a = list(map(int, input().split())); b = list(map(int, input().split()))
A_score, B_score, rnd = 0, 0, []

for i, j, _ in zip(a, b, range(10)):
    if i > j: A_score += 3; rnd.append([_+1, 'A'])
    elif i < j: B_score += 3; rnd.append([_+1, 'B'])
    else: A_score += 1; B_score += 1

print(A_score, B_score)

if A_score > B_score: print('A')
elif A_score < B_score: print('B')
else:
    if len(rnd) == 0: print('D')
    else:
        if rnd[-1][1] == 'A': print('A')
        else: print('B')
        
## 2440 o
for i in range(int(input()), 0, -1):
    print('*'*i)
    
## 4084 o
while True:
    a, b, c, d = map(int, input().split()); cnt = 0
    if a == b == c == d == 0: pass; break
    if a == b == c == d: print(0)
    else:
        while True:
            a, b, c, d = abs(a-b), abs(b-c), abs(c-d), abs(d-a)
            if a == b == c == d: cnt += 1; print(cnt); break
            else: cnt += 1
            
## 12780 o
h, n = [input().rstrip() for i in range(2)]
print(h.count(n))
