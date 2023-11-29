import sqlite3
import time

# Pin 번호 num을 입력 하면 그에 해당하는 User 정보를 가져옴
def check_pin_num(num):
    # SQLite DB 파일과 연결
    db = sqlite3.connect("./database/data.db")
    cursor = db.cursor() # DB와 상호작용을 위한 커서 생성
    #f는 동적으로 num 변수를 사용하게 함
    cursor.execute(f'SELECT * FROM User WHERE Pin_Num =="{num}"')
    # num과 일치하는 Pin 번호와 일치하는 정보를 뽑아냄
    result = cursor.fetchone()
    # 그 중 첫 번째 레코드를 가져와 result에 저장
    return str(result) # 문자열로 변환 후 반환

# 현재 회원가입된 회원의 수를 반환
def check_seq_user():
    # SQLite DB 파일과 연결
    db = sqlite3.connect(f"./database/data.db")
    cursor = db.cursor() # DB와 상호작용을 위한 커서 생성

    cursor.execute(f"SELECT COUNT(*) FROM User")
    count = cursor.fetchone()[0]
    return int(count)


# 마지막 User의 Name과 Content(소속)를 가져옴
def get_last_user():
    db = sqlite3.connect(f"./database/data.db")
    cursor = db.cursor()
    cursor.execute(f'SELECT Name, Content FROM User Order By "Seq" DESC')
    try:
        data = cursor.fetchone()
        return list(data)
    except:
        return ["No Data", "No Data"]

# List 테이블(방명록)의 행 수를 확인
def check_seq_list():
    db = sqlite3.connect(f"./database/data.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM List")
    count = cursor.fetchone()[0]
    return int(count)

# 최근 데이터를 가져오는 함수
# Date, Time, Name, Content(소속)의 리스트를 가져오는 함수
def get_last_list():
    db = sqlite3.connect(f"./database/data.db")
    cursor = db.cursor()
    cursor.execute(f'SELECT Date, Time, Name, Content FROM List Order By "Seq" DESC')
    try:
        data = cursor.fetchone()
        return list(data)
    except:
        return ["No Data", "No Data", "No Data", "No Data"]

def get_list(sort, desc):
    db = sqlite3.connect(f"./database/data.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM List")
    # 반복문을 실행하기 위한 방명록의 count 정보 가져옴
    count_lists = cursor.fetchone()[0]
    get_list = [] # 결과를 저장할 빈 리스트인 'get_list'를 생성
    if int(desc) == 0: # 내림차순이 아니면... -> 오름차순// sort를 기준으로 오름차순
        cursor.execute(f'SELECT * FROM List Order By "{sort}"')
    else: # 내림차순, sort를 기준으로 내림차순
        cursor.execute(f'SELECT * FROM List Order By "{sort}" DESC')

    for i in range(count_lists):
        # 레코드를 하나씩 가져와 get_list에 추가
        li = cursor.fetchone()[1:]
        get_list.append(li)
    return get_list # 정렬된 데이터들을 반환


# 회원 테이블에 count(seq번호), num(pin번호), name(이름), content(소속)
def input_Name(num, name, content):
    db = sqlite3.connect("./database/data.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM User")
    count = cursor.fetchone()[0]
    insert_query = f"INSERT INTO User VALUES('{count+1}','{num}','{name}','{content}')"
    # 쿼리문 실행
    cursor.execute(insert_query)
    # 변경사항을 데이터베이스에 반영하기 위해 커밋을 수행
    db.commit()

# 방명록 테이블에 레코드를 저장
# count, Date, Time, name(성명), content(소속)을 저장
def save(num):
    db = sqlite3.connect("./database/data.db")
    cursor = db.cursor()
    # 방명록 테이블의 레코드수를 가져옴
    cursor.execute(f"SELECT COUNT(*) FROM List")
    count = cursor.fetchone()[0]
    
    # pin번호에 맞는 성명과 소속을 가져옴
    cursor.execute(f'SELECT Name, Content FROM User WHERE Pin_Num =="{num}"')
    data = cursor.fetchone()
    name = data[0]
    content = data[1]
    now = time.localtime() # 현재 시간을 로컬 시간대로 가져옴
    Date = "%04d년 %02d월 %02d일" % (now.tm_year, now.tm_mon, now.tm_mday)
    Time = "%02d시 %02d분 %02d초" % (now.tm_hour, now.tm_min, now.tm_sec)
    insert_query = (
        f"INSERT INTO List VALUES('{count+1}','{Date}','{Time}','{name}','{content}')"
    )
    cursor.execute(insert_query)
    db.commit()
