import requests

header = {'token':'eyJ0aW1lT3V0IjoxNTk0MjYyOTExNTc3LCJ1c2VySWQiOjkxLCJ1c2VyTmFtZSI6Inpob25neng4OSJ9'}
r = requests.request('get','http://192.168.1.151:8084/cst/getAll/{pageNum}/{pageSize}'.format(pageNum=1,pageSize=3),headers = header)
print(r.request.url)  # 获取请求url
print(r.text)  # 获取响应数据
print(r.request.headers)  # 获取请求头信息


