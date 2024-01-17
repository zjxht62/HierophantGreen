import pytest
import requests
import jsonpath
import re
from commons.requests_util import RequestsUtil




class TestApi:
    # 类变量
    access_token = ''
    csrf_token = ''
    sess = requests.Session()

    # def setup_method(self):
    #     print('每个用例前执行')
    #
    # def teardown_method(self):
    #     print('每个用例后执行')
    #
    # def setup_class(self):
    #     print('每个类前执行')
    #
    # def teardown_class(self):
    #     print('每个类后执行')

    @pytest.mark.smoke
    # 获取access_token接口
    def test_get_token(self, base_url, conn):
        print(conn)
        urls = base_url + '/cgi-bin/token'
        datas = {'grant_type': 'client_credential',
                 'appid': 'wx8a9de038e93f77ab',
                 'secret': '8326fc915928dee3165720c910effb86'}
        # res = requests.get(url=urls, params=datas)
        # res = TestApi.sess.request('get', url=urls, params=datas)
        res = RequestsUtil().send_all_request(method='get', url=urls, params=datas)
        # lis = jsonpath.jsonpath(res.json(), '$.access_token')
        TestApi.access_token = res.json()['access_token']

    def test_select_flag(self):
        urls = 'https://api.weixin.qq.com/cgi-bin/tags/get'
        datas = {'access_token': TestApi.access_token}
        # res = requests.get(url=urls, params=datas)
        # res = TestApi.sess.request('get', url=urls, params=datas)
        res = RequestsUtil().send_all_request(method='get', url=urls, params=datas)

    # 编辑标签接口
    # 传入fixture手动执行
    @pytest.mark.user
    def test_edit_flag(self):
        urls = 'https://api.weixin.qq.com/cgi-bin/tags/update'
        params = {'access_token': TestApi.access_token}
        datas = {"tag": {"id": 134, 'name': '广东人'}}
        # res = requests.post(url=urls, json=datas, params=params)
        # res = TestApi.sess.request('post', url=urls, json=datas, params=params)
        res = RequestsUtil().send_all_request(method='post', url=urls, json=datas, params=params)

    def test_person_age(self,person_data):
        name = person_data["name"]
        age = person_data["age"]
        print(f'name:{name}, age:{age}')

        assert age > 20, f"{name}'s age is not greater than 20"

#     def test_file_upload(self):
#         urls = 'https://api.weixin.qq.com/cgi-bin/media/uploadimg'
#         params = {'access_token': TestApi.access_token}
#         datas = {'media': open(r"D:\aaa.jpg", 'rb')}
#         # res = requests.post(url=urls, files=datas, params=params)
#         # res = TestApi.sess.request('post', url=urls, files=datas, params=params)
#         res = RequestsUtil().send_all_request(method='post', url=urls, files=datas, params=params)
#
#
#     def test_phpwind(self):
#         urls = 'http://47.107.116.139/phpwind/'
#         # res = requests.get(url=urls)
#         res = TestApi.sess.request('get', url=urls)
#         res = RequestsUtil().send_all_request(method='get', url=urls)
#         # print(res.text)
#         TestApi.csrf_token = re.search('name="csrf_token" value="(.*?)"', res.text).group(1)
#
#     def test_login(self):
#         urls = 'http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun'
#         headers = {
#             'Accept': 'application/json, text/javascript, /; q=0.01',
#             'X-Requested-With': 'XMLHttpRequest'
#         }
#         datas = {
#             'username': 'baili',
#             'password': 'baili123',
#             'csrf_token': TestApi.csrf_token,
#             'backurl': 'http://47.107.116.139/phpwind/',
#             'invite': ''
#         }
#         # res = requests.post(url=urls, data=datas, headers=headers)
#         # res = TestApi.sess.request('post', url=urls, data=datas, headers=headers)
#         res = RequestsUtil().send_all_request(method='post', url=urls, data=datas, headers=headers)
#
#
# if __name__ == '__main__':
#     TestApi().test_get_token()
#     TestApi().test_select_flag()
#     TestApi().test_edit_flag()
#     TestApi().test_file_upload()
#     TestApi().test_phpwind()
#     TestApi().test_login()
