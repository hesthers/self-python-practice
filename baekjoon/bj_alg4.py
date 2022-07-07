## 2739 
n = int(input()); 1<=n<=9;
for i in range(1, 10): print(f'{n} * {i} = {n*i}')  

#-------------------------
## 10950
cases = [list(map(int, input().strip().split())) for i in range(int(input()))]             
for c in cases: a, b = c; print(a+b)

#------------------------
## 8393 
sum_num = 0
for i in range(1, int(input())+1): sum_num += i; 
print(sum_num)

#---------------------------
## 15552
cases = [list(map(int, input().strip().split())) for i in range(int(input()))]
for c in cases: a, b = c; print(a+b)

## 11021
cases = [list(map(int, input().strip().split())) for i in range(int(input()))]
for i, c in enumerate(cases): a, b = c; print(f'Case #{i+1}: {a+b}')

## 11022
cases = [list(map(int, input().strip().split())) for i in range(int(input()))]
for i, c in enumerate(cases): a, b = c; print(f'Case #{i+1}: {a} + {b} = {a+b}')

## 10952
nums = []
while True:
    nums += [list(map(int, input().split()))]
    if [0, 0] in nums: break
    else: continue;
for c in nums:
    a, b = c; 
    if (a !=0) & (b != 0): print(a+b)

## 10951
nums = []
while True:
    try: 
        a, b = map(int, input().split()); 
        if [] in nums: break;
        else: print(a+b);
    except ValueError: break;
    except EOFError: break;

#-----------------------
## 10818
length = int(input()); arrays = [0] * length
for i, j in zip(range(length), list(map(int, input().split()))): arrays[i] = j;
print(min(arrays), max(arrays))

#-------------------
## 2741 
for i in range(1, int(input())+1): print(i)

## 2742 
for i in range(int(input()), 0, -1): print(i)

#-------------------------
## 2562 
cases = [int(input()) for i in range(9)]; print(str(max(cases)) +'\n' + str(cases.index(max(cases))+1))

#--------------------------
## 2438 
for i in range(int(input())): print('*'*(i+1))

## 2439 
h = int(input())
for i in range(h): print(" "*(h-i-1)+'*'*(i+1))

#------------------------
## 10871
n, x = map(int, input().split()); arr = [0] * n
for i, j in zip(range(n), list(map(int, input().split()))): arr[i] = j;
for a in arr: 
    if a < x: print(a, end=' ')

#-------------------------
## 2577 
a, b, c = map(int, [input() for i in range(3)])
for s in range(10): print(str(a * b * c).count(str(s)))

## 3052 
cases = [int(input()) for i in range(10)]
mod = [c%42 for c in cases]; print(len(set(mod)))

#------------------------
## 1546 
cnt = int(input()); arr_sc = [0] * cnt
for i, j in zip(range(cnt), list(map(int, input().split()))): arr_sc[i] = j;
print((sum(arr_sc)/max(arr_sc)*100)/cnt)

#--------------------------
## 4344 
case_n = int(input()); case = [list(map(int,input().split())) for i in range(case_n)]
for c in case: 
    abv_avg = []
    n = c[0]; scores = c[1:];
    for s in scores:
        if s > sum(scores) / len(scores): abv_avg.append(s); 
    print('{:.3f}%'.format(round(len(abv_avg) / len(scores) * 100, 3)))

#---------------------------
## 10809
word = input(); lower_alpha = [chr(i) for i in range(97,123)]
for i in lower_alpha: print(word.find(i), end=' ')

#----------------------------
## 5622 
upper_cases = [chr(i) for i in range(65, 91)]; inp = input()
dials = {idx+1: upper_cases[3*(idx-1):3*idx] if idx<=7 else [] for idx in range(1, 9)}
dials[7] = upper_cases[15:15+4]; dials[8] = upper_cases[15+4: 15+4+3]; dials[9] = upper_cases[15+4+3:]
times = [k for k, v in dials.items() for j in inp if j in v]
time_sum = 0;
for i in times: time_sum += 2+(i-1)*1
print(time_sum)

#---------------------------
## 11720
n = int(input()); arr = [0] * n
for i, j in zip(range(n), input()): arr[i] = j;
arr = list(map(int, arr)); print(sum(arr))

#----------------------------
## 2675 
n = int(input()); cases = [input().split() for i in range(n)]
for c in cases: 
    a, b = c; 
    for j in b: print(j*int(a), end = '')
    print()
    
#-------------------------
## 1152 
sent = input().split(); print(len(sent))

## 11654
print(ord(input()))
#----------------------
## 10757
a, b = map(int, input().split()); print(a+b)

#-----------------------
## 10814
for s in sorted([input().split() for i in range(int(input()))], key = lambda x: int(x[0])): age, nm = s; print(age, nm)

#-----------------------------
## 11650
for s in sorted([list(map(int, input().split())) for i in range(int(input()))], key = lambda x: (x[0], x[1])): x, y = s; print(x, y)

#-----------------------------
## 3009 
rect_cases = [list(map(int, input().split())) for i in range(3)]; 
x_coor = []; y_coor = []; result= [];
for rc in rect_cases: x, y = rc; x_coor.append(x); y_coor.append(y);
for x, y in zip(x_coor, y_coor): 
    if x_coor.count(x) == 1 : x_ = x
    if y_coor.count(y) == 1 : y_ = y
print(x_, y_)  
