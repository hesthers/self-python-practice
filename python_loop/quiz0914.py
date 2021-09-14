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

cnt = 0
l_num = []
while True:
    cnt += 1

    game_num = input('숫자 3개를 입력하세요(띄어쓰기로 구분) : ')

    try:
        if ' ' in game_num:
            game_num = game_num.split(' ')
            for i in game_num:
                l_num.append(int(i))
        else:
            game_num = input('띄어쓰기와 함께 숫자를 다시 입력하세요 : ')
    except:
        game_num = input('숫자를 다시 입력하세요 : ')

    s_list = []
    b_list = []
    for n1, n2 in zip(ran_num, l_num):
        if (int(n1) != int(n2)) & (int(n1) not in l_num):
            print('OUT')
        else:
            strike = (int(n1) == int(n2)) & (int(n1) in l_num)
            ball = (int(n1) != int(n2)) & (int(n1) in l_num)
            s_list.append(ran_num[strike])
            b_list.append(ran_num[ball])
        print(f'{len(s_list)}S {len(b_list)}B')
               
    if len(s_list) == 3:
        print(f'입력횟수 : {cnt}')
        break
