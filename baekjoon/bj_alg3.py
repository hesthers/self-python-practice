## 2755 
        tot_g = [i+i1 for i in ['A', 'B', 'C', 'D'] for i1 in ['+', '0', '-']]; tot_g.append('F')
g_dict = {k: float(i) for k, i in zip([i+'0' for i in ['A', 'B', 'C', 'D']], range(4, 0, -1))}
gr_dict = {}
for g in tot_g:
    if '0' in g: pass
    elif '+' in g:
        for k, v in g_dict.items():
            if k[0] == g[0]: gr_dict[g] = v + 0.3
    elif '-' in g:
        for k, v in g_dict.items():
            if k[0] == g[0]: gr_dict[g] = v - 0.3
    else: gr_dict[g] = 0.0
gr_dict.update(g_dict)

n = int(input()); courses = [input().strip().split() for c in range(n)]
avg_gr = tot_gr = 0;
for i in courses:
    c, g, t = i
    if t in gr_dict.keys(): avg_gr += gr_dict[t] * int(g); tot_gr += int(g)
print("{:.2f}".format(round(avg_gr / tot_gr+10**-5, 2)))

## 10102 
num = int(input()); voting = input(); 1 <= num <= 15
if len(voting) == num:
    if voting.count('A') > voting.count('B'): print('A');
    elif voting.count('A') < voting.count('B'): print('B');
    else: print('Tie')

## 3034 
n, w, h = input().split(); match = [int(input()) for i in range(int(n))]
for m in match:
    if (m <= int(w)) | (m <= int(h)) | (m <= ((int(w)**2)+(int(h)**2))**(1/2)): print('DA') 
    else: print('NE')

## 18108 
print(int(input())-(2541-1998))

## 10773 
num = int(input()); n_l = list(map(int, [input().strip() for i in range(num)]))
l = []
for i, n in enumerate(n_l):
    if n != 0: l.append(n); 
    else: l.pop(-1); 
print(sum(l))

## 10828 
num = int(input()); n_l = [input().strip() for i in range(num)]
s = []
for i in n_l:
    if 'push' in i: s.append(int(i.split()[1])); 
    elif 'pop' in i: 
        if len(s) == 0: print(-1);  
        else: print(s[-1]); s.pop(-1);  
    elif 'size' in i: print(len(s));  
    elif 'empty' in i: 
        if len(s) == 0: print(1);  
        else: print(0); 
    else: 
        if len(s) != 0: print(s[-1]); 
        else: print(-1);  

# 4153 
inputs = []
while True:
    inp = list(map(int, input().strip().split()))
    if sum(inp) == 0: break;
    else: inputs.append(inp)
for i in inputs:
    a, b, c = sorted(i, reverse = False)
    if c**2 == (a**2) + (b**2): print('right')
    elif (a == 0) & (b == 0) & (c == 0): pass
    else: print("wrong")

## 1085 
x, y, w, h = map(int, input().split())
length = [((x-w)**2+(y-h)**2)**(1/2), (x-0), (y-0), (w-x), (h-y), (w**2+h**2)**(1/2),
          (x**2 + y**2)**(1/2)]
print(min(length))

#---------------------------------
## 10430 
a, b, c = map(int, input().split())
print(str((a+b)%c) + '\n' + str((a%c+b%c)%c) + '\n' + str((a*b)%c) + '\n' + str(((a%c)*(b%c))%c))

#---------------------------------
## 1330 
a, b = map(int, input().split())
if a > b: print('>');
elif a == b: print('==');
else: print('<');

#--------------------------------
## 2753 
leap_yr = int(input())
if ((leap_yr % 4) == 0) & ((leap_yr % 100) != 0) | ((leap_yr % 400) == 0): print(1)
else: print(0)

#------------------------------
## 10172
dog = r'''|\_/|
|q p|   /}
( 0 )"""\
|"^"`    |
||_/=\\__|
'''
print(dog)

#-------------------------------
## 10869
a, b = map(int, input().split())
print(str(a+b) + '\n' + str(a-b) + '\n' + str(a*b) + '\n' + str(a//b) + '\n' + str(a%b))

#------------------
## 9498
score = int(input())
if 90 <= score <= 100: print('A')
elif 80 <= score < 90: print('B')
elif 70 <= score < 80: print('C')
elif 60 <= score < 70: print('D')
else: print('F')

#------------------
## 2884
hr, min = map(int, input().split())
if min < 45:
    if hr == 0: print(f'{24 - 1} {min + 60 - 45}')
    elif 0 < hr < 24: print(f'{hr - 1} {min + 60 - 45}')
else: print(f'{hr} {min - 45}')
