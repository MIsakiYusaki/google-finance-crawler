# MoneyDJ人氣指數爬蟲		2016/12/22
# encoding: utf-8

import urllib, urllib2
url = 'http://www.moneydj.com/InfoSvc/apis/vc'

request = urllib2.Request(url)
request.add_header('Content-Type', 'application/json')

payload = '{"counts":[{"svc":"NV","guid":"a180a15b-9e4f-4575-b28f-927fcb5c63a3"}]}'
response = urllib2.urllib2.urlopen(request.data = payload)
html = response.read()
print html