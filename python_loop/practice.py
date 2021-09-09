# ATM machine algorithm programming codes

### Functions ###

def print_wel():
    welcome = '''
    환영합니다. SSAC BANK입니다.

    ------ 거래를 위한 메뉴입니다. ------
                1. 입금
                2. 출금
                3. 잔액확인
                4. 종료
    '''
    return print(welcome)


def select_menu(menu):
    if 1 <= menu <= 4:
        menu = menu
    else:
        menu = int(input('1~4 중에 하나 선택하여 숫자로 다시 입력하세요: '))
        menu = menu
    return menu

### codes ###
print_wel()
bal = int(input('원하시는 잔액을 입금하세요: '))

while True:
        m = int(input('선택할 메뉴를 입력하세요: '))
        if not select_menu(m):
            print('거래를 종료합니다.')
            break

        else:
            if select_menu(m) == 1:
                deposit = int(input('입금할 금액을 입력하세요: '))
                print(f'입금하신 금액입니다: {deposit}원')
                deposit = deposit + bal
                answer = str(input('Y/N?'))
                if answer == 'Y':
                    next
                else:
                    print('거래를 종료합니다.')
                    break

            elif select_menu(m) == 2:
                withdrawal = int(input('출금할 금액을 입력하세요: '))
                print(f'출금하신 금액입니다: {withdrawal}원')

                if bal <= 0:
                    print('귀하의 잔액이 부족하므로 입금을 해주세요.')
                    deposit = int(input('입금할 금액을 입력하세요: '))
                    print(f'입금하신 금액입니다: {deposit}원')
                    deposit = deposit + bal - withdrawal
                    print('다음 거래로 진행됩니다.')
                    print('다음으로 진행하시겠습니까?')
                    answer = str(input('Y/N?'))
                    if answer == 'Y':
                        next
                    else:
                        print('거래를 종료합니다.')
                        break

                else:
                    bal -= withdrawal
                    print(f'남은 잔액은 {bal}원입니다.')
                    print('다음으로 진행하시겠습니까?')
                    if x == 'Y':
                        next
                    else:
                        print('거래를 종료합니다.')
                        break

            elif select_menu(m) == 3:
                balance = deposit - withdrawal
                if balance > 0:
                    print(f"귀하의 잔액은 {balance}원입니다.")
                    print('다음으로 진행하시겠습니까?')
                    answer = str(input('Y/N?'))
                    if answer == 'Y':
                        next
                    else:
                        print('거래를 종료합니다.')
                        break

                else:
                    deposit = 0
                    withdrawal = 0
                    print(f"귀하의 잔액은 {balance}원입니다.")
                    print('귀하의 잔액이 부족하므로 입금을 해주세요.')
                    if select_menu(1) == True:
                        deposit = int(input('입금할 금액을 입력하세요: '))
                        print(f'입금하신 금액입니다: {deposit}원')
                        deposit += deposit
                        print('다음으로 진행하시겠습니까?')
                        answer = str(input('Y/N?'))
                        if answer == 'Y':
                            next
                        else:
                            print('거래를 종료합니다.')
                            break

            else:
                print('거래를 종료합니다.')
                print(f'최종 잔액 확인: {bal}원')
                break
