from django.db.models import query
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.db import connection

import requests, pymysql, sys, datetime

from rest_framework.parsers import JSONParser

from .models import Congestion_points_HJ, Congestion_points_SH, Questions, User_Account, turnover_points_SH
# from .serializers import Userinfo_serializer

# Create your views here.

# @csrf_exempt
# def Userinfo_list(request):
#     if request.method == 'GET':
#         query_set = Userinfo.objects.all()
#         serializer = Userinfo_serializer(query_set, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = Userinfo_serializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
        

# @csrf_exempt
# def Userinfo1(request, pk):
#     obj = Userinfo.objects.get(pk=pk)
#     # 선택된 데이터는 obj

#     if request.method == 'GET':
#         serializer = Userinfo_serializer(obj)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = Userinfo_serializer(obj, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         obj.delete()
#         return HttpResponse(status=204)


@csrf_exempt
def web_login(request):
    if request.method == 'POST':
        print("Request log: " + str(request.body))
        id = request.POST.get('user_id', '')
        pw = request.POST.get('user_pw', '')
        print("아이디: " + id + " / 패스워드: " + pw)

        result = authenticate(username=id, password=pw)
        if result:
            print("로그인 성공")
            login(request, result)
            redirect('fuzzbuzz_app1:login')
            return HttpResponse(status=200)
        else:
            print("로그인 실패")
            return HttpResponse(status=400)
    return render(request, 'signin.html')


@csrf_exempt
def app_login(request):
    if request.method == 'POST':
        print("Request log: " + str(request.body))
        id = request.POST.get("userid", '')
        pw = request.POST.get("userpw", '')
        print("아이디: " + id + " / 패스워드: " + pw)

        result = authenticate(username=id, password=pw)
        if result:
            print("로그인 성공")
            return JsonResponse({'code' : '0000', 'msg' : '로그인 성공'}, status=200)
        else:
            print("로그인 실패")
            return JsonResponse({'code' : '1001', 'msg' : '로그인 실패'}, status=200)
    return render(request, 'signin.html')


def web_logout(request):
    logout(request)
    return redirect("fuzzbuzz_app1:login")


def web_signup(request):
    if request.method=='POST':
        print(request.POST)
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]

        user = User_Account.objects.create_user(email, username, password)
        user.save()
        return redirect("fuzzbuzz_app1:login")
        
    return render(request, "signup.html")

def web_chart(request):
    condata = Congestion_points_SH.objects.all()
    turdata = turnover_points_SH.objects.all()
    context = {
        'condata' : condata,
        'turdata' : turdata,
    }
    return render(request, 'chart.html', context)


@csrf_exempt
def app_signup(request):
    if request.method == 'POST':
        print("\nRequest log: " + str(request.body))
        email       = request.POST.get('email', '')
        username    = request.POST.get('username', '')
        password    = request.POST.get('password', '')
        print(email + username + password)

        if email and username and password:
            print("**신규가입\n이메일: " + email + '\n사용자명: ' + username)
            user = User_Account.objects.create_user(email, username, password)
            user.save()
            return JsonResponse({'code' : '200', 'email' : email, 'username' : username}, status=200)
        else:
            print("**신규가입실패")
            return JsonResponse({'code' : '400'}, status=200)
    return render(request, 'signin.html')


# dl-con로 보낸 내용을 수신
@csrf_exempt
def dl_con_hj(request):             # Deep-Learning 혼잡도 HJ
    if request.method == 'POST':
        print("\nRequest log: " + str(request.body))
        input_time = request.POST.get("input_time", '')
        value      = request.POST.get("value", '')
        all_human  = request.POST.get("all_human", '')
        print("input_time: " + input_time + " / value: " + value + " / people: " + all_human)

        if input_time and value:
            curs = connection.cursor()  # setting.py에 구성된 db로 바로 연결 // from django.db import connection
            query = """INSERT INTO fuzzbuzz_app1_congestion_points_hj VALUES (null, '{}', '{}', '{}');""".format(input_time, value, all_human)
            curs.execute(query)
            fetchall = curs.fetchall()

            connection.commit()
            connection.close()
        else:
            print("Error: null값은 전송할 수 없습니다.")
            return HttpResponse(status=400)

        # input_time = datetime.datetime.strptime(input_time, '%Y-%m-%d %H:%M:%S')
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


@csrf_exempt
def dl_con_sh(request):             # Deep-Learning 혼잡도 HJ
    if request.method == 'POST':
        print("\nRequest log: " + str(request.body))
        input_time = request.POST.get("input_time", '')
        value      = request.POST.get("value", '')
        all_human = request.POST.get("all_human", '')
        print("input_time: " + input_time + " / value: " + value + " / people: " + all_human)

        if input_time and value and all_human:
            curs = connection.cursor()  # setting.py에 구성된 db로 바로 연결 // from django.db import connection
            query = """INSERT INTO fuzzbuzz_app1_congestion_points_sh VALUES (null, '{}', '{}', '{}');""".format(input_time, value, all_human)
            curs.execute(query)
            fetchall = curs.fetchall()

            connection.commit()
            connection.close()
        else:
            print("Error: null값은 전송할 수 없습니다.")
            return HttpResponse(status=400)

        # input_time = datetime.datetime.strptime(input_time, '%Y-%m-%d %H:%M:%S')
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)






# dl-cir로 보낸 내용을 수신
@csrf_exempt
def dl_cir_hj(request):
    if request.method == 'POST':
        print("\nRequest log: " + str(request.body))
        input_time = request.POST.get("input_time", '')
        table_id   = request.POST.get("table_id", '')
        
        print("""
        input_time: {}
        table_id  : {}
        """.format(input_time,  table_id))

        if input_time and table_id:
            curs = connection.cursor()  # setting.py에 구성된 db로 바로 연결 // from django.db import connection
            query = """INSERT INTO fuzzbuzz_app1_turnover_temp_hj VALUES (null, '{}', '{}');""".format(input_time, table_id)
            curs.execute(query)
            fetchall = curs.fetchall()

            connection.commit()
            connection.close()
        else:
            print("Error: null값은 전송할 수 없습니다.")
            return HttpResponse(status=400)

        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)

@csrf_exempt
def dl_cir_sh(request):
    if request.method == 'POST':
        print("\nRequest log: " + str(request.body))
        input_time = request.POST.get("input_time", '')
        total_turn = request.POST.get("total_turn", '')
        
        print("""
        input_time: {}
        total_turn: {}
        """.format(input_time,  total_turn))

        if input_time and total_turn:
            curs = connection.cursor()  # setting.py에 구성된 db로 바로 연결 // from django.db import connection
            query = """INSERT INTO fuzzbuzz_app1_turnover_points_sh VALUES (null, '{}', '{}');""".format(input_time, total_turn)
            curs.execute(query)
            fetchall = curs.fetchall()

            connection.commit()
            connection.close()
        else:
            print("Error: null값은 전송할 수 없습니다.")
            return HttpResponse(status=400)

        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


# Q&A 데이터 송수신
@csrf_exempt
def app_FAQ(request):
    if request.method == 'POST':
        print("Request log: " + str(request.body))
        FAQID = request.POST.get("idx", '')
        print("요청된 질문번호: " + FAQID)
        if FAQID:
            curs = connection.cursor()
            query = """Select Q_text, A_text from fuzzbuzz_app1_questions where id = {}""".format(FAQID)
            curs.execute(query)
            result = curs.fetchall()
            
            Q_text = result[0][0]
            A_text = result[0][1]
            print(Q_text)
            print(A_text)

            return JsonResponse({'Q_text' : '{}'.format(Q_text), 'A_text' : '{}'.format(A_text)}, status=200)
        else:
            return JsonResponse({'Q_text' : '해당번호의 질문이 없습니다.', 'A_text' : '해당번호의 답변이 없습니다.'}, status=400)
    else:
        return HttpResponse(status=400)

# @csrf_exempt
# def app_con(request):
#     if request.method == 'POST':
#         print()
#         print("현재시간: ", datetime.datetime.now())
#         print("Request log: " + str(request.body))
#         idx = request.POST.get("idx", '')
#         print("혼잡도 요청코드: " + idx)

#         if idx == 'concon':
#             curs = connection.cursor()
#             query = """select * from fuzzbuzz_app1_congestion_points_hj where input_time = (select max(input_time) from fuzzbuzz_app1_congestion_points_hj);"""
#             curs.execute(query)
#             result = curs.fetchall()

#             input_time = result[0][1]
#             input_time = datetime.datetime.strftime(input_time, '%Y-%m-%d %H:%M')
#             value      = result[0][2]

#             print('input_time: ', input_time)
#             print('value: ', value)
        
#             return JsonResponse({'input_time' : '{}'.format(input_time), 'value' : '{}'.format(value)})
#         else:
#             return JsonResponse({'input_time' : 'error: 요청코드 불일치', 'value' : 'null'})
#     else:
#         return HttpResponse(status=400)

@csrf_exempt
def app_con(request):
    if request.method == 'POST':
        print()
        print("현재시간: ", datetime.datetime.now())
        print("Request log: " + str(request.body))
        idx = request.POST.get("idx", '')
        print("혼잡도 요청코드: " + idx)

        if idx == 'concon':
            curs = connection.cursor()
            query = """select * from fuzzbuzz_app1_congestion_points_sh where input_time = (select max(input_time) from fuzzbuzz_app1_congestion_points_sh);"""
            curs.execute(query)
            result = curs.fetchall()

            input_time = result[0][1]
            input_time = datetime.datetime.strftime(input_time, '%Y-%m-%d %H:%M')
            value      = result[0][2]

            print('input_time: ', input_time)
            print('value: ', value)
        
            return JsonResponse({'input_time' : '{}'.format(input_time), 'value' : '{}'.format(value)})
        else:
            return JsonResponse({'input_time' : 'error: 요청코드 불일치', 'value' : 'null'})
    else:
        return HttpResponse(status=400)