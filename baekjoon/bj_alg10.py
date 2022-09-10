## 14561 o
import string; from collections import deque; t = int(input())

def convert_iter(n, base):
    T = string.digits + '012345';  q, r = divmod(n, base)
    return convert_iter(q, base) + T[r] if q else T[r]

def palin(string):
    que = deque(); stk = deque()
    for s in string:
        que.append(s); stk.append(s)

    while que:
        if que.popleft() != stk.pop(): return 0
    return 1

for i in range(t):
    a, n = map(int, input().split())
    val = str(convert_iter(a, n))
   # print(val)
    print(palin(val))
    
#-----------------------------------
## 23795 o
tot_sum_money = 0
while True:
    bet_money = int(input())
    if bet_money == -1: break
    if bet_money != -1: tot_sum_money += bet_money
    if tot_sum_money > 2147483647: pass
    
print(tot_sum_money)

#-------------------------------
## 11727 o
def rectangle(num):
    rect_arr = [0] * (1000+1); rect_arr[0] = rect_arr[1] = 1
    for i in range(2, num+1): rect_arr[i] = (rect_arr[i - 1] + rect_arr[i - 2] * 2)  % 10007
    return rect_arr[num]
print(rectangle(int(input())))

#------------------------
## 4892 o 
cnt = 1
while True:
    n0 = int(input())
    
    if n0 == 0: break
    else:
        n1 = 3 * n0
        if n1 % 2 == 0: 
            n2 = n1 // 2; n3 = n2 * 3; n4 = n3 // 9
            n0 = 2 * n4
            print(f'{cnt}. even {n4}')
        else: 
            n2 = (n1 + 1) // 2; n3 = n2 * 3; n4 = n3 // 9
            n0 = 2 * n4 + 1
            print(f'{cnt}. odd {n4}')
        cnt += 1

#------------------------------
## 1259 o
from collections import deque
def palin(string):
    que = deque(); stk = deque()
    for s in string:
        que.append(s); stk.append(s)

    while que:
        if que.popleft() != stk.pop(): return 'no'
    return 'yes'

while True:
    n = input()
    if n == '0': break
    else: 
        print(palin(n)) 
        
#-------------------------
## 15486 o
n = int(input()); day_profit = [list(map(int, input().split())) for i in range(n)]
def out_company(data_list, N):
    days = [0] * (N+2); profits = [0] * (N+2); 
    for i, dl in zip(range(1, N+1), data_list): days[i] = dl[0]
    for i, dl in zip(range(1, N+1), data_list): profits[i] = dl[1]

    data_result = [0] * (N+2)
    for i in range(N, 0, -1):
        if i + days[i] > N + 1:
            data_result[i] = data_result[i+1]
        else:
            data_result[i] = max(data_result[i+1], profits[i] + data_result[i+days[i]])

    return max(data_result)

print(out_company(day_profit, n))

#----------------------------
## 2338 o
a, b = map(int, [input().rstrip() for i in range(2)])
for i in [a+b, a-b, a*b]: print(i)

#-------------------------------
## 5339 o
print('     /~\\')
print('    ( oo|')
print('    _\=/_')
print('   /  _  \\')
print(r'  //|/.\|\\')
print(' ||  \ /  ||')
print('============')
print('|' + ' '*10 +'|')
print('|' + ' '*10 +'|')
print('|' + ' '*10 +'|')

#-----------------------------
## 10101 o
a, b, c = map(int, [input().strip() for i in range(3)])
if a == b == c == 60: print('Equilateral')
elif a + b + c == 180 and a != b and b != c and a != c: print('Scalene')
elif a + b + c != 180: print('Error')
else: print('Isosceles')

#-----------------------------
## 5554 o
road_times = sum(list(map(int, [input().strip() for i in range(4)])))
print(road_times//60); print(road_times%60)

#------------------------------
## 1251 o
word = input()
split_words = [[word[:i][::-1], word[i:j][::-1], word[j:][::-1]] for i in range(1, len(word)) for j in range(len(word)-1, i, -1)]
flipped_words = sorted([''.join(sw) for sw in split_words])
print(flipped_words[0])

#--------------------------------
## 5532 o
l, a, b, c, d = map(int, [input().strip() for i in range(5)])
if a % c == 0:
    if b % d == 0: max_done_hw = max(a//c, b//d)  
    else: max_done_hw = max(a//c, b//d+1) 
else:
    if b % d == 0: max_done_hw = max(a//c+1, b//d)  
    else: max_done_hw = max(a//c+1, b//d+1)
print(l-max_done_hw)

#-----------------------------
## 1855 o
k, encoded_str = map(str, [input().strip() for i in range(2)]); k = int(k)
row = len(encoded_str) // k; #print(row)
# 1. 행의 수 k개 별로 암호화된 문자열 나누어 배치하기
decoded_str = [encoded_str[es:es+k] for es in range(0,len(encoded_str), k)]
    #[['0'*(k+1)] for _ in range(row+1)]

# print(decoded_str)
# 2. 짝수번째 행(인덱스 넘버는 홀수)의 경우 뒤집기
for ds in range(len(decoded_str)):
    if ds % 2 != 0: decoded_str[ds] = decoded_str[ds][::-1]
    else: pass

decoded_str = ''.join(decoded_str)
# print(decoded_str)

# 3. 행과 열의 위치 변경하기 (첫번째 열 => 첫번째 행)
for i in range(len(encoded_str)):
    # print(decoded_str[i::row])
    if len(decoded_str[i::k]) == row: print(decoded_str[i::k], end = '')

#----------------------------
## 2744 o
eng_str= input()
for es in eng_str:
    if es.islower(): print(es.upper(), end = '')
    else: print(es.lower(), end = '')

## 1357 o
x, y = map(int, input().split())
def Rev(n):
    return int(str(n)[::-1])
print(Rev(Rev(x)+Rev(y)))

#--------------------------
## 1312 o
a, b, n = map(int, input().split());
for i in range(n):
    a = a % b * 10
print(a//b)

#----------------------
## 1284 o
while True:
    n = input(); width = 2+ (len(n)-1) * 1
    if n != '0':
        for i in n:
            if int(i) == 1: width += 2
            elif int(i) == 0: width += 4
            else: width += 3
        print(width)
    else: break

#--------------------------
## 4150 o
def fibo(num):
    if num == 0: return num
    first, second = 1, 1
    for _ in range(3, num+ 1):
        first, second = second, first + second
    return second
print(fibo(int(input())))
