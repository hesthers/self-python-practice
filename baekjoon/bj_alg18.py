## 2703 o
alphabet = {chr(k):v for k, v in zip(range(ord('A'), ord('Z')+1), range(1, 26+1))}
for _ in range(int(input())):
    encoded = input()
    rule = input(); decoded = ''
    for e in encoded:
        if alphabet.get(e) == None: decoded += ' '
        else: decoded += rule[alphabet.get(e)-1]
    print(decoded)

## 2495 x -> o
from itertools import groupby
for _ in range(3):
    num_str = input()

    max_len = max([len(list(g)) for k, g in groupby(num_str)], default=0)
    print(max_len)
    
'''for _ in range(3):
    inp = input()
    seq_nums, val = [], set(); max_cnt = 0

    if inp[0] == inp[1]: seq_nums.append(inp[0])
    for i in range(1, 8-1):
        if inp[i] == inp[i+1] or inp[i-1] == inp[i]:
            seq_nums.append(inp[i]); val.add(inp[i])

    if len(val) == 0: print(1)
    else:
        for v in val:
            max_cnt = max(seq_nums.count(v), max_cnt)
            if max_cnt == seq_nums.count(v): 
                print(seq_nums.count(v))
                
for _ in range(3):
    inp = input()
    val, max_cnt = set(), 0

    for i in range(1, 8):
        if inp[i-1] == inp[i]:
            val.add(inp[i])

    if len(val) == 0: print(1)
    else:
        for v in val:
            max_cnt = max(inp.count(v), max_cnt)
            if max_cnt == inp.count(v): 
                print(inp.count(v)) '''               
## 10874 o
def pattern(question):
        p = divmod((question-1), 5)
        return p[1] + 1

correction = [pattern(n) for n in range(1, 10+1)]

for _ in range(int(input())):
        cnt = 0
        answer = list(map(int, input().split()))
        for a, c in zip(answer, correction):
                if a == c: cnt += 1
        if cnt == 10: print(_+1)
        
## 2775 o
for _ in range(int(input())):
        k, n = [int(input()) for _ in range(2)]
        people = [[0 for _ in range(14+1)] for _ in range(14+1)]
        people[0][1:n+1] = [p for p in range(1, n+1)]
        # print(people)
        for i in range(1, k+1):
                for j in range(1, n+1):
                        people[i][j] += sum(people[i-1][:j+1])
        print(people[k][n])
        
## 10409 o
n, t = map(int, input().split()); nums = list(map(int, input().split()))
time, cnt = 0, 0
while nums:
        time += nums.pop(0); cnt += 1 
        
        if time > t: 
                cnt -= 1; print(cnt); break

        else: 
                if n == cnt: print(cnt)

## 10093 o
a, b = map(int, input().split())
if a == b: print(a-b)
else: 
        print(abs(a-b)-1)
        if a > b: 
                print(*[i for i in range(b+1, a)])
        elif a < b:
                print(*[i for i in range(a+1, b)])
'''틀린 풀이
a, b = map(int, input().split())

if 1 <= a <= 1000 and 1 <= b <= 1000:
        if a == b: print(a-b)
        else: 
                print(abs(a-b)-1)
        if a > b: 
                print(*[i for i in range(b+1, a)])
        elif a < b:
                print(*[i for i in range(a+1, b)])

elif abs(a-b) <= 100000 and 1 <= a <= 10**15 and 1 <= b <= 10**15:
        if a == b: print(a-b)
        else: 
                print(abs(a-b)-1)
        if a > b: 
                print(*[i for i in range(b+1, a)])
        elif a < b:
                print(*[i for i in range(a+1, b)])
'''

## 15489 o
def pascal_triangle(r, w):
        pascal = [[0]*(_+1) for _ in range(30+1)]

        for i in range(30+1-1):
                pascal[i][0] = 1; pascal[i][-1] = 1

        for i in range(1, 30+1):
                for j in range(len(pascal[i])-2):
                        pascal[i][j+1] = pascal[i-1][j] + pascal[i-1][j+1]

        return pascal[r-1:r+w-1]

r, c, w = map(int, input().split()); hap, i = 0, 0
for s in pascal_triangle(r, w):
        hap += sum(s[c-1:c+i]); i+= 1
print(hap)

## 2444 o
n = int(input())
for i in range(n):
        print(' '*(n-(i+1))+ '*'*(2*(i+1)-1))
for j in range(n-1, 0, -1):
        print(' '*(n-j)+'*'*(2*j-1))
        
## 2441 o
n = int(input())
for j in range(n, 0, -1):
        print(' '*(n-j)+'*'*j)

## 10174 o
for _ in range(int(input())):
        answer = []
        case = input().lower()
        if ' ' in case:
                case1 = case.split()
                for c1 in case1:
                        if c1[::-1] == c1:
                                if case[::-1] == case:
                                        answer.append('Yes')
                                else: answer.append('No')
                        else:
                                if case[::-1] == case:
                                        answer.append('Yes')
                                else: answer.append('No')

        else:
                if case[::-1] == case:
                        answer.append('Yes')  
                else: answer.append('No')

        print('Yes' if 'Yes' in answer else 'No')

## 1654 o
k, n = map(int, input().split())
lans = sorted([int(input()) for _ in range(k)])
left, right = 1, max(lans); answer = []

while left <= right:
        lan_cnt = 0; mid_length = (left + right) // 2  
        for l in lans:
                lan_cnt += l // mid_length

        if lan_cnt >= n: left = mid_length + 1
        else: right = mid_length - 1
        # print(mid_length, left, right)
        if mid_length <= left: answer.append(right)

print(min(answer))

## 4880 o
while True:
        a1, a2, a3 = map(int, input().split())
        if a1 == a2 == a3 == 0: pass; break
        if a2 - a1 == a3 - a2: print('AP', a3+(a2-a1))
        else: print('GP', a3*(a2//a1))
        
## 10384 o
for _ in range(int(input())):
        alphabet = {chr(i): -1 for i in range(ord('a'), ord('z')+1)}
        sentence = input().lower().replace(' ', '')
        
        for s in sentence: 
                if s.isalpha() :alphabet[s] += 1
        
        max_cnt = max(list(alphabet.values()).count(0), list(alphabet.values()).count(1), list(alphabet.values()).count(2))   
        
        if  min(list(alphabet.values())) == -1 or -1 in alphabet.values(): 
                print(f'Case {_+1}: Not a pangram') 

        elif max_cnt == list(alphabet.values()).count(0) or min(alphabet.values()) == 0:
                print(f'Case {_+1}: Pangram!')
        
        elif max_cnt == list(alphabet.values()).count(1) or min(alphabet.values()) == 1:
                print(f'Case {_+1}: Double pangram!!')

        elif max_cnt == list(alphabet.values()).count(2) or min(alphabet.values()) == 2: 
                print(f'Case {_+1}: Triple pangram!!!')
                
## 1100 o
chess_horse = [[_ for _ in input()] for _ in range(8)]
chess = [[0 for j in range(8)] for i in range(8)]

cnt = 0
for i in range(8):
        for j in range(8):
                if i % 2 == 0:
                        if j % 2 == 0: chess[i][j] = 'W'
                        else: chess[i][j] = 'B'
                elif i % 2 != 0:
[O                        if j % 2 == 0: chess[i][j] = 'B'
                        else: chess[i][j] = 'W'
              
                if chess[i][j] == 'W' and chess_horse[i][j] == 'F':
                        cnt += 1
print(cnt)

#-----------------------
## 2979 o
a, b, c = map(int, input().split())
times = [list(map(int, input().split())) for _ in range(3)]
max_time = sorted(times, key = lambda x: (-x[1], -x[0]))[0][1]
gaps = [0 for _ in range(max_time-1)]

for depart, arrive in times:
        for i in range(depart-1, arrive-1):
                gaps[i] += 1
   
fares = 0
for g in gaps:
        if g == 1: fares += a * g
        elif g == 2: fares += b * g
        else: fares += c * g
print(fares)

## 1065 o
x = int(input()); cnt = 99
if x < 100: print(x)
else:
    for n in range(100, x+1):
        if n >= 100 and n < 1000:
            for i in range(1, 2):
                if int(str(n)[i]) - int(str(n)[i-1]) == int(str(n)[i+1]) - int(str(n)[i]):
                    cnt += 1
                                        
    print(cnt)

## 1463 o
n = int(input())
cal = [1 for i in range(n+1)]
cal[:4] = [0, 0, 1, 1]

for idx in range(4, n+1):
        if idx % 2 == 0 and idx % 3 == 0:
                cal[idx] = min(cal[idx//3], cal[idx//2]) + 1
        elif idx % 2 == 0 and idx % 3 != 0:
                cal[idx] = min(cal[idx-1], cal[idx//2]) + 1
        elif idx % 2 != 0 and idx % 3 == 0:
                cal[idx] = min(cal[idx-1], cal[idx//3]) + 1
        else:
                cal[idx] = cal[idx-1] +1

print(cal[n])

## 2399 o
x_coord = [0 for _ in range(int(input()))]
for i, x in zip(range(len(x_coord)), list(map(int, input().split()))):
        x_coord[i] = x

hap = 0
for i in range(len(x_coord)):
        for j in range(len(x_coord)):
                if i == j: pass
                elif i < j:  hap += abs(x_coord[i]-x_coord[j])
print(hap*2)

## 10953 o
for _ in range(int(input())):
        a, b = map(int, input().split(','))
        print(a+b)
        
## 11655 o
encoded = {chr(k): chr(v) for k, v in zip(range(ord('A'), ord('Z')-12), range(ord('A')+13, ord('Z')+1))}
encoded.update({chr(k): chr(v) for k, v in zip(range(ord('A')+13, ord('Z')+1), range(ord('A'), ord('Z')+1-13))})
encoded.update({chr(k): chr(v) for k, v in zip(range(ord('a'), ord('z')-12), range(ord('a')+13, ord('z')+1))})
encoded.update({chr(k): chr(v) for k, v in zip(range(ord('a')+13, ord('z')+1), range(ord('a'), ord('z')+1-13))})

for w in input():
        if w == ' ': print(w, end='')
        elif w.isalpha(): 
                print(encoded[w], end='')
        else: print(w, end='')
        
## 9625 o (피보나치 수열 연관)
k = int(input())
ab_cnt =[[0, 0] for _ in range(45+1)]
ab_cnt[0] = [1, 0]; ab_cnt[1] = [0, 1]
for s in range(2, len(ab_cnt)):
        ab_cnt[s][0] = ab_cnt[s-1][0] + ab_cnt[s-2][0]
        ab_cnt[s][1] = ab_cnt[s-1][1] + ab_cnt[s-2][1]
# print(ab_cnt)
print(*ab_cnt[k])  

## 5426 o
[Ifor _ in range(int(input())):
        letter = input(); n = int(len(letter) ** 0.5) #항상 제곱수 만큼의 길이를 가진 문자열
        
        # 암호화된 (90도 회전) 문자열 저장 (행 -> 열)
        mat = [[0 for _ in range(n)] for _ in range(n)]
        for i, j in zip(range(n), range(0, len(letter), n)):
                mat[i] = list(letter[j:j+n])

        # 암호화된 (90도 회전) 문자열 다시 해독해서 저장 (열 -> 행)
        encoded = [[0 for _ in range(n)] for _ in range(n)]
        for i, j in zip(zip(*mat), range(n-1, -1, -1)):
                encoded[j] = i
        print(''.join([''.join(e) for e in encoded]))

## 11048 o 
n, m = map(int, input().split())

maze = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
        for j, v in zip(range(m), list(map(int, input().split()))):
                maze[i][j] = v  

mvm = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
        for j in range(1, m+1):
                max_candy = max(mvm[i-1][j], mvm[i][j-1], mvm[i-1][j-1]) 
                mvm[i][j] = max_candy + maze[i-1][j-1]
                
print(mvm[n][m])

## 1927 o 
# python3, sys.stdin.readline() 사용해야 시간초과 안남 (input() => 시간 x)
import heapq, sys
heap_arr = []
for _ in range(int(sys.stdin.readline())):
        x = int(sys.stdin.readline())
        
        if x == 0:
                if len(heap_arr) == 0: print(0)
                else: print(heapq.heappop(heap_arr))

        else: heapq.heappush(heap_arr, x)
        
## 11279 o
import heapq, sys
heap_arr = []
for _ in range(int(sys.stdin.readline())):
        x = int(sys.stdin.readline())
        
        if x == 0:
                if len(heap_arr) == 0: print(0)
                else: print(-heapq.heappop(heap_arr))

        else: heapq.heappush(heap_arr, -x)
        
## 4435 o
gandalf = {k:v for k, v in zip(range(1, 6+1), [1, 2, 3, 3, 4, 10])}
sauron = {k:v for k, v in zip(range(1, 7+1), [1, 2, 2, 2, 3, 5, 10])}


for _ in range(int(input())):
        g, s = 0, 0
        gandalf_war = list(map(int, input().split()))
        sauron_war = list(map(int, input().split()))

        for gk in gandalf.keys():
                g += gandalf.get(gk) * gandalf_war[gk-1]
        
        for sk in sauron.keys():
                s += sauron.get(sk) * sauron_war[sk-1]

        if g > s:
                print(f'Battle {_+1}: Good triumphs over Evil')
        elif g < s:
                print(f'Battle {_+1}: Evil eradicates all trace of Good')
        else: print(f'Battle {_+1}: No victor on this battle field')
        
## 1526 o
max_geumminsu = 0
for i in range(1, int(input())+1):
        i = str(i)
        if i.count('4') + i.count('7') == len(i):
                max_geumminsu = max(int(i), max_geumminsu)
print(max_geumminsu)
