# -*- coding: utf-8 -*-
# PN: Selenium practice, Created Feb, 2017
# Version 1.0
# KW: crawler selenium tutorial
# Link: http://cuiqingcai.com/2599.html
# --------------------------------------------------- lib import
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
# --------------------------------------------------- part 1-1: quick start, open Chrome and search for ChromeDriver
# import time
# from selenium import webdriver

# driver = webdriver.Chrome()  # Setting default webbrowser (Optional argument, if not specified will search path.)
# driver.get('http://www.google.com/xhtml')	# navigate to the url page, 會等到js渲染完畢後才執行下一個動作
# time.sleep(5) # Let the user actually see something!
# search_box = driver.find_element_by_name('q')	# 
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5) # Let the user actually see something!
# driver.quit()
# --------------------------------------------------- part 1-2: more practice 
# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# class PythonOrgSearch(unittest.TestCase):

# 	def setUp(self):	# setUp 為初始化的方法，在每個測試中自動調用
# 		self.driver = webdriver.Chrome()

# 	def test_search_in_python_org(self):
# 		driver = self.driver
# 		driver.get("http://www.python.org")
# 		self.assertIn("Python", driver.title)
# 		elem = driver.find_element_by_name("q")
# 		elem.send_keys("pycon")
# 		elem.send_keys(Keys.RETURN)
# 		assert "No results found." not in driver.page_source

# 	def tearDown(self):	# tearDown 在每個測試方法結束後調用
# 		self.driver.close()	# close(): close tab / quit(): close browser

# if __name__ == "__main__":
# 	unittest.main()
# --------------------------------------------------- part 2: element control
# text = '''
# <input type="text" name="passwd" id="passwd-id" />
# '''

# # element searching(single element)
# element = driver.find_element_by_id("passed-id")
# element = driver.find_element_by_name("passwd")
# element = driver.find_element_by_tag_name("input")
# element = driver.find_element_by_xpath("//input[@id = 'passwd-id']")
# element = driver.find_element_by_css_selector("")
# .
# .
# .
# # element searching(multi elements)
# element = driver.find_elements_by_id("passed-id")
# element = driver.find_elements_by_name("passwd")
# element = driver.find_elements_by_tag_name("input")
# element = driver.find_elements_by_xpath("//input[@id = 'passwd-id']")
# element = driver.find_elements_by_css_selector("")
# .
# .
# .

# # element input
# element.send_keys("some text")
# element.send_keys("and some", Keys.ARROR_DOWN)	# 模擬點擊
# # element clear
# element.clear()
# --------------------------------------------------- part 3: list element control
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select

# driver = webdriver.Chrome()
# driver.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select')
# driver.maximize_window()	# 開啟全螢幕
# driver.switch_to_frame('iframeResult')
# Selector_Xpath = '/html/body/select'

# # The number of options in the selection
# Selector_Element = Select(driver.find_element_by_xpath(Selector_Xpath))
# print("The number of options in the selection = {}".format(str(len(Selector_Element.options))))

# # Select by Index = 2
# Selector_Element.select_by_index(2)
# print("Select by index (2) = {}".format(Selector_Element.first_selected_option.text))

# # Select by visible text = Audi
# Selector_Element.select_by_visible_text('Audi')
# print("Select by visible text Audi = {}".format(Selector_Element.first_selected_option.text))

# # select.select_by_value(value)
# driver.quit()
# --------------------------------------------------- part 4: submit
# driver.find_element_by_id("submit").click()
# or element.submit()
# --------------------------------------------------- part 5: drag and drop 左鍵拖曳
# element = driver.find_element_by_name("source")
# target = driver.find_element_by_name("target")

# from selenium.webdriver import ActionChains
# action_chains = ActionChains(driver)
# action_chains.drag_and_drop(element, target).perform()
# --------------------------------------------------- part 6: switch tabs, switch frame, switch alert
# driver.switch_to_window("windowName")
# for handle in driver.window_handles:
# 	driver.switch_to_window(handle)

# driver.switch_to_frame("frameName.0.child")

# alert = driver.switch_to_alert()
# --------------------------------------------------- part 7: forward, back
# driver.forward()
# driver.back()
# --------------------------------------------------- part 8: cookies
# driver.get('http://www.example.com')
# # 添加cookies
# cookie = {'name': 'foo', 'value': 'bar'}
# driver.add_cookie(cookie)
# # 取得網頁cookies
# drver.get_cookies()
# --------------------------------------------------- part 9-1: time setting (顯式等待，可設定條件)
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
# driver.get("http://somedomain/url_that_delays_loading")
# # solution 1
# try:
# 	elelment = WebDriverWait(driver, 10).until(
# 		EC.presence_of_element_located((By.ID, "myDynamicElement"))
# 		)
# finally:
# 	driver.quit()
# # solution 2
# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))
# --------------------------------------------------- part 9-2: time setting (隱式等待，單純設定等待時間)
# from selenium import webdriver

# driver = webdriver.Chrome()
# driver.implicity_wait(10)    # set timer with 10 sec
# driver.get("http://somedomain/url_that_delays_loading")
# myDynamicElement = driver.find_elements_by_id("myDynamicElement")