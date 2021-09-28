# 컨트롤 할 크롬 브라우저 생성
driver = webdriver.Chrome('./chromedriver_win32/chromedriver.exe')
url = 'https://www.instagram.com/'
driver.get(url)
time.sleep(4)

# 인스타그램 로그인 클릭
ins_id = input('아이디를 입력하세요 : ')
pw = input('비밀번호를 입력하세요 : ')

driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(ins_id)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(pw)

# 인스타그램 로그인 정보 입력 후 로그인 버튼 클릭
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()

# 페이지 로딩에 약간의 시간이 필요하면
import time
time.sleep(3)

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
time.sleep(3)
