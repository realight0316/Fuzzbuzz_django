# Fuzzbuzz_django
팀 'Fuzzbuzz'의 'AWS와 Deeplearning을 활용한 공간 혼잡도'의 Django Server 파일을 다루고 있습니다.
2021.12.02 서비스 종료

## 목차

1. [서비스 환경 기본 정보](#1-서비스-환경-기본-정보)

2. [디렉토리 구조](#2-디렉토리-구조)

3. [데이터 베이스 구조](#3-데이터-베이스-구조)

4. [REST API](#4-REST-API)



## 1. 서비스 환경 기본 정보

- AWS
    - EC2 / Amazon Linux = 2
    - RDS / MySQL = 8.0.23
- Linux/Django
    - Python = 3.7.10
    - Django = 3.2.8
    - Django rest framework = 3.12.4
    - Requests = 2.26.0
    - PyMySQL = 1.0.2
    - MySQLclient = 2.0.3
    - Sqlparse = 0.4.2
    - uWSGI = 2.0.20
    - bootstrap4 = 0.1.0

## 2. 디렉토리 구조

```markdown
.
├── config
│   ├── nginx
│   │   └── fuzzbuzz_django.conf
│   └── uwsgi
│       ├── fuzzbuzz_django.ini
│       ├── log
│       │   ├── 2021-11-24.log
│       │   ├── 2021-11-25.log
│       │   ├── 2021-11-29.log
│       │   ├── 2021-11-30.log
│       │   └── 2021-12-01.log
│       └── uwsgi.service
├── fuzzbuzz_app1
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_auto_20211123_1455.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-37.pyc
│   │       ├── 0002_answers_congestion_points_questions.cpython-37.pyc
│   │       ├── 0002_auto_20211026_1127.cpython-37.pyc
│   │       ├── 0002_auto_20211026_1606.cpython-37.pyc
│   │       ├── 0002_auto_20211119_1621.cpython-37.pyc
│   │       ├── 0002_auto_20211119_1640.cpython-37.pyc
│   │       ├── 0002_auto_20211123_1455.cpython-37.pyc
│   │       ├── 0002_rename_call_userinfo_phone.cpython-37.pyc
│   │       ├── 0002_user_account_is_superuser.cpython-37.pyc
│   │       ├── 0002_user.cpython-37.pyc
│   │       ├── 0003_alter_congestion_points_people.cpython-37.pyc
│   │       ├── 0004_alter_congestion_points_people.cpython-37.pyc
│   │       └── __init__.cpython-37.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-37.pyc
│   │   ├── apps.cpython-37.pyc
│   │   ├── __init__.cpython-37.pyc
│   │   ├── models.cpython-37.pyc
│   │   ├── serializers.cpython-37.pyc
│   │   ├── urls.cpython-37.pyc
│   │   └── views.cpython-37.pyc
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── fuzzbuzz_django
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   ├── settings.cpython-37.pyc
│   │   ├── urls.cpython-37.pyc
│   │   ├── views.cpython-37.pyc
│   │   └── wsgi.cpython-37.pyc
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── manage.py
├── RDS_connect.py
├── requirements.txt
├── restful_transmit.py
├── static
│   ├── admin
│   │   ├── css
│   │   │   ├── autocomplete.css
│   │   │   ├── base.css
│   │   │   ├── changelists.css
│   │   │   ├── dashboard.css
│   │   │   ├── fonts.css
│   │   │   ├── forms.css
│   │   │   ├── login.css
│   │   │   ├── nav_sidebar.css
│   │   │   ├── responsive.css
│   │   │   ├── responsive_rtl.css
│   │   │   ├── rtl.css
│   │   │   ├── vendor
│   │   │   │   └── select2
│   │   │   │       ├── LICENSE-SELECT2.md
│   │   │   │       ├── select2.css
│   │   │   │       └── select2.min.css
│   │   │   └── widgets.css
│   │   ├── fonts
│   │   │   ├── LICENSE.txt
│   │   │   ├── README.txt
│   │   │   ├── Roboto-Bold-webfont.woff
│   │   │   ├── Roboto-Light-webfont.woff
│   │   │   └── Roboto-Regular-webfont.woff
│   │   ├── img
│   │   │   ├── calendar-icons.svg
│   │   │   ├── gis
│   │   │   │   ├── move_vertex_off.svg
│   │   │   │   └── move_vertex_on.svg
│   │   │   ├── icon-addlink.svg
│   │   │   ├── icon-alert.svg
│   │   │   ├── icon-calendar.svg
│   │   │   ├── icon-changelink.svg
│   │   │   ├── icon-clock.svg
│   │   │   ├── icon-deletelink.svg
│   │   │   ├── icon-no.svg
│   │   │   ├── icon-unknown-alt.svg
│   │   │   ├── icon-unknown.svg
│   │   │   ├── icon-viewlink.svg
│   │   │   ├── icon-yes.svg
│   │   │   ├── inline-delete.svg
│   │   │   ├── LICENSE
│   │   │   ├── README.txt
│   │   │   ├── search.svg
│   │   │   ├── selector-icons.svg
│   │   │   ├── sorting-icons.svg
│   │   │   ├── tooltag-add.svg
│   │   │   └── tooltag-arrowright.svg
│   │   └── js
│   │       ├── actions.js
│   │       ├── admin
│   │       │   ├── DateTimeShortcuts.js
│   │       │   └── RelatedObjectLookups.js
│   │       ├── autocomplete.js
│   │       ├── calendar.js
│   │       ├── cancel.js
│   │       ├── change_form.js
│   │       ├── collapse.js
│   │       ├── core.js
│   │       ├── inlines.js
│   │       ├── jquery.init.js
│   │       ├── nav_sidebar.js
│   │       ├── popup_response.js
│   │       ├── prepopulate_init.js
│   │       ├── prepopulate.js
│   │       ├── SelectBox.js
│   │       ├── SelectFilter2.js
│   │       ├── urlify.js
│   │       └── vendor
│   │           ├── jquery
│   │           │   ├── jquery.js
│   │           │   ├── jquery.min.js
│   │           │   └── LICENSE.txt
│   │           ├── select2
│   │           │   ├── i18n
│   │           │   │   ├── af.js
│   │           │   │   ├── ar.js
│   │           │   │   ├── az.js
│   │           │   │   ├── bg.js
│   │           │   │   ├── bn.js
│   │           │   │   ├── bs.js
│   │           │   │   ├── ca.js
│   │           │   │   ├── cs.js
│   │           │   │   ├── da.js
│   │           │   │   ├── de.js
│   │           │   │   ├── dsb.js
│   │           │   │   ├── el.js
│   │           │   │   ├── en.js
│   │           │   │   ├── es.js
│   │           │   │   ├── et.js
│   │           │   │   ├── eu.js
│   │           │   │   ├── fa.js
│   │           │   │   ├── fi.js
│   │           │   │   ├── fr.js
│   │           │   │   ├── gl.js
│   │           │   │   ├── he.js
│   │           │   │   ├── hi.js
│   │           │   │   ├── hr.js
│   │           │   │   ├── hsb.js
│   │           │   │   ├── hu.js
│   │           │   │   ├── hy.js
│   │           │   │   ├── id.js
│   │           │   │   ├── is.js
│   │           │   │   ├── it.js
│   │           │   │   ├── ja.js
│   │           │   │   ├── ka.js
│   │           │   │   ├── km.js
│   │           │   │   ├── ko.js
│   │           │   │   ├── lt.js
│   │           │   │   ├── lv.js
│   │           │   │   ├── mk.js
│   │           │   │   ├── ms.js
│   │           │   │   ├── nb.js
│   │           │   │   ├── ne.js
│   │           │   │   ├── nl.js
│   │           │   │   ├── pl.js
│   │           │   │   ├── ps.js
│   │           │   │   ├── pt-BR.js
│   │           │   │   ├── pt.js
│   │           │   │   ├── ro.js
│   │           │   │   ├── ru.js
│   │           │   │   ├── sk.js
│   │           │   │   ├── sl.js
│   │           │   │   ├── sq.js
│   │           │   │   ├── sr-Cyrl.js
│   │           │   │   ├── sr.js
│   │           │   │   ├── sv.js
│   │           │   │   ├── th.js
│   │           │   │   ├── tk.js
│   │           │   │   ├── tr.js
│   │           │   │   ├── uk.js
│   │           │   │   ├── vi.js
│   │           │   │   ├── zh-CN.js
│   │           │   │   └── zh-TW.js
│   │           │   ├── LICENSE.md
│   │           │   ├── select2.full.js
│   │           │   └── select2.full.min.js
│   │           └── xregexp
│   │               ├── LICENSE.txt
│   │               ├── xregexp.js
│   │               └── xregexp.min.js
│   ├── assets
│   │   ├── brand
│   │   │   ├── bee.svg
│   │   │   ├── bootstrap-logo.svg
│   │   │   └── bootstrap-logo-white.svg
│   │   └── dist
│   │       ├── css
│   │       │   ├── bootstrap.min.css
│   │       │   ├── bootstrap.min.css.map
│   │       │   ├── bootstrap.rtl.min.css
│   │       │   └── bootstrap.rtl.min.css.map
│   │       └── js
│   │           ├── bootstrap.bundle.min.js
│   │           └── bootstrap.bundle.min.js.map
│   ├── css
│   │   ├── dashboard.css
│   │   ├── dashboard.rtl.css
│   │   └── signin.css
│   ├── js
│   │   └── dashboard.js
│   └── rest_framework
│       ├── css
│       │   ├── bootstrap.min.css
│       │   ├── bootstrap-theme.min.css
│       │   ├── bootstrap-tweaks.css
│       │   ├── default.css
│       │   ├── font-awesome-4.0.3.css
│       │   └── prettify.css
│       ├── docs
│       │   ├── css
│       │   │   ├── base.css
│       │   │   ├── highlight.css
│       │   │   └── jquery.json-view.min.css
│       │   ├── img
│       │   │   ├── favicon.ico
│       │   │   └── grid.png
│       │   └── js
│       │       ├── api.js
│       │       ├── highlight.pack.js
│       │       └── jquery.json-view.min.js
│       ├── fonts
│       │   ├── fontawesome-webfont.eot
│       │   ├── fontawesome-webfont.svg
│       │   ├── fontawesome-webfont.ttf
│       │   ├── fontawesome-webfont.woff
│       │   ├── glyphicons-halflings-regular.eot
│       │   ├── glyphicons-halflings-regular.svg
│       │   ├── glyphicons-halflings-regular.ttf
│       │   ├── glyphicons-halflings-regular.woff
│       │   └── glyphicons-halflings-regular.woff2
│       ├── img
│       │   ├── glyphicons-halflings.png
│       │   ├── glyphicons-halflings-white.png
│       │   └── grid.png
│       └── js
│           ├── ajax-form.js
│           ├── bootstrap.min.js
│           ├── coreapi-0.1.1.js
│           ├── csrf.js
│           ├── default.js
│           ├── jquery-3.5.1.min.js
│           └── prettify-min.js
└── templates
    ├── base.html
    ├── chart.html
    ├── index.html
    ├── nav.html
    ├── signin.html
    └── signup.html
```

## 3. 데이터 베이스 구조

Django 기본 생성 테이블 제외

- fuzzbuzz_app1_user_account : Django 사용자정보 커스텀 테이블
    
    
    | Field | Type | definition | note |
    | --- | --- | --- | --- |
    | id | bigint | 계정 고유 번호 | auto_increment, primary key |
    | password | varchar | 비밀번호 |  |
    | email | varchar | 이메일 주소 |  |
    | username | varchar | 사용자명 |  |
    | date_signup | datetime | 계정 생성일자 |  |
    | last_login | datetime | 마지막 접속일자 |  |
    | is_active | tinyint | 활성화 여부 | 0 비활성화, 1 활성화 |
    | is_staff | tinyint | 스태프 권한 | 0 권한 없음, 1 권한 부여 |
    | is_admin | tinyint | 관리자 권한 | 0 권한 없음, 1 권한 부여 |
    | is_superuser | tinyint | Superuser 권한 | 0 권한 없음, 1 권한 부여 |
- fuzzbuzz_app1_congestion_points_sh : DL-1 혼잡도 테이블
    
    
    | Field | Type | definition | note |
    | --- | --- | --- | --- |
    | id | bigint | 데이터 고유 번호 | auto_increment, primary key |
    | input_time | datetime | 입력일자 |  |
    | value | double | 혼잡도 값 |  |
    | people | int | 사람 수 |  |
- fuzzbuzz_app1_congestion_points_hj : DL-2 혼잡도 테이블
    
    
    | Field | Type | definition | note |
    | --- | --- | --- | --- |
    | id | bigint | 데이터 고유 번호 | auto_increment, primary key |
    | input_time | datetime | 입력일자 |  |
    | value | double | 혼잡도 값 |  |
    | people | int | 사람 수 |  |
- fuzzbuzz_app1_turnover_points_sh : DL-1 유입량 테이블
    
    
    | Field | Type | definition | note |
    | --- | --- | --- | --- |
    | id | bigint | 데이터 고유 번호 | auto_increment, primary key |
    | input_time | datetime | 입력일자 |  |
    | total_turn | int | 신규 유입 횟수 |  |
- fuzzbuzz_app1_questions : 서비스 FAQ 테이블
    
    
    | Field | Type | definition | note |
    | --- | --- | --- | --- |
    | id | bigint | 데이터 고유 번호 | auto_increment, primary key |
    | Q_text | longtext | FAQ 질문 |  |
    | A_text | longtext | FAQ 답변 |  |
    | time | datetime | 작성일자 |  |

## 4. REST API

- Android 어플리케이션 통신
    
    
    | Method | URL | Definition |
    | --- | --- | --- |
    | POST | /app-con | 혼잡도 최신값 조회 |
    | POST | /app-faq | FAQ 내용 조회 |
- DeepLearning 데이터 통신
    
    
    | Method | URL | Definition |
    | --- | --- | --- |
    | POST | /dl-con-sh | DL-1 혼잡도 산출값 입력 |
    | POST | /dl-con-hj | DL-2 혼잡도 산출값 입력 |
    | POST | /dl-cir-sh | DL-1 유입량 산출값 입력 |
    | POST | /dl-cir-hj | DL-2 유입량 산출값 입력 |
- Django 웹페이지 통신
    
    
    | Method | URL | Definition |
    | --- | --- | --- |
    | POST | /app1/login | Django 웹페이지 로그인 |
    | POST | /app1/signup | Django 웹페이지 회원가입 |
    | POST | /app1/chart | DB연동 데이터 시각화 (차트) |

## Developers

- 권송미 (Android application / [https://github.com/songmik](https://github.com/songmik))
- 김혜진 (Deep-Learning / [https://github.com/GIMEA](https://github.com/GIMEA))
- 한성현 (Deep-Learning / [https://github.com/SaintSeong](https://github.com/SaintSeong))
- 김진환 (Back-End / [https://github.com/realight0316](https://github.com/realight0316))

[👆맨위로](#Fuzzbuzz_django)
