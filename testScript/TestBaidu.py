#-*- coding: utf-8 -*-
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestBaidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.baseUrl = "https://www.baidu.com"

    def tearDown(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.get(self.baseUrl)
        searchBox = self.driver.find_element(by = By.ID, value = "kw")
        searchBox.clear()
        searchBox.send_keys('haha')
        time.sleep(2)
        searchButton = self.driver.find_element(by = By.ID ,value='su')
        searchButton.click()
        self.driver.implicitly_wait(10)
        firstPageLink = self.driver.find_element(by = By.LINK_TEXT,value="百度首页")
        firstPageLink.click()
        time.sleep(3)





if __name__ == "__main__":
    unittest.main()