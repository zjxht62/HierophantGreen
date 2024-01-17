import requests
import jsonpath
import re
from commons.requests_util import RequestsUtil
from testcases.test_api import TestApi


class TestApi2:

    def test_file_upload(self):
        urls = 'https://api.weixin.qq.com/cgi-bin/media/uploadimg'
        params = {'access_token': TestApi.access_token}
        datas = {'media': open(r"D:\aaa.jpg", 'rb')}
        # res = requests.post(url=urls, files=datas, params=params)
        # res = TestApi.sess.request('post', url=urls, files=datas, params=params)
        res = RequestsUtil().send_all_request(method='post', url=urls, files=datas, params=params)
