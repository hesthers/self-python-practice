## 1712 
a, b, c = list(map(int, input().split()))
if c > b: cost = a // (c - b) + 1; print(cost);
elif c <= b: print(-1)

## 2525
time = list(input().split(' '))
a = int(time[0])
b = int(time[1])
cooking= int(input())
if (a+((b+cooking)//60) < 24):
    if (b + cooking) < 60:
        print(f"{a} {b+cooking}")
    else:
        print(f"{a+((b+cooking) // 60)} {(b+cooking)%60}")

elif (a+((b+cooking)//60) >= 24):
        print(f"{a+((b+cooking) // 60) - 24} {(b+cooking)%60}")

## 17478 
num = int(input())
print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
txt = '''"재귀함수가 뭔가요?"
"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'''
for i in range(num+1):
    if i == num:
        print('__'*(2*i)+'"재귀함수가 뭔가요?"')
        print('__'*(2*i)+'"재귀함수는 자기 자신을 호출하는 함수라네"')
    else:
        for t in txt.splitlines():
            print('__'*(2*i)+t.lstrip()) 
for j in range(num, -1, -1):
    print('__'*(2*j)+'라고 답변하였지.')

## 2941 
letter = input()
sc = ["c=", 'c-', "dz=", 'd-', "lj", "nj", "s=", "z="]
in_letter = [l for l in sc if l in letter]
len_sum = 0
cnt_let = 0
for i in in_letter:
    cnt_let += letter.count(i) #dz=: 1, z=: 2(+1)
    len_sum += len(i)*letter.count(i)  #dz= *1 + z= * 3 - (z= * 1)
print(len(letter)-(len_sum-len('z=')*letter.count('dz='))+cnt_let-letter.count('dz='))

## 2908
nums = list(input().split())
a = nums[0]; b = nums[1]
n1= a[2] + a[1] + a[0]; n2 = b[2]+b[1]+b[0] 
n = []; n.append(n1); n.append(n2)
n = list(map(int, n))
print(max(n))

## 1181 
import sys
count_wds = int(input())
input_wds = [input().strip() for i in range(count_wds)]
if len(input_wds) == count_wds:
    input_wds = list(set(input_wds))
    input_wds = list(sorted(sorted(input_wds), key = lambda x: len(x)))
for inp in input_wds:
    print(inp, end='\n')

## 8958
## O -> O / O -> X
n = int(input()); answers = [input().strip() for i in range(n)]
for _ in answers:
    score = 0; tot = 0
    for i in _:
        if i == 'O': score += 1
        else: score = 0
        tot += score
    print(tot)

## 1157
words = input().lower()
split_wds = list(set(words))
wds_cnt = [words.count(w) for w in split_wds]
if (wds_cnt.count(max(wds_cnt)) > 1): print('?')
elif (wds_cnt.count(max(wds_cnt)) == 1): print(split_wds[wds_cnt.index(max(wds_cnt))].upper())

## 1267 
n = int(input())
pym = list(map(int, input().split(' ')))
y = list(map(lambda x:10 * (x//30+1) if x >= 30 else 10, pym))
m = list(map(lambda x:15 * (x//60+1) if x >= 30 else 15, pym))
if sum(y) > sum(m): print('M', sum(m))
elif sum(y) < sum(m): print('Y', sum(y))
else: print('Y M', sum(m))

## 10815 
cards_num = int(input()); cards = set(input().split(' '))
m = int(input()); m_num = input().split(' ')
num = []
for a in m_num:
    if a in cards: num.append('1')
    else: num.append('0')
print(' '.join(num))
