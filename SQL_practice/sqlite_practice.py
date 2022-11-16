### 서울시 월별 평균 대기오염도 정보 (Seoul monthly average air pollution information)
# make table object using SQL queries
import sqlite3                            
conn = sqlite3.connect('dust.sqlite')  
cursor = conn.cursor()              
cursor.executescript('''            
   drop table if exists items;
   create table dust (no integer primary key,
      area text unique,  amount integer );                    
   insert into dust (area, amount) values ("강남구","25");
   insert into dust (area, amount) values ("강동구","21");
   insert into dust (area, amount) values ("노원구","22");
   insert into dust (area, amount) values ("마포구","23");
''')
conn.commit()   
cur = conn.cursor()       
cur.execute('select * from dust')   
dust_list = cur.fetchall()  
print(dust_list)

# Loop to print the result
#반복문
for values in dust_list:     #컬럼 2개 전체 데이터 출력
    print(values[1], values[2])

for values in dust_list:     #조건에 따른 데이터 출력
    if values[2] >=23:
        print(values[1], values[2])

# select 구문(SQL query started with 'select ~') -- 두번째 반복문 코딩 결과와 동일하게 출력
cur = conn.cursor()
cur.execute('select * from dust where amount >=23')
dust_list = cur.fetchall()
print(dust_list)

sql = "insert into dust (area, amount) values ('종로구','22')"
cur = conn.cursor()
cur.execute(sql)
conn.commit()

cur = conn.cursor()
cur.execute('select * from dust')
dust_list = cur.fetchall()
print(dust_list)
conn.close()    #데이터 베이스 접속을 종료해주는 기능. 잊지말고 꼭 해줘야 한다는 것. (Do not forget this!!)

drop table dust purge ;
create table dust(
no number(3) primary key,
estmonth date default sysdate,
area varchar2(10) unique,
amount number(3) not null);

insert into dust values(1, '2021-07-01', '강남구',25);
insert into dust values(2, '2021-07-01', '강동구',21);
insert into dust values(3, '2021-07-01', '강북구',23);
insert into dust values(4, '2021-07-01', '강서구',22);
insert into dust values(5, '2021-07-01', '구로구',18);
insert into dust values(6, '2021-07-01', '금천구',25);
insert into dust values(7, '2021-07-01', '노원구',22);
insert into dust values(8, '2021-07-01', '동작구',26);
insert into dust values(9, '2021-07-01', '마포구',23);

commit;  #완전 중요한 부분이다. 테이블 객체를 생성하고 완전히 데이터 객체로 db에 저장하기 위해서는 반드시 입력해야한다!! (Important!! To create table object and to save the data into DB)

select * from dust;

pip install cx_Oracle   #미리 설치해야 함
import cx_Oracle 

conn = cx_Oracle.connect(오라클 사용자 아이디/user_id, 비밀번호/pw, IP주소값/IP address)
cur = conn.cursor()
cur.execute("select * from dust")
dust_list= cur.fetchall()

print(dust_list)

for values in dust_list:   #깔끔하게 출력하고 싶다면 반복문을 쓰자
    print(values)

# EXAMPLE
'''
Q: 이 데이터 객체에 '영등포구'와 '용산구' 정보 추가하고 해당 두 구의 정보(번호, 구명, 미세먼지 농도)만 출력하기
'''
insert into dust values(10, '2021-07-01', '영등포구',24); #파이썬에서는 값의 크기 오류가 나서 안된다...
                                                          #그래서 오라클에서 객체생성시 varchar2(10)을 20으로 바꿨더니 된다..
insert into dust values(11, '2021-07-01', '용산구',22);
commit;

#파이썬 입력내용
sql1 = "insert into dust values(10, '2021-07-01', '영등포구',24)"
cur = conn.cursor()
cur.execute(sql1)
conn.commit()

sql2 = "insert into dust values(11, '2021-07-01', '용산구',22)"
cur = conn.cursor()
cur.execute(sql2)
conn.commit()

cur = conn.cursor()
cur.execute("select no, area, amount from dust where area in ('영등포구','용산구')")
dust_list= cur.fetchall()
for values in dust_list:
    print('번호:',values[0], '구:', values[1], '농도:', values[2])
