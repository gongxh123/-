# from config.env_config import QA_BASS_URL
# # post无参数
# # post键值对参数
# import requests
#
# from tools import log_tool
import requests

from config.env_config import QA_BASS_URL
from tools import log_tool
from tools.random_tool import random_pwd
from tools.random_tools import random_string
s = {}
g = {}
g['producode'] = random_pwd()
g['prodName'] = "gongxh" + random_string('1234567890',4)
#  创建
def test_product_chuangjian(d):
    header = {"token": d["token"]}
    data = {
  "brand": "小米",
  "colors": [
    "黑色"
  ],
  "price": 10000,
  "productCode":g['producode'],
  "productName":g['prodName'],
  "sizes": [
    "5"
  ],
  "type": "全黑,全白"
}
    r = requests.request("POST", QA_BASS_URL + "/product/addProd", json=data,headers=header)  # data参数关键字可以把字典类型的数据转成键值对类型，再存入请求正文中
    log_tool.info('''-----------request-----------
    {} {}
    {}

    {}
    '''.format(r.request.method, r.request.url, r.request.headers, r.request.body))

    log_tool.info("""----------------response---------------
    {}
    {}

    {}
    """.format(r.status_code, r.headers, r.text))

    print(r.request.body)  # 获取请求正文的数据
    print(r.text)
    log_tool.info("实际结果：{}  \n  预期结果：{}".format(r.text, "2000"))
    try:
        assert "2000" in r.text
    except:
        log_tool.error("{} 断言失败,实际结果：{}  \n  预期结果：{}".format("test_lock_user", r.text, "2000"))
        raise
    s["skucode"] = r.json()["data"][0]["skuCode"]

#  查询产品
def test_product_chaxun(d):
    header = {"token": d["token"]}
    para = {'prodCode':g['producode']}
    r = requests.request("GET", QA_BASS_URL + "/product/getSkuByProdCode", params=para,headers=header)  # data参数关键字可以把字典类型的数据转成键值对类型，再存入请求正文中
    log_tool.info('''-----------request-----------
    {} {}
    {}

    {}
    '''.format(r.request.method, r.request.url, r.request.headers, r.request.body))

    log_tool.info("""----------------response---------------
    {}
    {}

    {}
    """.format(r.status_code, r.headers, r.text))

    print(r.request.body)  # 获取请求正文的数据
    print(r.text)
    log_tool.info("实际结果：{}  \n  预期结果：{}".format(r.text, "2000"))
    try:
        assert "2000" in r.text
    except:
        log_tool.error("{} 断言失败,实际结果：{}  \n  预期结果：{}".format("test_lock_user", r.text, "2000"))
        raise


#  修改产品价格
def test_product_xiugaichanpin(d):
    header = {"token": d["token"]}
    para = {'prodCode':g['producode'],'price':1000}
    r = requests.request("POST", QA_BASS_URL + "/product/changePriceByProdCode", params=para,headers=header)  # data参数关键字可以把字典类型的数据转成键值对类型，再存入请求正文中
    log_tool.info('''-----------request-----------
    {} {}
    {}

    {}
    '''.format(r.request.method, r.request.url, r.request.headers, r.request.body))

    log_tool.info("""----------------response---------------
    {}
    {}

    {}
    """.format(r.status_code, r.headers, r.text))

    print(r.request.body)  # 获取请求正文的数据
    print(r.text)
    log_tool.info("实际结果：{}  \n  预期结果：{}".format(r.text, "2000"))
    try:
        assert "2000" in r.text
    except:
        log_tool.error("{} 断言失败,实际结果：{}  \n  预期结果：{}".format("test_lock_user", r.text, "2000"))
        raise

#  查询产品
def test_product_chaxun2(d):
    header = {"token": d["token"]}
    para = {'prodCode':g['producode']}
    r = requests.request("GET", QA_BASS_URL + "/product/getSkuByProdCode", params=para,headers=header)  # data参数关键字可以把字典类型的数据转成键值对类型，再存入请求正文中
    log_tool.info('''-----------request-----------
    {} {}
    {}

    {}
    '''.format(r.request.method, r.request.url, r.request.headers, r.request.body))

    log_tool.info("""----------------response---------------
    {}
    {}

    {}
    """.format(r.status_code, r.headers, r.text))

    print(r.request.body)  # 获取请求正文的数据
    print(r.text)
    log_tool.info("实际结果：{}  \n  预期结果：{}".format(r.text, "2000"))
    try:
        assert "2000" in r.text
    except:
        log_tool.error("{} 断言失败,实际结果：{}  \n  预期结果：{}".format("test_lock_user", r.text, "2000"))
        raise

#  修改商品价格
def test_product_xiugaishangping(d):
    header = {"token":d["token"]}
    para = {"SKU":s["skucode"],'price':200}
    r = requests.request("POST", QA_BASS_URL + "/product/changePrice", params=para,headers=header)  # data参数关键字可以把字典类型的数据转成键值对类型，再存入请求正文中
    log_tool.info('''-----------request-----------
    {} {}
    {}

    {}
    '''.format(r.request.method, r.request.url, r.request.headers, r.request.body))

    log_tool.info("""----------------response---------------
    {}
    {}

    {}
    """.format(r.status_code, r.headers, r.text))

    print(r.request.body)  # 获取请求正文的数据
    print(r.text)
    log_tool.info("实际结果：{}  \n  预期结果：{}".format(r.text, "2000"))
    try:
        assert "2000" in r.text
    except:
        log_tool.error("{} 断言失败,实际结果：{}  \n  预期结果：{}".format("test_lock_user", r.text, "2000"))
        raise

#  产品下架
def test_product_xiajia(d):
    header = {"token":d["token"]}
    para = {"productCode":g['producode']}
    r = requests.request("POST", QA_BASS_URL + "/product/soldOut", params=para,headers=header)  # data参数关键字可以把字典类型的数据转成键值对类型，再存入请求正文中
    log_tool.info('''-----------request-----------
    {} {}
    {}

    {}
    '''.format(r.request.method, r.request.url, r.request.headers, r.request.body))

    log_tool.info("""----------------response---------------
    {}
    {}

    {}
    """.format(r.status_code, r.headers, r.text))

    print(r.request.body)  # 获取请求正文的数据
    print(r.text)
    log_tool.info("实际结果：{}  \n  预期结果：{}".format(r.text, "2000"))
    try:
        assert "2000" in r.text
    except:
        log_tool.error("{} 断言失败,实际结果：{}  \n  预期结果：{}".format("test_lock_user", r.text, "2000"))
        raise

#  产品预售
def test_product_yushou(d):
    header = {"token":d["token"]}
    para = {"productCode":g['producode']}
    r = requests.request("POST", QA_BASS_URL + "/product/toPreSale", params=para,headers=header)  # data参数关键字可以把字典类型的数据转成键值对类型，再存入请求正文中
    log_tool.info('''-----------request-----------
    {} {}
    {}

    {}
    '''.format(r.request.method, r.request.url, r.request.headers, r.request.body))

    log_tool.info("""----------------response---------------
    {}
    {}

    {}
    """.format(r.status_code, r.headers, r.text))

    print(r.request.body)  # 获取请求正文的数据
    print(r.text)
    log_tool.info("实际结果：{}  \n  预期结果：{}".format(r.text, "2000"))
    try:
        assert "2000" in r.text
    except:
        log_tool.error("{} 断言失败,实际结果：{}  \n  预期结果：{}".format("test_lock_user", r.text, "2000"))
        raise