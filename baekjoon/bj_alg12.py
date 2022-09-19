## 20492 o
N = int(input()); print(round(N * (1- 0.22)), round(N * 0.80 + N * (1 - 0.80) * (1 - 0.22)))

## 2712 o
for _ in range(int(input())):
    num, unit = input().split()
    if unit == 'kg': print('{:.4f}'.format(float(num) * 2.2046), 'lb')
    elif unit == 'lb': print('{:.4f}'.format(float(num) * 0.4536), 'kg')
    elif unit == 'l': print('{:.4f}'.format(float(num) * 0.2642), 'g')
    else: print('{:.4f}'.format(float(num) * 3.7854), 'l')

## 23080 o
k, s = [input().rstrip() for i in range(2)]; print(s[::int(k)])

## 5717 o
while True:
    M, F = map(int, input().split())
    if M == 0 and F == 0: pass; break
    else: print(M + F)
    
#----------------------------------
## 2446 o
N = int(input())
for i in range(N, 0, -1): print(' '*(N-i)+'*'*(2*i-1))
for i in range(2, N+1): print(' '*(N-i)+'*'*(2*i-1))

#-----------------------------------
## 2083 o
while True:
    name, age, weight = input().split()
    age = int(age); weight = int(weight)
    if name == '#' and age == 0 and weight == 0: pass; break
    if age > 17 or weight >= 80: print(name, 'Senior')
    else: print(name, 'Junior')
    
## 2576 o
natural_nums = list(map(int, [input().strip() for _ in range(7)]))
odd_sum = 0; odds = []
for nn in natural_nums:
    if nn % 2 == 0: pass
    else: odds.append(nn); odd_sum += nn
if len(odds) == 0: print(-1)
else: print(odd_sum); print(min(odds)) 

#-------------------------
## 11945 o
n, m = map(int, input().split())
for i in range(n): print(input()[::-1])

## 2857 o
cnt_agent = []; agents = [input() for i in range(5)]
for a in list(filter(lambda x: 'FBI' in x, agents)):
    cnt_agent.append(agents.index(a)+1)
if len(cnt_agent) == 0: print('HE GOT AWAY!')
else: print(*cnt_agent)

#-----------------------------
## 10988 o
word = input()
if word == word[::-1]: print(1)
else: print(0)

#---------------------------
## 6996 o
from collections import defaultdict
for i in range(int(input())):
    anagrams = defaultdict(list); words = input().split()
    for word in words: anagrams["".join(sorted(word))].append(word)
    if len(list(anagrams.values())[0]) == 2: print(f'{words[0]} & {words[1]} are anagrams.')
    else: print(f'{words[0]} & {words[1]} are NOT anagrams.')

## 16394 o
print(int(input()) - 1946)

#---------------------------
## 2721 o
def tri_num(n):
    tn = [0] * (300+2); wn = [0] * (300+1)
    tn[1] = wn[0] = 1; tn[2] = tn[1] + 2; wn[1] = tn[2] * 1
    for i in range(3, n+2):
        tn[i] += tn[i-1] + i
        wn[i-1] += (i-1) * tn[i] + wn[i-2]
    return wn[n]
for _ in range(int(input())):
    n = int(input()); print(tri_num(n))
    
## 2154 o
new_n = ''; n = input()
for i in range(1, 10**5+1): new_n += str(i)
print(new_n.find(n)+1)

#-----------------------
## 3273 o
from collections import defaultdict
case_dict = defaultdict(list); n = int(input()); cases = [0] * n; case_cnt = []
for idx, j in zip(range(len(cases)), list(map(int, input().split()))): cases[idx] = j
x = int(input())
for i, n in enumerate(cases):
    case_dict[n] = i
    if x - n in case_dict and case_dict[x-n] != i: case_cnt.append((case_dict[x-n], i))    
print(len(case_cnt))

#--------------------
## 3003 o
k, q, l, b, kn, p = map(int, input().split())
print(1-k, 1-q, 2-l, 2-b, 2-kn, 8-p)

#-----------------------------
## 1271 o
n, m = map(int, input().split())
for _ in divmod(n, m): print(_)

## 5543 o
burger = list(map(int, [input().strip() for _ in range(3)]))
drink = list(map(int, [input().strip() for _ in range(2)]))
print(min(burger) + min(drink) - 50)

## 20254 o
ur, tr, uo, to = map(int, input().split())
print(56*ur+24*tr+14*uo+6*to)

## 1145 o
from itertools import permutations, combinations; from math import gcd
cases = list(map(int, input().split())); least_lcm = []
def lcm_two(a, b):
    return a*b//gcd(a, b)
for i in combinations(cases, 3):
    a, b, c= i; least_lcm.append(lcm_two(lcm_two(a, b), c))
print(min(least_lcm))

## 2822 o
grade = list(map(int, [input().rstrip() for _ in range(8)]))
scores = {v:k for k, v in zip(grade, range(1, 8+1))}
grade = sorted(grade, reverse=True)
ranking_qs = sorted(scores.keys(), key=lambda x:scores[x], reverse=True)[:-3]
print(sum(grade[:-3]))
print(*sorted(ranking_qs))

## 2547 o
t = int(input())
for _ in range(t*2):
    n = input()
    if n == '': next
    else:
        n = int(n); candies = list(map(int, [input().strip() for i in range(n)]))
        if sum(candies) % n == 0: print('YES')
        else: print('NO')

## 4096 o
while True:
    n = input()
    if n == '0': pass; break
    else:
        if n[::-1] == n: print(0)
        else: 
            val = int(n) + 1
            while True:
                val = str(val).zfill(len(n))
                if str(val)[::-1] == str(val): break
                val = int(val); val += 1
            print(int(val)-int(n))

#----------------------------------
## 13416 o
for _ in range(int(input())):
    n = int(input()); max_val = 0
    for i in range(n):
        max_stk = max(map(int, input().split()))
        if  max_stk < 0: max_val += 0
        else: max_val += max_stk
    print(max_val)
    
## 6749 o
y, m = map(int, [input().rstrip() for _ in range(2)])
print(m + (m-y))

## 2592 o
num_cases = list(map(int, [input().rstrip() for _ in range(10)]))
print(sum(num_cases)//10) 
print(sorted(num_cases, key=lambda x: num_cases.count(x), reverse=True)[0])

## 15727 o
l = int(input())
if l / 5 - l //5 !=0: print(l//5+1)
else: print(l//5)

## 4696 o
while True:
    n = float(input())
    if n == 0.0: pass; break
    else: print('{:.2f}'.format(1 + n + n**2 + n**3 + n**4))
    
## 2355 o
a, b = map(int, input().split())
if a < 0 and b < 0:
    if a >= b: print((abs(b)+1)*b//2-abs(a)*(a+1)//2)
    else: print((abs(a)+1)*a//2-abs(b)*(b+1)//2)
elif a < 0 and b > 0: print((abs(a)+1)*a//2+b*(b+1)//2)
elif a > 0 and b < 0: print((abs(b)+1)*b//2+a*(a+1)//2)
elif a == 0 and b == 0: print(0)
else: 
    if a >= b: print(a*(a+1)//2 - (b-1)*(b) // 2)
    else: print(b*(b+1)//2 - (a-1)*(a) // 2)

## 4589 o
print('Gnomes:')
for _ in range(int(input())):
    length = list(map(int, input().split()))
    if length[0] < length[1] and length[1] < length[2]: print('Ordered')
    elif length[0] > length[1] and length[1] > length[2]: print('Ordered')
    else: print('Unordered')

#-----------------------------
## 15964 o
a, b = map(int, input().split())
def cal_ab(a, b):
    a <= 1000; b <= 1000
    return (a+b) * (a-b)
print(cal_ab(a, b))

#-------------------------------------
## 2997 o
nums = sorted(list(map(int, input().split())))
if nums[1] - nums[0] == nums[2] - nums[1]: print(nums[2] + (nums[1] - nums[0]))
elif nums[1] - nums[0] > nums[2] - nums[1]: print(nums[1] - (nums[2] - nums[1]))
else: print(nums[2] - (nums[1] - nums[0]))

## 3047 o
vals = sorted(list(map(int, input().split()))); order = input()
num_dict = {k: v for k, v in zip(['A', 'B', 'C'], vals)}
print(num_dict[order[0]], num_dict[order[1]], num_dict[order[2]])

## 2745 o
vals = {chr(k): v for k, v in zip(range(ord('A'), ord('Z')+1), range(10, 35 + 1))}
vals.update({str(k): v for k, v in enumerate(range(10))})
n, b = map(str, input().split()); s = 0; b = int(b)
for i, v in enumerate(n[::-1]):
    s += vals[v] * (b ** i)
    # if b > 10: s += vals[v] * (b ** i)
    # # elif b == 10: s += int(v) * (b ** i)
    # else: s += int(v) * (b ** i)
print(s)

## 24082 o
print(int(input())**3)
 
## 17356 o
a, b = map(int, input().split()); m = (b-a) / 400
print(1/(1+(10**(m))))

## 2530 o
a, b, c = map(int, input().split()); d = int(input())
hr = d // 3600; min = (d - hr*3600) // 60; sec = d - (hr*3600 + min*60) 
A, B, C = a + hr, b + min, c+sec
if C >= 60: 
    C-= 60; B += 1
    if B >= 60: B %= 60; A += 1; 
    A %= 24
else:
    if B >= 60: B %= 60; A += 1
    A %= 24
print(A, B, C)

## 4299 o
s, d = map(int, input().split())
a = (s+d)/2; b = (s-d)/2
if a >= 0 and b >= 0:
    if a - (s+d)//2 == 0 and b - (s-d)//2 == 0:
        if a > b: print((s+d)//2, (s-d)//2)
        else: print((s-d)//2, (s+d)//2)
    else: print(-1)
else: print(-1)

## 4470 o
for i in range(int(input())):
    print(f'{i+1}. {input()}')

## 9086 o
for _ in range(int(input())):
    test_case = input()
    print(f'{test_case[0]}{test_case[-1]}')

## 1598 o
a, b = map(int, input().split())
play = [[0 for i in range(max(a, b)//4+1)] for _ in range(4)]; coord = []
for i in range(4):
    for j in range(max(a, b)//4+1):
        play[i][j] = (i+1) + j*4
    if a in play[i]: coord.append((i, play[i].index(a)))
    if b in play[i]: coord.append((i, play[i].index(b)))
print(abs(coord[1][0]-coord[0][0])+abs(coord[1][1]-coord[0][1]))
