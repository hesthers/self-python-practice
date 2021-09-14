# Python code for baseball game

import random

num_list = []
index = []
ran_num = []
for i in range(3):
    index.append(i)
    num_list.append(random.randint(0, 9))

for n, m in zip(index, num_list):
    ran_num.append(m)
    cnt = ran_num.count(ran_num[n])
    if cnt >= 2:
        ran_num.remove(ran_num[n])
        ran_num.append(random.randint(0, 9))
        if ran_num[n] in ran_num:
            pass
        else:
            ran_num.append(random.randint(0, 9))

    else:
        ran_num = ran_num

    if len(ran_num) == 3:
        break

print(f'랜덤 숫자: {ran_num}')
