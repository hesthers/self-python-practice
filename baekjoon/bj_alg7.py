## 1568 o
k = 1; n = int(input()); cnt = 0
while True:
    if n < k: k = 1; n -= k; k += 1; cnt += 1
    else: n -= k; k += 1; cnt += 1
    if n == 0: break
print(cnt)

#-----------------
## 1302 o
books = [input().strip() for i in range(int(input()))]
print(sorted(books, key = lambda x: (-books.count(x), x))[0])

#-------------------
## 1260 o
from collections import deque
n, m, pt = map(int, input().split())
data = {k: [] for k in range(1, n+1)}
graphs = [list(map(int, input().strip().split())) for i in range(m)]
for k, v in data.items():
    for g in graphs:
        if k == g[0]: data[k].append(g[1])
        if k == g[1]: data[k].append(g[0])
    data[k] = sorted(data[k])

def dfs_code(data, first_node):
    vi_que = deque(); visit = deque()

    visit.append(first_node)

    while visit:
        graph_node = visit.pop()
        if graph_node not in vi_que:
            vi_que.append(graph_node)
            visit.extend(sorted(data[graph_node], reverse=True))

    return list(vi_que)

def bfs_code(data, first_node):
    vi_que = deque(); visit = deque()

    visit.append(first_node)

    while visit:
        graph_node = visit.popleft()
        if graph_node not in vi_que:
            vi_que.append(graph_node)
            visit.extend(data[graph_node])

    return list(vi_que)

print(*dfs_code(data, pt))
print(*bfs_code(data, pt))

#---------------------
## 2606 o
from collections import deque
n, m = map(int, [input().strip() for i in range(2)])
data = {k: [] for k in range(1, n+1)}
graphs = [list(map(int, input().strip().split())) for i in range(m)]
for k, v in data.items():
    for g in graphs:
        if k == g[0]: data[k].append(g[1])
        if k == g[1]: data[k].append(g[0])
    data[k] = sorted(data[k])

def virus(graph_data, first_node):
    vi_que = deque(); visit = deque()

    visit.append(first_node)

    while visit:
        graph_node = visit.popleft()
        if graph_node not in vi_que:
            vi_que.append(graph_node)
            visit.extend(graph_data[graph_node])

    return list(vi_que)[1:]
print(len(virus(data, 1)))

#-------------------------------------
## 11004 o
from collections import deque; import sys; que = deque()
a, k = map(int, sys.stdin.readline().split())
for i in list(map(int, sys.stdin.readline().split())): que.append(i)
print(sorted(que)[k-1])
'''
a, k = map(int, input().split())
from collections import deque; que = deque()
for i in list(map(int, input().split())): que.append(i)

#for i in range(a): que.append(0)
#for idx, j in zip(range(len(que)), list(map(int, input().split()))): que[idx] = j;

def sort_data(data_list):
        if len(data_list) <= 1: return data_list

        pivot = data_list[0]; left=[]; right = [];
        for dl in data_list[1:]:
            if dl <= pivot: left.append(dl)
            else: right.append(dl)

        return sort_data(left)+[pivot]+sort_data(right)

print(sort_data(list(que))[k-1])
sorted(que)'''

#---------------------------
## 15969 o
from collections import deque; scores = deque()
for i in range(int(input())): scores.append(0)
for idx, j in zip(range(len(scores)), list(map(int, input().split()))): scores[idx] = j;
print(max(scores) - min(scores))

#-----------------------
## 10539 o
from collections import deque; que = deque(); elements = deque()
for i in range(int(input())): que.append(0)
for idx, j in zip(range(len(que)), list(map(int, input().split()))): que[idx] = j;
el = que[0]; elements.append(el)
for q in range(1, len(que)):
    el = que[q] * (q+1) - que[q-1]*(q); elements.append(el);
print(*elements)

#----------------------------
## 17269 o
n, m = map(int, input().split()); a, b = map(str, input().split())
cnt_letter = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1 ,2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
alpha_dict = {chr(a):c for a, c in zip(range(ord('A'), ord('Z')+1), cnt_letter)}
from collections import deque; nm_letter = deque()
for nm_a, nm_b in zip(a, b):
    nm_letter.append(alpha_dict[nm_a]); nm_letter.append(alpha_dict[nm_b])
if len(a) > len(b):
    for i in a[len(b)-len(a):]: nm_letter.append(alpha_dict[i])
elif len(a) < len(b):
    for i in b[len(a)-len(b):]: nm_letter.append(alpha_dict[i])
def num_sum_letter(data_list):
    cnt_sum_letter = deque()
    for nl in range(len(data_list)-1):
        sum_letter = (data_list[nl]+data_list[nl+1]) % 10
        cnt_sum_letter.append(sum_letter)
    if len(cnt_sum_letter) == 2: return cnt_sum_letter
    return num_sum_letter(cnt_sum_letter)
print(f"{int(''.join(list(map(str, num_sum_letter(nm_letter)))))}%")

#----------------------------
## 17389 o
n, S = map(str, [input().strip() for i in range(2)])
tot_score, score, bonus = 0, 0, 0
for idx, s in enumerate(S):
    if 'X' == s:
        score = 0; bonus = 0;
        tot_score += score + bonus
    else:
        score = idx+1; bonus = bonus; tot_score += score + bonus; bonus += 1;
print(tot_score)

#--------------------------------
## 16165 o
from collections import deque;

n, m = map(int, input().split()); idol = dict(); quizzes = deque()

for i in range(n):
    nm, num = map(str, [input().strip() for i in range(2)])
    gr_member = [0] * int(num)
    for gm, mem_nm in zip(range(len(gr_member)), list(map(str, [input().strip() for i in range(int(num))]))):
        gr_member[gm] = mem_nm
    idol[nm] = gr_member
for i in range(m):
    ans = [input().strip() for i in range(2)]; quizzes.append((ans[0], ans[1]))

for q in quizzes:
    for gr_nm in idol.keys():
        if (q[0] in idol[gr_nm]) and (q[1] == '1'): print(gr_nm)
        elif (q[0] == gr_nm) and (q[1] == '0'):
            for j in sorted(idol[gr_nm]): print(j)
