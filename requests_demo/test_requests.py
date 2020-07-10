import requests

# 发送请求
# get请求无参数
# r = requests.request('get','http://mall.yansl.com:8080/prefrenceArea/listAll')
# print(r.text)  # 获取响应数据

# get请求qurey参数
# params关键字会把字典类型的数据转为键值对类型，然后在放入url最后面再用?分隔,在响应行中
# para = {'accountName':'gxhhs'}
# r = requests.request('get','http://192.168.1.151:8084/acc/getAccInfo',params = para)
# r = requests.request('get','http://192.168.1.151:8084/acc/getBills',params = para)
# print(r.request.url)  # 获取请求url
# print(r.text)  # 获取响应数据

# get path类型参数
# r = requests.request('get','http://192.168.1.151:8084/acc/getAllAccs/{pageNum}/{pageSize}'.format(pageNum=1,pageSize=3))
# print(r.request.url)  # 获取请求url
# print(r.text)  # 获取响应数据




