import requests

class RequestsUtil:

    sess = requests.Session()

    def send_all_request(self, **kwargs):
        res = RequestsUtil.sess.request(**kwargs)
        print(res.text)
        return res