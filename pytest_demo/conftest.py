import pytest
#
# from tools.random_tool import random_pwd
# from tools.random_tools import random_string
#
#
# @pytest.fixture(scope='module')
# def d():
#     g = {}
#     g['pwd'] = random_pwd()
#     g['userName'] = "gongxh" + random_string('1234567890',4)
#     return g
import requests

from config.env_config import QA_BASS_URL


@pytest.fixture(scope='module')
def d():
    data = {"pwd": "zBvCRV00", "userName": "gongxh0857"}
    r = requests.request("POST", QA_BASS_URL + "/login", json=data)
    print(r.text)
    return {"token":r.json()["data"]["token"]}