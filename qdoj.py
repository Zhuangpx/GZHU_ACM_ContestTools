'''
Autor: violet apricity ( Zhuangpx )
Date: 2023-03-26 01:05:04
LastEditors: violet apricity ( Zhuangpx )
LastEditTime: 2023-04-18 18:50:32
FilePath: \GZHU_ACM_ContestTools\qdoj.py
Description:  Zhuangpx : Violet && Apricity:/ The warmth of the sun in the winter /
'''

import requests
import json
# 管理员账号密码
username = 'root_usename'
password = 'root_password'
# 请求头
HEADERS = {
    'user-agent':
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'
}
COOKIES = {}
# URL和api
URL = 'http://172.22.72.199/'
PROFILE = URL + 'api/profile'
LOGIN_URL = URL + 'api/login'
CONTEST_SUBMISSIONS_URL = URL + 'api/contest_submissions'


def init():
    '''
    get csrftoken
    '''
    global COOKIES
    res = requests.get(PROFILE)
    COOKIES = res.cookies
    HEADERS['X-CSRFToken'] = res.cookies['csrftoken']


def login(username, password):
    global COOKIES
    res = requests.post(LOGIN_URL,
                        headers=HEADERS,
                        cookies=COOKIES,
                        json={
                            'username': username,
                            'password': password
                        })
    assert res.status_code == 200
    COOKIES = res.cookies


def getStatus(cid, page, name, pid, result):
    '''
    get first page results
    limit: max number of results
    '''
    limit = 50
    res = requests.get(CONTEST_SUBMISSIONS_URL,
                       cookies=COOKIES,
                       params={
                           'contest_id': str(cid),
                           'limit': str(limit),
                           'offset': str((page - 1) * limit),
                           'result': str(0)
                       })
    assert res.status_code == 200
    results = json.loads(res.text)
    # print(results)
    return list(
        map(
            lambda result: {
                'userName': result['username'],
                'problemID': result['problem'],
                # 'result': result['result']
            },
            results['data']['results'])), results['data']['total']


init()
login(username, password)
if __name__ == '__main__':
    res = getStatus(1, 1, '', '', 0)
    #print(res)
