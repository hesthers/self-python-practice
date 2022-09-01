## 1629 o 
a, b, c = map(int, input().split()) 
print(pow(a, b, c))

## 2523 o
n = int(input())
for i in range(1, n+1): print('*'*i)
for j in range(n-1, 0, -1): print('*'*j)

#--------------------------------
## 10833 o
stu_app = [list(map(int,input().split())) for i in range(int(input()))]
rest = 0
for sa in stu_app:
    s, a = sa
    if a >= s:
        rest += a%s
    else: rest += a
print(rest)

#-----------------------------
## 10995 o
N = int(input())
for i in range(1, N+1):
    if i % 2 == 1:
        print(('*'+' ')*N)
    else:
        print((' '+'*')*N)

#------------------------------
## 2506 o
from collections import deque
score = deque(); tot_score = 0; cnt_score = deque()
for s in range(int(input())): score.append(0)
for i, j in zip(range(len(score)), list(map(int, input().split()))): score[i] = j

for idx in range(len(score)-1):
    if score[idx] == 0: tot_score += 0; tot_score = 0
    else:
        if score[idx] == score[idx+1]:
                tot_score += 1; cnt_score.append(tot_score)
        else:
                tot_score += 1; cnt_score.append(tot_score)

if score[-1] == 0: pass
else:
    if score[-2] == 0: cnt_score.append(1)
    else: cnt_score.append(cnt_score[-1]+1)

print(sum(cnt_score))

#------------------------------------
## 10797 o
car_nums = [list(map(int, input().strip().split())) for i in range(2)]
print(car_nums[1].count(car_nums[0][0]))

#----------------------------------
## 9295 o
cubes = [list(map(int, input().split())) for i in range(int(input()))]
for idx, c in enumerate(cubes): print(f'Case {idx+1}: {sum(c)}')

#----------------------------------------
## 2455 o
ppl = [list(map(int, input().strip().split())) for n in range(4)]
train_ppl = 0; tot_ppl = []
for pl in ppl:
    on, off = pl; train_ppl += off; train_ppl -= on
    tot_ppl.append(train_ppl)
print(max(tot_ppl))

#----------------------------------------
## 2914 o
a, I = map(int, input().split())
print(a*(I-1)+1)

#---------------------------------------------
## 2231 o
N = int(input()); min_digit = []
for j in range(N-len(str(N))*9, N+1):
    num = N - j; sum_num = 0
    if j >= 0:
        for n in str(j):
            sum_num += int(n);
        if int(N) == j + sum_num: min_digit.append(j)
if len(min_digit) == 0: print(0)
else: print(min(min_digit))
'''
N = input(); min_digit = []
for j in range(int(N)-len(N)*9, int(N)):
    num = int(N) - j; sum_num = 0
    for n in str(j):
        sum_num += int(n);
    if int(N) == j + sum_num: min_digit.append(j)
if len(min_digit) == 0: print(0)
else: print(min(min_digit)) '''

## 2738 o
n, m = map(int, input().split())
mat1 = [list(map(int, input().split())) for i in range(n)]
mat2 = [list(map(int, input().split())) for j in range(n)]
ans_mat = [[0 for _ in range(m)] for j in range(n)]
for _1 in range(n):
    for _2 in range(m):
        ans_mat[_1][_2] = mat1[_1][_2] + mat2[_1][_2] 
        
for ans in ans_mat: print(*ans)

## 1822 o
na, nb = map(int, input().split())
arr_a = {}; arr_b = {}
for idx_a in list(map(int, input().split())): arr_a[idx_a] = idx_a
for idx_b in list(map(int, input().split())): arr_b[idx_b] = idx_b

from collections import deque
result = deque()
for i in set(arr_a.values()) - set(arr_b.values()): result.append(i)

print(len(result))
if len(result) != 0: print(*sorted(result))
else: pass

## 14425 o
n, m = map(int, input().split())
set_collection = [0 for i in range(n)]; str_collection = [0 for j in range(m)]

for sc, s in zip(range(len(set_collection)), [input().strip() for i in range(n)]): set_collection[sc] = s
for stc, k in zip(range(len(str_collection)), [input().strip() for j in range(m)]): str_collection[stc] = k

set_collection = set(set_collection); hash_cnt = 0
for stc in str_collection:
    if stc in set_collection: hash_cnt += 1
print(hash_cnt)

