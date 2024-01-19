import requests
import jsonpath
import re
from commons.requests_util import RequestsUtil
from commons.yaml_util import read_yaml


class TestApi2:
    pass
    # def test_file_upload(self):
    #     # print('TestApi2里面的测试用例')
    #     urls = 'https://api.weixin.qq.com/cgi-bin/media/uploadimg'
    #     params = {'access_token': read_yaml('access_token')}
    #     datas = {'media': open(r"D:\aaa.jpg", 'rb')}
    #     # res = requests.post(url=urls, files=datas, params=params)
    #     # res = TestApi.sess.request('post', url=urls, files=datas, params=params)
    #     res = RequestsUtil().send_all_request(method='post', url=urls, files=datas, params=params)
