## 1934 
cnt = int(input()); a_b = [input().strip().split(' ') for i in range(cnt)]
def gcd(a, b):
    while b > 0: r = a % b; a, b = b, r 
    return a
for i in a_b: 
    a, b = int(i[0]), int(i[1])
    print(a*b//gcd(a, b))
    
## 2609 
num = input(); a, b = list(map(int, num.split(' ')))
def gcd(a, b):
    while b > 0: r = a % b; a, b = b, r 
    return a
print(gcd(a,b)); print(a*b//gcd(a,b))

## 3053
import math
r = int(input())
print(str(round(math.pi * (r**2), 7))[:-1] + '\n' + str(2 * (r**2)) + '.000000')

## 10872 
n = int(input()); fact = 1;
if n == 0: fact = 1
else:
    for i in range(1, n+1): fact*=i
print(fact)

## 2869 
a,b, c = list(map(int, input().split(' '))); x = (c-b) / (a-b)
if x - int(x) != 0 : print(int(x) +1)
else: print(int(x))

## 6603 
from itertools import combinations; lot = []
while True:
    lot += [list(map(int, input().split()))]
    if [0] in lot:
        for l in lot:
            if len(l) > 1:
                for i in list(combinations(l[1:], 6)):
                    print(' '.join(list(map(str,i))))
                print()
        break
    else: continue

## 5086 
nums = []
while True:
    nums += [list(map(int, input().split()))]
    if [0, 0] in nums: 
        for n in nums:
            if (n[0] == 0) & (n[1] == 0): break
            if n[1] % n[0] == 0: print('factor')
            elif n[0] % n[1] == 0: print('multiple')
            else: print('neither')
        break
    else: continue

## 1764 
n = list(map(int, input().split())); names = [input().strip() for _ in range(sum(n))]
a = set(names[:n[0]]); b = set(names[n[0]:]); print(len(a.intersection(b)))
for i in sorted(list(a.intersection(b))): print(i)

## 11050
import math; inp = list(map(int, input().split()))
print(int(math.factorial(inp[0]) / (math.factorial(inp[1])*math.factorial(inp[0] - inp[1]))))

## 11051
import math; inp = list(map(int, input().split()))
bi = math.factorial(inp[0]) // (math.factorial(inp[1])*math.factorial(inp[0] - inp[1]))
print(bi%10007)

## 1010 
import math; cnt = int(input()); case = [input().split() for i in range(cnt)]
for c in case:
    n, m = list(map(int, c)); print(math.factorial(m) // (math.factorial(n)*math.factorial(m-n)))

## 3036
import math;
n = int(input()); r = list(map(int, input().split()))
def gcd(a, b):
    while b > 0: r = a % b; a, b = b, r;
    return a
for i in range(1, len(r)):
    if r[0] % r[i] != 0: print(f'{r[0]//gcd(r[0], r[i])}/{r[i]//gcd(r[0], r[i])}');
    else: print(f"{r[0] // r[i]}/1")
