# -*- coding: utf-8 -*-
# PN: Requests practice, Created Feb, 2017
# Version 1.0
# KW: http://cuiqingcai.com/2556.html crawler requests tutorial
# --------------------------------------------------- lib import
import requests
# --------------------------------------------------- part 1: status code
# res = requests.get('http://cuiqingcai.com')
# print(type(res))    # 回傳get的類型
# print(res.status_code)    # 回傳get的狀態碼(Success or fail)
# print(res.encoding)    # 回傳get到的網站編碼方式
# print(res.text)    # 回傳get的網站文字內容
# print(res.cookies)    # 回傳get到的網站cookies
# --------------------------------------------------- part 2: request catogeries
# res = requests.post('http://httpbin.org/post')
# res = requests.put('http://httpbin.org/put')
# res = requests.delete('http://httpbin.org/delete')
# res = requests.head('http://httpbin.org/get')
# res = requests.options('http://httpbin.org/get')
# --------------------------------------------------- part 3-1: get with params
# payload = {'key1': 'value1', 'key2': 'value2'}
# res = requests.get('http://cuiqingcai.com', params=payload)
# print(res.url)
# --------------------------------------------------- part 3-2: get with params and headers
# payload = {'key1': 'value1', 'key2': 'value2'}
# headers = {'content-type': 'application/json'}
# res = requests.get('http://httpbin.org/get', params=payload, headers=headers)
# print(res.url)
# --------------------------------------------------- part 4-1: post pass with form(傳送表單式)
# payload = {'key1': 'value1', 'key2': 'value2'}
# res = requests.post('http://httpbin.org/post', data=payload)
# print(res.text)
# --------------------------------------------------- part 4-2: post pass with json(傳送json)
# import json

# url = 'http://httpbin.org/post'
# payload = {'some':'data'}
# res = requests.post(url, data=json.dumps(payload))
# print(res.text)
# --------------------------------------------------- part 4-3: post pass with file(傳送file, 文件上傳)
# url = 'http://httpbin.org/post'
# files = {'file': open('test.txt', 'rb')}
# res = requests.post(url, files=files)
# print(res.text)
# --------------------------------------------------- part 5-1: get cookies
# url = 'http://example.com'
# res = requests.get(url)
# print(res.cookies)
# --------------------------------------------------- part 5-2: pass cookies
# url = 'http://httpbin.org/cookies'
# cookies = dict(cookies_are='working')
# res = requests.get(url, cookies=cookies)
# print(res.text)
# --------------------------------------------------- part 6: timeout setting
# request.get('http://github.com', timeout=0.001)    # only affect to connect process, not download process
# --------------------------------------------------- part 7: short-term requests and long-term session
# requests.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
# res = requests.get('http://httpbin.org/cookies')
# print(res.text)

# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
# res = s.get('http://httpbin.org/cookies')
# print(res.text)
# --------------------------------------------------- part 7-1: use session to pass, delete
# print('Pass x-test1, x-test2 through Session')
# s = requests.Session()
# s.headers.update({'x-test': 'true'})
# res = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
# print(res.text)

# print('Delete x-test2 with None value')
# res = s.get('http://httpbin.org/headers', headers={'x-test2': None})
# print(res.text)
# --------------------------------------------------- part 8: SSL verify
# res = requests.get('https://kyfw.12306.cn/otn/', verify=True)    # failed example, need change True to False to sent requests
# print(res.text)
# res = requests.get('http://github.com', verify=True)    # Successed example
# print(res.text)
# --------------------------------------------------- part 9: Proxy
# proxies = {
# 	'http': 'http://41.118.132.69:4433'
# }
# res = requests.post('http://httpbin.org/post', proxies=proxies)
# print(res.text)












