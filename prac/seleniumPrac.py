# -*- coding: utf-8 -*-
# PN: Selenium practice, Created Feb, 2017
# Version 1.0
# KW: crawler selenium tutorial
# Link: http://cuiqingcai.com/2599.html
# --------------------------------------------------- lib import
# from selenium import webdriver
# --------------------------------------------------- part 1: quick start
import time
from selenium import webdriver

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()