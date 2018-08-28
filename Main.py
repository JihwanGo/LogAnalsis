# -- coding: utf-8 --
import glob, errno
#from Log_msg_translation import *
import operator





# TODO: 오류 추가
# TODO: 보기 좋게 데이터 가공
# TODO: 데이터 정리
# TODO: 예외 처리
# TODO: 인코딩 문제 해결해야함.





DEBUG_MODE = True


#데이터
log_dict = [
    ## db_error
    {'category': 0,
     'description': 'DB 드라이버 실패',
     'keyword': 'DataBaseExceptionHandler + driver name :'},
    {'category': 0,
     'description': 'DB 종류,아이피,포트,서비스이름 관련 실패 ',
     'keyword': 'DataBaseExceptionHandler + conn url :'},
    {'category': 0,
     'description': '데이터베이스 연결 실패',
     'keyword': 'DataBaseExceptionHandler + connection db exception :'},
    {'category': 0,
     'description': 'DB 구성 파일 설정중 실패',
     'keyword': 'DB configuration file make exception'},
    {'category': 0,
     'description': 'Send 세션 생성 실패 ',
     'keyword': '_Send SqlSessionFactory IOException : '},
    {'category': 0,
     'description': 'Send 쓰레드 인터럽트 ',
     'keyword': '_Send Thread.sleep InterruptedException : '},
    {'category': 0,
     'description': 'Send 큐 입출력 에러 ',
     'keyword': '_Send permanence queue IOException : '},
    {'category': 0,
     'description': 'MySQL 테이블 자동증가 에러',
     'keyword': '_Send MySQL auto increment Exception : '},
    {'category': 0,
     'description': 'DB에서 메세지를 가져오는 도중 에러',
     'keyword': 'selectMessage() exception : '},
    {'category': 0,
     'description': '세션 롤백도중 에러',
     'keyword': 'session rollback exception : '},
    {'category': 0,
     'description': '세션 닫는도중 에러',
     'keyword': 'session close exception : '},
    {'category': 0,
     'description': 'Status 에러',
     'keyword': 'setStatusForDBS Exception : '},
    {'category': 0,
     'description': 'Msgkey 에러',
     'keyword': 'setStatusForDBS Exception msgkey : '},
    {'category': 0,
     'description': 'Status 에러',
     'keyword': 'setStatus exception : '},
    {'category': 0,
     'description': '메세지 가져오는 시간초과 ',
     'keyword': 'getTimeOutMessage Exception : '},
    {'category': 0,
     'description': '로그 Select 에러',
     'keyword': 'logSelectChk exception : '},
    {'category': 0,
     'description': 'DB 테이블 기본키 자동증가 실패',
     'keyword': 'mysql auto_increment excute exception : '},
    {'category': 0,
     'description': 'Msg Table 생성 에러',
     'keyword': 'create msg table Exception : '},
    {'category': 0,
     'description': '존재하지 않는 테이블 ',
     'keyword': 'isNotExistTable exception : '},
    {'category': 0,
     'description': '데이터베이스 에러',
     'keyword': 'java.sql.SQLException'},

    ## socket_error
    {'category': 1,
     'description': '서버와 통신 실패',
     'keyword': 'java.net.SocketException'},
    {'category': 1, 'description': '통신 종료 실패', 'keyword': 'Socket Close Fail...'},
    {'category': 1,
     'description': '소켓 바인드 실패',
     'keyword': 'BIND Exception socketClose'},
    {'category': 1, 'description': 'IP를 가져오는데 실패.', 'keyword': 'GET IP Exception'},

    ## settings_error
    {'category': 2,
     'description': 'Service 설정 파일 읽는 도중 에러',
     'keyword': 'Service, 설정 파일을 읽는 도중 에러 발생'},
    {'category': 2,
     'description': 'DB설정 파일을 읽는 도중 에러',
     'keyword': 'Data Base 설정 파일을 읽는 도중 에러 발생'},
    {'category': 2,
     'description': 'MyBatis 설정 파일이 존재하지 않는 에러',
     'keyword': "MyBatis Configure File Is Doesn't exist. "},
    {'category': 2,
     'description': 'DB 구성 파일 에러',
     'keyword': 'DB configuration file make exception : '},
    {'category': 2,
     'description': '이전 사용중인 db.xml 파일 삭제 실패 에러',
     'keyword': 'previously used [db.xml] delete fail'},
    {'category': 2,
     'description': '홈 경로에 대한 값이 없는 에러',
     'keyword': 'No argument value for home ath'},

    ## etc_error
    {'category': 3, 'description': 'not found.', 'keyword': 'not found'},
]

# count 0으로 초기화
def init_stat_dict():
    for error_item in log_dict:
        error_item.update({"count": 0})


# 분석할 파일이 위치한 경로 리턴
def get_log_path():
    # 해당 디렉토리 파일 순회
    if DEBUG_MODE:
        return('/Users/hwangjihwan/desktop/list')
    else:
        path = input('폴더 안에 파일리스트 검사 경로: ')
        return path


# path 경로 안의 extension을 가진 파일 목록 리턴
def get_files(path, extension):
    test = path + extension
    files = glob.glob(test)
    return files


# 한 줄에 키워드 발견시 count 값 증가
def increase_count(line):
    for err_item in log_dict:
        print(err_item['keyword'])
        if err_item['keyword'] in line:
            err_item['count'] += 1


# 로그 파일에서 키워드를 찾아 카운트 값을 올려줌
def analyze_stat(file):
    try:
        with open(file, encoding='utf-8') as f:
            for line in f:
                increase_count(line)

    except IOError as exc:
        if exc.errno != errno.EISDIR:
            raise


# 통계 결과 출력 형식
def print_stat_result(result_dict):
    result_dict.sort(key=operator.itemgetter('count'))
    for err_item in result_dict:
        if err_item['count'] is 0:
            continue
        print(err_item['description'], err_item['count'], "건")







if __name__ == '__main__':


    if DEBUG_MODE:
        _programStart = '1'
    else:
        _programStart = input('시작 1 종료 2 : ')


    while _programStart == '1':
        init_stat_dict()
        files = get_files(get_log_path(), '/*.log')
        for file in files:
            analyze_stat(file)
        print_stat_result(log_dict)
        _programStart = input("다시 시작 1번 종료 2번 :")

    if _programStart == "2":
        print("종료됨")


