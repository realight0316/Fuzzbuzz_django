import json, requests

from fuzzbuzz_django.settings import BASE_DIR

# urltest = 'https://jsonplaceholder.typicode.com/todos/1'

# res = requests.request('GET', urltest, headers={}, data={})
# data = res.content

# print('\n' + str(res))
# print('응답 코드: ' + str(res.status_code))
# print('응답 데이터: ' + str(data) + '\n')

# data = json.loads(res.content)
# print(data); print('')

# ----------------------------------------------------------------------

url = 'http://13.124.135.112:8000/dl_data/'
d = {
    "name" : "배스킨라빈스",
    "phone" : "",
    "address" : "대구광역시"
}

res = requests.post(url, data=d)
print(d)

# -------------------

# url2 = 'http://3.38.116.21:8000/app_faq/' # Django server 재부팅시 IP 확인 필요
# d = {
#     "FAQID" : 1,
# }
# 보내려는 데이터를 'd'에 JSON 형식으로 작성

requests.post(url2, data=d)
print(d)
print("base: ", BASE_DIR)