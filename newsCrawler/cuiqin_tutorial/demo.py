
# encoding: utf-8
import urllib, urllib2

request = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(request)

print response.read()	#read() 可以返回獲取到的網頁內容

# Request 可分為兩種方法 POST (傳送封包參數) / GET (鏈結)

"""POST 方式的寫法"""
values = {"username": "1016903103@qq.com", "password": "XXXX"}
data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)
print response.read()

# 加入user_agent的寫法，寫入請求身分，避免服務器不反應
# 对付”反盗链”的方式
# 服务器会识别headers中的referer是不是它自己，如果不是，有的服务器不会响应
# 所以我们还可以在headers中加入referer
url = 'http://www.server.com/login'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  
values = {'username' : 'cqc',  'password' : 'XXXX' }  
headers = { 'User-Agent' : user_agent, 'Referer':'http://www.zhihu.com/articles' }  
data = urllib.urlencode(values)  
request = urllib2.Request(url, data, headers)  
response = urllib2.urlopen(request)  
page = response.read() 

"""GET 方式的寫法，修改傳送的url"""
values = {}
values['username'] = '1016903103@qq.com'
values['password'] = 'XXXX'
data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login"
geturl = url + "?" + data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()

# 編碼後的url，也就是在網址會輸入的鏈結
print geturl

# Proxy(代理)的設置，有些網站會檢測某段時間內某個IP的訪問次數，避免因訪問過多遭禁止訪問
import urllib2
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http": "http://some-proxy.com:8080"})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
	opener = urllib2.build_opener(proxy_handler)
else:
	opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)

# Timeout 的設置，設置等待多久超時
import urllib2
response = urllib2.urlopen('http://www.baidu.com', timeout = 10)
response = urllib2.urlopen('http"//www.baidu.com', data, 10)

# PUT, DELETE方法
import urllib2
request = urllib2.Request(url, data = data)
request.get_method = lambda: 'PUT' # or 'DELETE'
response = urllib2.urlopen(request)

# 打開 DebugLog，收發包的內容會在屏幕上print out

import urllib2
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.baidu.com')