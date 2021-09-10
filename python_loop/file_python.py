# Python codes (log data with time and loop by practicing reading and writing codes)

f = open('file_log.txt', 'w', encoding='euc-kr')
while True:
    import time
    from datetime import datetime as dt
    text = f'{i} 로그 데이터: {dt.now()} \n'
    time.sleep(2)
    f.write(text) 

f = open('file_nm.txt', 'r', encoding='euc-kr')
text_line = f.readlines()
f.close()

text_line
