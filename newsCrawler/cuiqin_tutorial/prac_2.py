# 高鐵網站爬蟲	2016/12/22
# encoding: utf-8

import urllib, urllib2
# setting scrape url
url = "http://www.thsrc.com.tw/tw/TimeTable/SearchResult"

# request
request = urllib2.Request(url)
# 偽裝成瀏覽器，繞過網站對爬蟲程式的檢查，這個值可以從Chrome開發人員工具中Network看到的User-Agent直接複製
request.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36")

form_data = {
	"StartStation": "977abb69-413a-4ccf-a109-0272c24fd490", 
    "EndStation": "f2519629-5973-4d08-913b-479cce78a356",
    "SearchDate": "2016/12/22",
    "SearchTime": "15:00",
    "SearchWay":"DepartureInMandarin",
    "RestTime":"",
    "EarlyOrLater":""
}

# encode datas, then store in html
form_data = urllib.urlencode(form_data)
response = urllib2.urlopen(request, data = form_data)
html = response.read()

# create new file to store the information and them close it
file_out = file('prac_2.html', 'w')
file_out.write(html)
file_out.close()

print "Scrape finished"