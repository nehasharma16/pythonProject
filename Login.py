import time

import selenium
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service




class Test_Login(unittest.TestCase):
    def logintest(self):
        s = Service('C:/Program Files/py/PyCharm 2021.3/chromedriver.exe')
        driver = webdriver.Chrome(service=s)
        driver.find_element(By.XPATH, "//a[@id='logout']").click()
        time.sleep(10)
        driver.find_element(By.ID, "Email").send_keys("nehatest16@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("Testme@123")
        driver.find_element(By.XPATH, "//label[@for='RememberMe']").click()
        time.sleep(10)
        driver.find_element(By.XPATH, "//button[@id='Login_Btn']").click()

if __name__ == '__main__':
    unittest.main()