
# 登录
import requests

api_url = 'http://192.168.1.151:8084'
a = 1
def test_login():
    data = {
      "pwd": "qq1234",
      "userName": "KDS123"
    }
    r = requests.post(f"{api_url}/login", json=data)
    global a
    a = r.json()["data"]["token"]
# test_login()
def test_lock1():
    data = {"userName": "xuchao11"}
    header = {"token": f"{a}"}
    r = requests.post(f"{api_url}/user/lock", data=data, headers=header)
    assert "该用户已被冻结" in r.text
    print(r.text)

#  登录正常流
# def test_post_form_data():
#  data =  {
#    "pwd": "qq123456",
#    "userName": "sku888999"
#   }
#  r = requests.request("POST","http://192.168.1.151:8084/login",json=data)
#  print(r.text)
#  print(r.request.body)
#  assert "2000" in r.text

#  冻结正常流
# def test_post_dongjie():
#   hearder = {'token':'eyJ0aW1lT3V0IjoxNTk0Mjg3ODg3MDc0LCJ1c2VySWQiOjI0MzkxLCJ1c2VyTmFtZSI6InNrdTg4ODk5OSJ9'}
#   data = {'userName':'sku888999'}
#   r = requests.request("POST","http://192.168.1.151:8084/user/lock",data=data,headers = hearder)
#   # print(r.text)
#   assert "该用户已被冻结" in r.text

#  冻结异常流-1
# def test_post_dongjie():
#   hearder = {'token':'eyJ0aW1lT3V0IjoxNTk0Mjg3ODg3MDc0LCJ1c2VySWQiOjI0MzkxLCJ1c2VyTmFtZSI6InNrdTg4ODk5OSJ9'}
#   data = {'userName':'sku8889999'}
#   r = requests.request("POST","http://192.168.1.151:8084/user/lock",data=data,headers = hearder)
#   print(r.text)
#   assert "该用户不存在" in r.text

#  冻结异常流-为空
# def test_post_dongjie():
#   hearder = {'token':'eyJ0aW1lT3V0IjoxNTk0Mjg3ODg3MDc0LCJ1c2VySWQiOjI0MzkxLCJ1c2VyTmFtZSI6InNrdTg4ODk5OSJ9'}
#   data = {'userName':''}
#   r = requests.request("POST","http://192.168.1.151:8084/user/lock",data=data,headers = hearder)
  # print(r.text)
  # assert "该用户不存在" in r.text


#  解冻正常流
# def test_post_jiedong():
#   hearder = {'token':'eyJ0aW1lT3V0IjoxNTk0Mjg3ODg3MDc0LCJ1c2VySWQiOjI0MzkxLCJ1c2VyTmFtZSI6InNrdTg4ODk5OSJ9'}
#   data = {'userName':'sku888999'}
#   r = requests.request("POST","http://192.168.1.151:8084/user/unLock",data=data,headers = hearder)
#   # print(r.text)
#   assert "该用户已经解冻" in r.text

#  解冻异常流-1
# def test_post_jiedong():
#   hearder = {'token':'eyJ0aW1lT3V0IjoxNTk0Mjg3ODg3MDc0LCJ1c2VySWQiOjI0MzkxLCJ1c2VyTmFtZSI6InNrdTg4ODk5OSJ9'}
#   data = {'userName':'sku88899'}
#   r = requests.request("POST","http://192.168.1.151:8084/user/unLock",data=data,headers = hearder)
#   print(r.text)
#   assert "该用户不存在" in r.text

#  解冻异常流-为空
# def test_post_jiedong():
#   hearder = {'token':'eyJ0aW1lT3V0IjoxNTk0Mjg3ODg3MDc0LCJ1c2VySWQiOjI0MzkxLCJ1c2VyTmFtZSI6InNrdTg4ODk5OSJ9'}
#   data = {'userName':'sku88899'}
#   r = requests.request("POST","http://192.168.1.151:8084/user/unLock",data=data,headers = hearder)
#   print(r.text)
#   assert "该用户不存在" in r.text

if __name__ == '__main__':
    test_login()