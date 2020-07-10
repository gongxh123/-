import requests

# post无参数
# r = requests.request('post','http://mall.yansl.com:8080/aliyun/oss/callback')
# print(r.text)  # 获取响应数据

# post键值对参数
# header = {'token':'eyJ0aW1lT3V0IjoxNTk0MjYyOTExNTc3LCJ1c2VySWQiOjkxLCJ1c2VyTmFtZSI6Inpob25neng4OSJ9'}
# data = {'userName':'gxhhs'}
# r = requests.request('post','http://192.168.1.151:8084/user/lock',data = data,headers = header)
# print(r.request.url)  # 获取请求url
# print(r.text)  # 获取响应数据
# print(r.request.body) # 获取请求正文

# post json类型参数
# data = {
#     "accountName": "gxhhs",
#     "changeMoney": 100000
# }
# r = requests.request('post','http://192.168.1.151:8084/acc/charge',json = data)
# print(r.request.headers)
# print(r.request.body)
# print(r.text)


# header = {'token':'eyJ0aW1lT3V0IjoxNTk0MjYyOTExNTc3LCJ1c2VySWQiOjkxLCJ1c2VyTmFtZSI6Inpob25neng4OSJ9'}
# data = {
#   "newPwd": "a123456",
#   "oldPwd": "g123456",
#   "reNewPwd": "a123465",
#   "userName": "gxhhs"
# }
# r = requests.request('post','http://192.168.1.151:8084/user/changepwd',headers = header,json = data)
# print(r.request.url)  # 获取请求url
# print(r.request.headers)
# print(r.request.body)  # 获取请求头信息
# print(r.text)  # 获取响应数据


# data = {
#     "ccountName": "gxhhs",
#     "changeMoney": 100000
# }
# header = {'Content-Type': 'application/json'}
# import json
# r = requests.request('post','http://192.168.1.151:8084/acc/charge',data = json.dumps(data),headers = header)
# print(r.request.headers)
# print(r.request.body)
# print(r.request.url)
# print(r.text)

# 下载文件
# header = {'token':'eyJ0aW1lT3V0IjoxNTk0Mjc2NjM4MzcxLCJ1c2VySWQiOjI0MTY2LCJ1c2VyTmFtZSI6IkZrSlI3UiJ9'}
# r = requests.request('get','http://192.168.1.151:8084/product/downRepertoryTemplate',headers = header)
# print(r.content)
# with open('aaa.xls','wb') as f:
#     f.write(r.content)
#
# # f = open('aaa.xls','rb')
# # print(f.read())
#
# f = open('aaa.xls','rb')
# file = {'file': f}
# header = {'token':'eyJ0aW1lT3V0IjoxNTk0Mjc2NjM4MzcxLCJ1c2VySWQiOjI0MTY2LCJ1c2VyTmFtZSI6IkZrSlI3UiJ9'}
# r = requests.request('post','http://192.168.1.151:8084/product/uploaProdRepertory',headers = header,files = file)
# f.close()
# print(r.text)


