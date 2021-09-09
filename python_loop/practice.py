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
