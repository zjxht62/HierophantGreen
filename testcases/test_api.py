import pytest
import requests
import jsonpath
import re
from commons.requests_util import RequestsUtil
from commons.yaml_util import write_yaml, read_yaml, read_yaml_testcase


class TestApi:
    # # 类变量
    # access_token = ''
    # csrf_token = ''
    # sess = requests.Session()

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
    @pytest.mark.parametrize('caseinfo', read_yaml_testcase('testcases/test_get_token.yaml'))
    # 获取access_token接口
    def test_get_token(self, base_url, caseinfo):
        urls = caseinfo['request']['url']
        datas = caseinfo['request']['params']
        method = caseinfo['request']['method']
        # res = requests.get(url=urls, params=datas)
        # res = TestApi.sess.request('get', url=urls, params=datas)
        res = RequestsUtil().send_all_request(method=method, url=urls, params=datas)
        # lis = jsonpath.jsonpath(res.json(), '$.access_token')
        # TestApi.access_token = res.json()['access_token']
        if 'access_token' in dict(res.json()).keys():
            # 保存到yaml
            write_yaml({'access_token': res.json()['access_token']})

    # 编辑标签接口
    # 传入fixture手动执行
    @pytest.mark.user
    @pytest.mark.parametrize('caseinfo', read_yaml_testcase('testcases/test_edit_flag.yaml'))
    def test_edit_flag(self, caseinfo):
        method = caseinfo['request']['method']
        urls = caseinfo['request']['url']
        params = caseinfo['request']['params']
        params['access_token'] = read_yaml('access_token')
        json = caseinfo['request']['json']
        # res = requests.post(url=urls, json=datas, params=params)
        # res = TestApi.sess.request('post', url=urls, json=datas, params=params)
        res = RequestsUtil().send_all_request(method=method, url=urls, json=json, params=params)


    @pytest.mark.parametrize('caseinfo', read_yaml_testcase('testcases/test_select_flag.yaml'))
    def test_select_flag(self, caseinfo):
        method = caseinfo['request']['method']
        urls = caseinfo['request']['url']
        datas = caseinfo['request']['params']
        datas['access_token'] = read_yaml('access_token')
        # res = requests.get(url=urls, params=datas)
        # res = TestApi.sess.request('get', url=urls, params=datas)
        res = RequestsUtil().send_all_request(method=method, url=urls, params=datas)


    # def test_person_age(self, person_data):
    #     name = person_data["name"]
    #     age = person_data["age"]
    #     print(f'name:{name}, age:{age}')
    #
    #     assert age > 20, f"{name}'s age is not greater than 20"

    @pytest.mark.parametrize('caseinfo', read_yaml_testcase('testcases/test_file_upload.yaml'))
    def test_file_upload(self,caseinfo):
        method = caseinfo['request']['method']
        urls = caseinfo['request']['url']
        params = caseinfo['request']['params']
        params['access_token'] = read_yaml('access_token')
        files = caseinfo['request']['files']
        for k, v in files.items():
            files[k] = open(v,'rb')
        RequestsUtil().send_all_request(method=method, url=urls, params=params, files=files)



    # def test_phpwind(self):
    #     urls = 'http://47.107.116.139/phpwind/'
    #     # res = requests.get(url=urls)
    #     # res = TestApi.sess.request('get', url=urls)
    #     res = RequestsUtil().send_all_request(method='get', url=urls)
    #     # print(res.text)
    #     write_yaml({'csrf_token': re.search('name="csrf_token" value="(.*?)"', res.text).group(1)})
    #
    # def test_login(self):
    #     urls = 'http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun'
    #     headers = {
    #         'Accept': 'application/json, text/javascript, /; q=0.01',
    #         'X-Requested-With': 'XMLHttpRequest'
    #     }
    #     datas = {
    #         'username': 'baili',
    #         'password': 'baili123',
    #         'csrf_token': read_yaml('csrf_token'),
    #         'backurl': 'http://47.107.116.139/phpwind/',
    #         'invite': ''
    #     }
    #     # res = requests.post(url=urls, data=datas, headers=headers)
    #     # res = TestApi.sess.request('post', url=urls, data=datas, headers=headers)
    #     res = RequestsUtil().send_all_request(method='post', url=urls, data=datas, headers=headers)


if __name__ == '__main__':
    TestApi().test_get_token()
    TestApi().test_select_flag()
    TestApi().test_edit_flag()
    TestApi().test_file_upload()
    TestApi().test_phpwind()
    TestApi().test_login()
