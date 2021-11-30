# -*- coding: utf-8 -*- 
import sys
import os

import pymysql
import pandas
import base64
import requests

from pytz import timezone

# Fuzzbuzz RDS info
host        = 'fuzzbuzz-mysql.cwvbxvvwztug.ap-northeast-2.rds.amazonaws.com'
port        = 3306
username    = 'admin'
database    = 'fuzzbuzzdb'
password    = '123456789'

def RDS_connect(host, port, username, password, database):
    try:
        conn = pymysql.connect(
            host        = host,
            user        = username,
            passwd      = password,
            db          = database,
            port        = port,
            use_unicode = True,
            charset     = 'utf8mb4'
        )
        Cursor = conn.cursor()
        # RDS간에 SQL문을 주고 받는데 사용
    except:
        print("ERROR: RDS에 연결되지 않았습니다.")
        sys.exit(1)
    return conn, Cursor


# RDS 호출
conn, Cursor = RDS_connect(host, port, username, password, database)

query = """INSERT INTO fuzzbuzz_app1_userinfo VALUES ('', 'Park', '000555779', '서울시 서초구', now());"""
print( "** 실행쿼리문: ", query)
Cursor.execute(query)

# 해당 테이블 조회
print_sql = "SELECT * FROM fuzzbuzz_app1_userinfo"
Cursor.execute(print_sql)
# print(Cursor.fetchall())
print(pandas.DataFrame(Cursor.fetchall()))

conn.commit()

# connection:           데이터베이스에 접속을 하기 위한 모듈
#                       settings.py에 입력한 데이터베이스 정보를 가지고 접속
# cursor():             cursor 객체 생성
#                       cursor 란 SQL문을 수행하고 결과를 얻는데 사용하는 객체
# cursor.execute():     쿼리문을 연결된 DB로 보내 쿼리를 실행
# cursor.fetchall():    쿼리 실행 결과로 반환된 전체 데이터를 데이터베이스 서버로부터 가져옴
# connection.commit():  데이터에 대한 변경사항이 있다면 이를 확정, 갱신
# connection.close():   데이터베이스와의 연결을 닫음
# connection.rollback(): 쿼리문 실행 도중 잘못된 경우 실행 전으로 되돌려 놓음