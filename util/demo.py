from selenium import webdriver


driver  = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element().send_keys()
driver.page_source