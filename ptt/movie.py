# -*- coding: utf-8 -*-
# PN: Crawler - ptt_movie, Created Mar. 2017
# Version 1.2 (push_count, output prettify)
# KW: 
# Link: 
# https://github.com/leVirve/CrawlerTutorial
# --------------------------------------------------- lib import
import time

import requests
import urllib.parse
from bs4 import BeautifulSoup
from multiprocessing import Pool

from utlis import pretty_print
# --------------------------------------------------- Crawler start
# --------------------------------------------------- 1. Initial process
def get_posts_list(url):
    time.sleep(0.5)  # 每次爬取前暫停 0.5 秒以免被 PTT 網站判定為大量惡意爬取

    res = requests.get(
        url = url,
        cookies = {'over18': '1'}   # 部分看板會驗證是否已成年，傳送成年訊息給 cookies
        )
    if res.status_code != 200:
        print('Invalid url:', res.url)
        return None
    else:
        soup = BeautifulSoup(res.text, 'lxml')

    posts = list()
    for article in soup.find_all('div', 'r-ent'):
        # 取得推文數
        push_count = 0
        if article.find('div', 'nrec').string:
            # 處理 push_count 可能為0的情形
            try:
                push_count = int(article.find('div', 'nrec').string)  # 轉換字串為數字
            except ValueError:  # 若轉換失敗，不做任何事，push_count 保持為 0
                pass
            try:
                meta = article.find('div', 'title').find('a')
                posts.append({
                    'title': meta.get_text().strip(),
                    'link': meta.get('href'),
        			'push': push_count,
        			'date': article.find('div', 'date').getText(),
        			'author': article.find('div', 'author').getText(),
        			})
            except AttributeError:
                print('本文已被刪除')
    # 抓取下一頁的網址
    next_link = soup.find('div', 'btn-group-paging').find_all('a', 'btn')[1].get('href')

    return posts, next_link
# --------------------------------------------------- 2. Next page
def get_paged_meta(page):
    page_url = INDEX
    all_posts = list()
    for i in range(page):
        posts, link = get_posts_list(page_url)
        all_posts += posts
        page_url = urllib.parse.urljoin(INDEX, link)
    return all_posts
# --------------------------------------------------- Multi-crawling in-article content (用來計算文章內有多少字)
def get_articles(metadata):
	post_links = [meta['link'] for meta in metadata]
	with Pool(processes = 8) as pool:
		contents = pool.map(fetch_article_content, post_links)
		return contents
def fetch_article_content(link):
    url = urllib.parse.urljoin(INDEX, link)
    res = requests.get(url)
    return res.text
# --------------------------------------------------- Function calling
if __name__ == '__main__':
    INDEX = 'https://www.ptt.cc/bbs/movie/index.html'
    pages = 1

    start = time.time()

    metadata = get_paged_meta(pages)
    articles = get_articles(metadata)


    for post in metadata:
        print('----------------------------------------------------------------')
        print('獲得{3: >2}個讚 日期:{0} 作者:{1: <15} {2}'.format(post['date'], post['author'], post['title'], post['push']))
        print('連結: https://www.ptt.cc{0}'.format(post['link']))
    print('----------------------------------------------------------------')  
    print('花費: %f 秒' % (time.time() - start))  
    print('共{}項結果'.format(len(articles)))
