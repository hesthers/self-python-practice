## 9095
test_cases = list(map(int, [input().strip() for i in range(int(input()))]))
def sum_123(num):
    arr = [0 for i in range(num+1)]
    for i in range(1, num+1): arr[i] = 2 ** (i-1); #return arr[num]
    for idx in range(4, len(arr)):
        arr[idx] = arr[idx-1] + arr[idx-2] + arr[idx-3]
    return arr[num]
for tc in test_cases: print(sum_123(tc))

#-----------------------------
## 10870 
def fibo(number):
    if number <= 1: return number
    return fibo(number-1)+fibo(number-2)
print(fibo(int(input())))

## 2748 
def fibo(number):
    fibo_cases = [0] * (number+1)
    for i in range(2): fibo_cases[i] = i
    for idx in range(2, number+1):
        fibo_cases[idx] = fibo_cases[idx-1]+fibo_cases[idx-2]
    return fibo_cases[number]
print(fibo(int(input())))

#------------------------------
## 2750 
cases = list(map(int, [input().strip() for i in range(int(input()))]))
for c in range(len(cases)):
    for idx in range(len(cases)-c-1):
        if cases[idx] > cases[idx+1]: cases[idx+1], cases[idx] = cases[idx], cases[idx+1]
for c_d in cases: print(c_d)       

## 2751 
cases = list(map(int, [input().strip() for i in range(int(input()))]))
for i in sorted(cases): print(i) # 맞은 풀이
'''
def sort_data(data_list):
        if len(data_list) <= 1: return data_list 
        
        pivot = data_list[0]; left=[]; right = [];
        for dl in data_list[1:]:
            if dl <= pivot: left.append(dl)
            else: right.append(dl)
                
        return sort_data(left)+[pivot]+sort_data(right)

for i in sort_data(cases): print(i)'''

#----------------------------
## 1920 x -> o
n_cases = [0 for i in range(int(input()))]
for nc, val in zip(range(len(n_cases)), list(map(int, input().split()))): n_cases[nc] = val
m_cases = [0 for i in range(int(input()))]
for mc, val in zip(range(len(m_cases)), list(map(int, input().split()))): m_cases[mc] = val  
n_cases = set(n_cases)
for mc in m_cases:
    if mc in n_cases: print(1)
    else: print(0)

'''def bin_search(data_list, num):
    
    def sort_data(data_list):
        if len(data_list) <= 1: return data_list 
        
        pivot = data_list[0]; left=[]; right = [];
        for dl in data_list[1:]:
            if dl <= pivot: left.append(dl)
            else: right.append(dl)
                
        return sort_data(left)+[pivot]+sort_data(right)

    data_list = sort_data(data_list)
    
    if len(data_list) == 1 and num == data_list[0]: return 1
    #if len(data_list) == 0  or (len(data_list) == 1 and num != data_list[0]): return 0
        
    med = len(data_list) // 2; med_val = data_list[med]
    if num != med_val:
        if num < med_val: return bin_search(data_list[:med], num)
        else: return bin_search(data_list[med+1:], num)
    else: return 1#bin_search([med_val], num)
    
for mc in m_cases: print(bin_search(n_cases, mc))

inp = [input().strip() for i in range(4)]
n_cases = list(map(int, inp[1].split()))
m_cases = list(map(int, inp[3].split()))

import sys; 

def sort_data(data_list):
    if len(data_list) <= 1: return data_list 
    
    pivot = data_list[0]; left=[]; right = [];
    for dl in data_list[1:]:
        if dl <= pivot: left.append(dl)
        else: right.append(dl)
            
    return sort_data(left)+[pivot]+sort_data(right)

inp = [input().strip() for i in range(4)]
n_cases = list(map(int, inp[1].split())); n_cases = sort_data(n_cases)
m_cases = list(map(int, inp[3].split()))

def bin_search(beg, end, num):  
    if beg > end: return 0
        
    med = (beg+end) // 2
    if num != n_cases[med]:
        if num < n_cases[med]: return bin_search(beg, med-1, num)
        else: return bin_search(beg, med+1, num)
    else: return 1

for mc in m_cases: print(bin_search(0, len(n_cases)-1 , mc))'''

#-------------------------
## 11047
from collections import deque
n, k = map(int, input().split())
coins = [int(input()) for i in range(n)]
coins = sorted(coins, reverse=True)
cnt = 0; cnt_coins = deque()
for c in coins:
    cnt = k // c; k -= cnt * c; cnt_coins.append(cnt)
print(sum(cnt_coins))  

## 24416
n = int(input())
def fib(n):
    cnt = 0
    if n <= 2: cnt+=1; return 1
    cnt += 1;
    return fib(n-1) + fib(n-2)
    return cnt

def fibo(n):
    arr = [0 for i in range(n)]
    arr[0] = arr[1] = 1; counting = 0
    for i in range(2, n):
        arr[i] = arr[i-1] + arr[i-2]
        counting+=1
    #return arr[n-1]
    return counting

print(fib(n), fibo(n))

#---------------------------
## 2920 
notes = list(map(int, input().split()))
for idx in range(len(notes)-1):
    if (notes[idx+1] - notes[idx] == 1) and (sorted(notes) == notes): result = 'ascending'
    elif (notes[idx+1] - notes[idx] == -1) and (sorted(notes, reverse=True) == notes): result = 'descending'
    else: result = 'mixed'
print(result)

#-------------------------
## 1874 
cases = [int(input()) for i in range(int(input()))]
from collections import deque
stk = deque(); answer = deque(); val = 1
for c in cases:
    while val <= c:
        if val <= c: stk.append(val); answer.append('+'); val += 1
    if c == stk[-1]: stk.pop(); answer.append('-');
    else: answer.append('NO'); print('NO'); break

if 'NO' in answer: pass
else:
    for a in answer: print(a)

## 5397 ** 
from collections import deque;
cases = [input().strip() for i in range(int(input()))]
print_pw = deque()
for c in cases:
    left = deque(); right = deque()
    for i in c:
        if '>' == i: 
            if right: left.append(right.pop())
        elif '<' == i: 
            if left: right.append(left.pop())
        elif '-' == i: 
            if left: left.pop()
        else: left.append(i)
    left.extend(reversed(list(right))); #print("".join(left))
    print_pw.append(''.join(left))
for pw in print_pw: print(pw)
#---------------------------
## 10930 
import hashlib

test_password = input()
print(hashlib.sha256(test_password.encode()).hexdigest())
'''
after_password = test_password.encode('utf-8')
password_hash = hashlib.new('sha256')
password_hash.update(after_password)
print(password_hash.hexdigest())    '''

#----------------
## 2953 
scores = [sum(list(map(int, input().split()))) for i in range(5)]
print(scores.index(max(scores))+1, max(scores))
