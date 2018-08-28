# 정렬
# 카테고리
log_keys = [

]

category = [
    {"name": "db_error", "desc": "DB에 관련된 에러"},
    {"name": "socket_error", "desc": "소켓에 관련된 에러"},
    {"name": "settings_error", "desc": "세팅에 관련된 에러"},
    {"name": "etc_error", "desc": "기타 에러"},
]

# db에러
db_error_dict = {
    "DataBaseExceptionHandler + driver name :": "DB 드라이버 실패",
    "DataBaseExceptionHandler + conn url :": "DB 종류,아이피,포트,서비스이름 관련 실패 ",
    "DataBaseExceptionHandler + connection db exception :": "데이터베이스 연결 실패",
    "DB configuration file make exception": "DB 구성 파일 설정중 실패",
    "_Send SqlSessionFactory IOException : ": "Send 세션 생성 실패 ",
    "_Send Thread.sleep InterruptedException : ": "Send 쓰레드 인터럽트 ",
    "_Send permanence queue IOException : ": "Send 큐 입출력 에러 ",
    "_Send MySQL auto increment Exception : ": "MySQL 테이블 자동증가 에러",
    "selectMessage() exception : ": "DB에서 메세지를 가져오는 도중 에러",
    "session rollback exception : ": "세션 롤백도중 에러",
    "session close exception : ": "세션 닫는도중 에러",
    "setStatusForDBS Exception : ": "Status 에러",
    "setStatusForDBS Exception msgkey : ": "Msgkey 에러",
    "setStatus exception : ": "Status 에러",
    "getTimeOutMessage Exception : ": "메세지 가져오는 시간초과 ",
    "logSelectChk exception : ": "로그 Select 에러",
    "mysql auto_increment excute exception : ": "DB 테이블 기본키 자동증가 실패",
    "create msg table Exception : ": "Msg Table 생성 에러",
    "isNotExistTable exception : ": "존재하지 않는 테이블 ",
    "java.sql.SQLException": "데이터베이스 에러",

}

# 소켓에러
socket_error_dict = {
    "java.net.SocketException": "서버와 통신 실패",
    "Socket Close Fail...": "통신 종료 실패",
    "BIND Exception socketClose": "소켓 바인드 실패",
    "GET IP Exception": "IP를 가져오는데 실패.",
}
# 설정에러
settings_error_dict = {
    "Service, 설정 파일을 읽는 도중 에러 발생": "Service 설정 파일 읽는 도중 에러",
    "Data Base 설정 파일을 읽는 도중 에러 발생": "DB설정 파일을 읽는 도중 에러",
    "MyBatis Configure File Is Doesn't exist. ": "MyBatis 설정 파일이 존재하지 않는 에러",
    "DB configuration file make exception : ": "DB 구성 파일 에러",
    "previously used [db.xml] delete fail": "이전 사용중인 db.xml 파일 삭제 실패 에러",
    "No argument value for home ath": "홈 경로에 대한 값이 없는 에러",
}
# 기타 에
etc_error_dict = {
    "not found": "not found.",
}

# 전체 에러 리스트
# log_dict = {
#     "db_error": db_error_dict,
#     "socket_error": socket_error_dict,
#     "settings_error": settings_error_dict,
#     "etc_error": etc_error_dict,
# }

# import pprint
#
# temp_list = []
# for key, value in etc_error_dict.items():
#     temp_list.append({"keyword": key, "description": value, "category": 3})
#
# pprint.pprint(temp_list)

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
