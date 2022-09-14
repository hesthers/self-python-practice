## 10807 o
n, nums, v = map(str, [input().strip() for i in range(3)])
cases = [0 for _ in range(int(n))]
for c, val in zip(enumerate(cases), list(map(int, nums.split()))): cases[c[0]] = val
print(cases.count(int(v)))

#------------------------------
## 2845 o
l, person = map(int, input().split()); ppl = list(map(int, input().split()))
diff = [p - l*person for p in ppl]
print(*diff)

#------------------------------
## 1193 o
x = int(input()); n = 0; 
while True:
# arr[1] = '1/1'
# for i in range(2, num+1):
    rule_num = 1 + (n * (n-1) //2); 
    if rule_num > x: break
    n += 1

n = n - 1; rule_num = rule_num - n
# if rule_num <= x < 1 + (n * (n+1) //2):
if n % 2 == 0: 
    diff = x - rule_num
    num = 1+diff; den = n-diff
    # den = n; num = 1  
    # for _ in range(i, i+n):
    #     arr[_] = f'{num}/{den}'; den -= 1; num += 1; 
    
    
else: 
    diff = x - rule_num
    num = n-diff; den = 1+diff
        # den = 1; num = n  
        # for _ in range(i, i+n):
        #     arr[_] = f'{num}/{den}'; den += 1; num -= 1; 
        # n += 1
            
# print(diff, num, den)
print(f'{num}/{den}')

#---------------------------
## 11365 o
while True:
    code = input()
    if code == 'END': pass; break
    else: print(code[::-1])
    
#_---------------------------------
## 5635 o
students = [input().split() for _ in range(int(input()))]
students = sorted(students, key= lambda x: (-int(x[-1]), -int(x[-2]), -int(x[1])))
young = students[0][0]; old = students[-1][0]
print(young + '\n' + old)

#---------------------------------
## 25304 o
x, n = map(int, [input().strip() for i in range(2)]); cost = 0
for i in range(n):
    a, b = map(int, input().split())
    cost += a * b
if x == cost: print('Yes')
else: print('No')

#---------------------------
## 5596 o
s = sum(list(map(int, input().split())))
t = sum(list(map(int, input().split())))
if s >= t: print(s)
else: print(t)

#---------------------
## 1233 o
from collections import Counter
s1, s2, s3 = map(int, input().split())
sum_cases_cube = [i+j+k for i in range(1, s1+1) for j in range(1, s2+1) for k in range(1, s3+1)]
print(sorted(Counter(sum_cases_cube).keys(), key= lambda x: Counter(sum_cases_cube)[x], reverse=True)[0])

## 1673 o
while True:
    try:
        n, k = map(int, input().split())
        cnt_ch = 0; coupon = n; stamp = 0
        while coupon > 0:
            cnt_ch += coupon; stamp += coupon
            coupon = stamp // k; stamp %= k

        print(cnt_ch)
    except: break

'''while True:
    try:
        n, k = map(int, input().split())
        coupon = n; stamp = 0; cnt_ch = 0
        while coupon > 0:
            coupon -= 1; stamp += 1; cnt_ch += 1
            if stamp == k: coupon += 1; stamp = 0
        print(cnt_ch)
    except: break'''

#------------------------------
## 10992 o
n = int(input())
for i in range(n):
    if i == 0: print(' '*(n-i-1) + '*')
    elif 1 <= i < n-1: print(' '*(n-i-1) + '*' +' '*(2*i-1) +'*')
    else: print('*'*(2*n-1))

#--------------------------
## 1735 o
a1, b1 = map(int, input().split()); a2, b2 = map(int, input().split())
numerator = a1*b2 + a2*b1; denominator = b2 * b1

def gcd(a, b):
    if a%b == 0: return b
    return gcd(b, a%b)

def non_divide(a, b):
    if gcd(a, b) == 1: return a, b
    else: return a//gcd(a, b), b//gcd(a, b)

n, d = non_divide(numerator, denominator)
print(n, d)

#---------------------------------
## 10699 o
from datetime import datetime
today_date = datetime.now().date().strftime('%Y-%m-%d')
print(today_date)

## 11718 o
while True:
    try: print(input())
    except: break
    
#---------------------------
## 1371 o
cnt_letter = {chr(k):0 for k in range(ord('a'), ord('z')+1)}
while True:
    try:
        sentence = input()
        for s in sentence:
            for k in cnt_letter.keys():
                if s == k: cnt_letter[k] += 1

    except: break
for i in list(filter(lambda x: cnt_letter[x] == max(cnt_letter.values()), cnt_letter.keys())): print(i, end='')

#--------------------------------
## 1871 o
# car_license = [input().split('-') for i in range(int(input()))]

def chg_alpha_to_num(letter):
    val = 0
    alpha_num = {chr(k): v for k, v in zip(range(ord('A'), ord('Z')+1), range(26))}
    for idx, v in enumerate(letter[::-1]): val += alpha_num[v] * (26 ** idx)
    return val

n = int(input())
for _ in range(n):
    car_license_alpha, car_license_num = input().split('-')
    car_license_num = int(car_license_num); car_num = chg_alpha_to_num(car_license_alpha)
    print('nice' if abs(car_num - car_license_num) <= 100 else 'not nice')

    #if abs(car_num - car_license_num) <= 100: print('nice')
    #else: print('not_nice')

# print(alpha_num)
#---------------------------
## 9093 o
for i in range(int(input())):
    sentence = input()
    reversed_sentences = [s[::-1] for s in sentence.split()]
    print(*reversed_sentences)
    
## 8370 o
n1, k1, n2, k2 = map(int, input().split())
print(n1*k1+n2*k2)

## 5893 o
n = input(); bi_num = 0
for i, j in enumerate(n[::-1]):
    bi_num += int(j) * pow(2, i)
print(format(bi_num*17, 'b'))

#-------------------------
## 6810 o
n1, n2, n3 = map(str,[input().rstrip() for _ in range(3)])
isbn = '9780921418' + n1 + n2 + n3; isbn_sum = 0
for i in range(len(isbn)):
    if i % 2 == 0: isbn_sum += int(isbn[i]) * 1
    else: isbn_sum += int(isbn[i]) * 3
print(f'The 1-3-sum is {isbn_sum}')

#-----------------------------
## 1551 o
n, k = map(int, input().split()); a = [0] * n
for i, j in zip(range(len(a)), list(map(int, input().split(',')))): a[i] =j

b = a[:]
for _ in range(k):
    c = [b[idx+1] - b[idx] for idx in range(len(b)-1)]
    b = c[:]

if k >= 1: print(*c, sep=',')
else: print(*a, sep=',')

#------------------------
## 1225 o
a, b = input().split(); multiple_result = 0
for i in a:
    for j in b:
        multiple_result += int(i) * int(j)
print(multiple_result)

#-------------------------------
## 1964 o
n = int(input())
def cnt_dot(num):
    dots = [0] * (num+1); dots[1] = 5
    for i in range(2, num+1): dots[i] = dots[i-1] + (3*i + 1)
    return dots[num] % 45678
print(cnt_dot(n))

#---------------------------
## 2153 o
word = input(); alpha_sum = 0
alpha_num = {chr(i): v for i, v in zip(range(ord('a'), ord('z')+1), range(1, 26 + 1))}
for i, v in zip(range(ord('A'), ord('Z')+1), range(26 + 1, 26*2 +1)):
    alpha_num[chr(i)] = v

for w in word:
    for k, v in alpha_num.items():
        if w == k: alpha_sum += v

def isPrime(n):
    cases = [k for k in range(2, n+1)]; j = 0 
    for cnt in range(2, int(n**(1/2))+1): 
        for i in range(j, len(cases), cnt):
            if (cnt != cases[i]): cases[i] = 0; cnt += 1
        j += 1
    prime = [1]+[c for c in cases if c != 0] 
    return 'It is a prime word.' if n in prime else 'It is not a prime word.'

print(isPrime(alpha_sum))

#----------------------------
## 1009 o
cnt = 0; t = int(input())
while cnt < t:
    i = 1; num_1 = []; 
    a, b = map(int, input().split())
    
    while True:
        if pow(a, i) % 10 in num_1: break
        else: 
            num_1.append((a ** i) % 10)
            i += 1
            
    if b%len(num_1) == 0 and 0 not in num_1: print(num_1[-1])
    elif len(num_1) == 1 and 0 in num_1: print(10)
    else: print(num_1[b%len(num_1)-1])
    cnt += 1
#--------------------------------
## 1076 o
color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
col_val = {c: [v, 10**v] for c, v in zip(color, range(10))}
r1, r2, r3 = map(str, [input().strip() for i in range(3)])
resist_val = ''
resist_val += str(col_val[r1][0]) + str(col_val[r2][0])
result = int(resist_val) * col_val[r3][1]
print(result)
#or
'''color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
col_val = {c: [v, 10**v] for c, v in zip(color, range(10))}
r1, r2, r3 = map(str, [input().strip() for i in range(3)]); resist_val = ''
resist_val += str(col_val[r1][0]) + str(col_val[r2][0])
print(int(resist_val) * col_val[r3][1])'''

#--------------------------------------------
## 1380 o
c = 1
while True:
    n = int(input()); girls = [input().strip() for _ in range(n)]
    earrings = {str(i+1):[] for i in range(n)}
    for i in range(2*n-1):
        seq, yn = input().split(); earrings[seq].append(yn)
    if n == 0: pass; break
    earrings = list(map(int, sorted(earrings.keys(), key=lambda x: len(earrings[x]))))
    print(c, girls[earrings[0]-1])
    c += 1

#-------------------------------
## 4999 o
j, d = [input().rstrip() for _ in range(2)]
if len(j) >= len(d): print('go')
else: print('no')

#-------------------------------
## 3944 o
import sys
def mod_num(b, d):
    chg_num = 0
    for v in d:
        chg_num += int(v) 
    return chg_num % (int(b)-1)

for _ in range(int(sys.stdin.readline())):
    b, d = sys.stdin.readline().split()
    print(mod_num(b, d))
    
## 1247 o
for i in range(3):
    s = 0
    nums = list(map(int, [input().strip() for _ in range(int(input()))]))
    for n in nums:
        s += n
    if s == 0: print('0')
    elif s > 0: print('+')
    else: print('-')
    
#------------------------
## 5063 o
for i in range(int(input())):
    r, e, c = map(int, input().split())
    if r + c > e: print('do not advertise')
    elif r + c == e: print('does not matter')
    else: print('advertise') 
    
#---------------------
## 9610 o
q1, q2, q3, q4, axis = 0, 0, 0, 0, 0
for i in range(int(input())):
    x, y = map(int, input().split())
    if x > 0 and y > 0: q1 += 1
    elif x > 0 and y < 0: q4 += 1      
    elif x < 0 and y > 0: q2 += 1
    elif x < 0 and y < 0: q3 += 1
    else: axis += 1

for i, v in enumerate([q1, q2, q3, q4, axis]):
    if i < 4: print(f'Q{i+1}: {v}')
    else: print(f'AXIS: {v}')

# q1, q2, q3, q4, axis = [], [], [], [], []
# for i in range(int(input())):
#     x, y = map(int, input().split())
#     if x > 0:
#         if y > 0: q1.append((x, y))
#         elif y < 0: q4.append((x, y))
#         # else: axis.append((x, y))
#     elif x < 0:
#         if y > 0: q2.append((x, y))
#         elif y < 0: q3.append((x, y))
#         # else: axis.append((x, y))
#     elif x == 0 or y == 0: axis.append((x, y))

# for i, v in zip(range(5), [q1, q2, q3, q4, axis]):
#     if i != 4: print(f'Q{i+1}: {len(v)}')
#     else: print(f'AXIS: {len(v)}')

# q1, q2, q3, q4, axis = [], [], [], [], []
# for i in range(int(input())):
#     x, y = map(int, input().split())
#     if x > 0:
#         if y > 0: q1.append((x, y))
#         elif y < 0: q4.append((x, y))
            
#     elif x < 0:
#         if y > 0: q2.append((x, y))
#         elif y < 0: q3.append((x, y))

#     else: axis.append((x, y))

# for i, v in enumerate([q1, q2, q3, q4, axis]):
#     if i < 4: print(f'Q{i+1}: {len(v)}')
#     else: print(f'AXIS: {len(v)}')

#----------------------
## 2420 o
n, m = map(int, input().split()); print(abs(n-m))

#----------------------
## 11382 o
a, b, c = map(int, input().split()); print(a+b+c)
