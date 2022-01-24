import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
from selenium.webdriver.support.ui import Select

s = Service('C:/Program Files/py/PyCharm 2021.3/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://www.phptravels.net/login")
driver.maximize_window()
driver.find_element(By.ID, "languages").click()
time.sleep(10)
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Spanish']"))).click()
driver.get_screenshot_as_file("spanish.png")

time.sleep(10)






