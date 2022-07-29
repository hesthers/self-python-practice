## 10845 & 18258 x
import sys; from collections import deque
que = list(); 
for i in range(int(input())):
    cases = input().split()
    if len(cases) == 2: que.append(int(cases[1]))
    else:
        if cases[0] == 'pop': 
            if que == []: print(-1) 
            else: print(que[0]); que = que[1:]
        elif cases[0] == 'size': print(len(que))
        elif cases[0] == 'front': 
            if len(que) == 0: print(-1)
            else: print(que[0])
        elif cases[0] == 'back': 
            if len(que) == 0: print(-1)
            else: print(que[-1])
        else:
            if len(que) == 0: print(1)
            else: print(0)

#-------------------------------
## 2164
num = int(input()); que = [i for i in range(1, num+1)]
while True:
    que.pop(0); que.append(que[0]); que.pop(0); print(que)
    if len(que) == 1: print(que[0]); break

from collections import deque; que = deque()
def que_card(num): 
    for i in range(1, num+1): 
        que.append(i)
    while True:
        que.popleft(); que.append(que[0]); que.popleft()
        if len(que) == 1: return que[0]; break        
que_card(int(input()))

##<correction>##
from collections import deque; que = deque(); num = int(input());
for i in range(1, num+1): que.append(i)
while len(que) > 1:
    que.popleft(); que.append(que[0]); que.popleft(); 
print(que[0])

#----------------------------------
## 10103
cases = [list(map(int, input().split())) for i in range(int(input()))]; c_sc = 100; s_sc = 100
for cs in cases:
    c, s = cs
    if c > s: s_sc -= c
    elif c < s: c_sc -= s
    else: pass
print(c_sc); print(s_sc)

#----------------------------------
## 3046 
r1, s = map(int, input().split()); r2 = 2 * s - r1; print(r2)

#-----------------------------------
## 10039
score = [0] * 5
for i in range(5):
    j = int(input()); score[i] = j
    if j < 40: score[i] = 40
    else: continue
print(sum(score)//5)

#---------------------------
## 11651
for s in sorted([list(map(int, input().split()))
                 for i in range(int(input()))],
                key = lambda x: (x[1], x[0])):
    x, y = s; print(x, y)

#------------------------
## 11866
from collections import deque; que = deque(); perm = []; n, k = map(int, input().split());
for i in range(1, n+1): que.append(i)
while True:
    if k > 2:
        if len(que) >= k:
            perm.append(que[k-1]); que.rotate(-k+1); que.popleft();
        if len(que) == k-1: perm.append(que[0]); que.popleft()
        elif len(que) == 1: perm.append(que[0]); break
        elif len(que) < k-1: que.rotate(-k+len(que)+1); perm.append(que[0]); que.popleft()
    else:
        if len(que) > 1: perm.append(que[k-1]); que.rotate(-k+1); que.popleft();
        elif len(que) == 1: perm.append(que[0]); break
print(f'<{", ".join(map(str, perm))}>')

#--------------------------
## 1676 
n = int(input()); f = 1; cnt = 0
for i in range(1, n+1): f *= i;
for i in range(len(str(f))-1, -1, -1):
    if str(f)[i] != '0': break
    else: cnt += 1
print(cnt)

#----------------------------
## 1037 
n = int(input()); cases = sorted(list(map(int, input().split())))
if n % 2 == 0: print(cases[0] * cases[-1])
else: print(cases[0] * cases[-1])

#---------------------------
## 2581 
m, n= map(int, [input().strip() for i in range(2)]);
cases = [k for k in range(2, n+1)]; j = 0
for cnt in range(2, int(n**(1/2))+1):
    for i in range(j, len(cases), cnt):
        if (cnt != cases[i]): cases[i] = 0; cnt += 1
    j += 1
prime = [c for c in cases if (c != 0) & (c >= m)]
if prime == []: print(-1)
else:
    print(sum(prime))
    print(min(prime))

## 1978 
n = int(input()); prime = [0] * n; j = 0; prime_no = []
for i, j in zip(range(n), map(int, input().split())): prime[i] = j;
cases = [k for k in range(2, max(prime)+1)]; j = 0
for cnt in range(2, int(max(prime)**(1/2))+1):
    for i in range(j, len(cases), cnt):
        if (cnt != cases[i]): cases[i] = 0; cnt += 1
    j += 1
answer = [c for c in cases for p in prime if (c != 0) & (c == p)]
print(len(answer))

## 2960 
n, k = map(int, input().split()); non_prime = []
cases = [k for k in range(2, n+1)]; j = 0
for cnt in range(2, n+1):
    for i in range(j, len(cases), cnt): non_prime.append(cases[i]); cases[i] = 0
    j += 1
non_prime = [np for np in non_prime if np != 0]
print(non_prime[k-1])

## 1929 
m, n= map(int, input().split());
cases = [k for k in range(2, n+1)]; j = 0
for cnt in range(2, int(n**(1/2))+1):
    for i in range(j, len(cases), cnt):
        if (cnt != cases[i]): cases[i] = 0; cnt += 1
    j += 1
prime = [c for c in cases if (c != 0) & (c >= m)]
for p in prime: print(p)

## 11653
n = int(input()); cases = [k for k in range(2, n+1)]; j = 0
for cnt in range(2, int(n**(1/2))+1):
    for i in range(j, len(cases), cnt):
        if (cnt != cases[i]): cases[i] = 0; cnt += 1
    j += 1
prime = [c for c in cases if c != 0]
prime_no = []
for pn in prime:
    while n % pn == 0:
        n //= pn; prime_no.append(pn)
for p in prime_no: print(p)
''' 시간초과 풀이
for c in cases:
    if c != 0:
        while n % c == 0:
            n //= c; prime_no.append(c)
for p in prime_no: print(p) '''

#----------------------------
## 2475 
cases = list(map(lambda x: int(x) ** 2, input().split())); print(sum(cases) % 10)
#---------------------------
## 11728
n, m = map(int, input().split()); a = [0] * n; b = [0] * m
for i, j in zip(range(n), list(map(int, input().split()))): a[i] = j
for i, j in zip(range(m), list(map(int, input().split()))): b[i] = j
for data in sorted(a+b): print(data, end = ' ')
'''
merged_list = a + b
def sorted_list(list_data):
    for idx in range(len(list_data)):
        for j in range(len(list_data)-idx-1):
            if list_data[j] > list_data[j+1]:
                list_data[j], list_data[j+1] = list_data[j+1], list_data[j]
    return list_data
sorted_list(merged_list)'''

#------------------------
## 2752 
from collections import deque
cases = deque()
for c in list(map(int, input().split())): cases.append(c)
for data in sorted(cases): print(data, end = ' ')

#---------------------------
## 11399 
def sort_data(data_list):
    if len(data_list) <= 1: return data_list

    pivot = data_list[0]; left=[]; right = [];
    for dl in data_list[1:]:
        if dl <= pivot: left.append(dl)
        else: right.append(dl)

    return sort_data(left)+[pivot]+sort_data(right)

n_cases = [0 for i in range(int(input()))]
for nc, val in zip(range(len(n_cases)), list(map(int, input().split()))): n_cases[nc] = val
n_cases = sort_data(n_cases)
times, tot_time = 0, 0
for nc in n_cases: times += nc; tot_time += times
print(tot_time)

'''from itertools import combinations;
n = [0 for i in range(int(input()))]
for idx, j in zip(range(len(n)), list(map(int, input().split()))): n[idx] = j
cases = combinations(n, len(n))
for c in cases: print(c)'''

#------------------------------
## 11726 
def rectangle(num):
    rect = [0 for i in range(num)]
    if 0 < num <= 2: rect[num-1] = num; #return rect[num-1]
    #for n in range(2): rect[n] = n+1
    if num > 2:
        for i in range(2): rect[i] = i+1
        for i in range(3, num+1): rect[i-1] = rect[i-2] + rect[i-3]
       # rect[num-1] = rect[num-2] + rect[num-3]
    return rect[num-1] % 10007
print(rectangle(int(input())))

#----------------------------
## 9461 
test_case = list(map(int, [input().strip() for i in range(int(input()))]))
def pado_seq(num):
    pado = [0 for n in range(100)]
    for i in range(3): pado[i] = 1
    if num >= 3:
        for n in range(3, num+1): pado[n-1] = pado[n-3] + pado[n-4]
    return pado[num-1]
for tc in test_case: print(pado_seq(tc))
pado_seq(3)
'''
for tc in test_case:
    pado = [0 for n in range(tc)]
    pado[0] = 1; pado[1] = 1; pado[2] = 1
pado = [0 for n in range(1)]
for i in range(3): pado[i] = 1'''

#----------------------------
## 1904 
# correction
def tiles(n):
    cases = [0] * (n+1)
    cases[1] = 1;
    if n >= 2:
        cases[1] = 1; cases[2] = 2
        for idx in range(3, len(cases)):
            cases[idx] = (cases[idx-1] + cases[idx-2]) % 15746
    return cases[n]
print(tiles(int(input())))
'''
def tiles(n):
    cases = [0 for i in range(n)]
    for idx in range(len(cases)):
        if idx < 2: cases[idx] = idx + 1
        else: cases[idx] = cases[idx-1] + cases[idx-2]
    return (cases[n-1]%15746)

def tiles(n):
    if n <= 2:
        return n
    return ((tiles(n-1) + tiles(n-2))%15746)

def tiles(n):
    cases = [0] * 1000000
    cases[0] = 1; cases[1] = 2
    for idx in range(2, len(cases)): cases[idx-1] = (cases[idx-2] + cases[idx-3]) % 15746
    return cases[n] '''
