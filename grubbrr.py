import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import asserts
s = Service('C:/Program Files/py/PyCharm 2021.3/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://order.grubbrr.com/Home/Menu/Ns-QA-Test-branch")
driver.maximize_window()
time.sleep(5)
# driver.find_element(By.ID, "79477").click()
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(driver.find_element(By.XPATH, "(//a[@id='79477'])[1]"))).click()
time.sleep(10)
driver.find_element(By.XPATH, "(//img[contains(@alt,'close')])[2]").click()
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(driver.find_element(By.XPATH, "(//a[@id='79477'])[1]"))).click()

WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable(driver.find_element(By.CSS_SELECTOR, "#SingleItemOrder"))).click()
print(driver.title)
a = driver.title
expected1 = "Online Ordering - Grubbrr"
assert a == expected1
print("Test case Pass-Going good")
time.sleep(2)
driver.find_element(By.XPATH, "(//img[@alt='coke'])[1]").click()
time.sleep(2)
driver.find_element(By.XPATH, "(//button[@class='qtyInc btn btn-default btn-inc'])[1]").click()
driver.find_element(By.XPATH, "//button[@id='SingleItemOrder']").click()
time.sleep(1)
driver.find_element(By.XPATH, "(//span[@id='spanText'])[1]").click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    driver.find_element(By.XPATH, "//button[@id='Layout_Continue_as_Guest_CheckLoginModel']"))).click()
time.sleep(2)
driver.find_element(By.XPATH, "//label[@for='pickup']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//label[@for='pickupLater']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='pickupTime']").click()
for i in range(5):
    driver.find_element(By.XPATH, "(//div[@class='prev action-next'])[14]").click()
driver.find_element(By.XPATH, "(//div[@id='content'])[1]").click()
driver.find_element(By.XPATH, "//input[@id='pFName']").send_keys("Neha")
driver.find_element(By.XPATH, "//input[@id='pLName']").send_keys("Sharma")
driver.find_element(By.XPATH, "//input[@id='pPhone']").send_keys("9099823482")
driver.find_element(By.XPATH, "//input[@id='pReceiptEmail']").send_keys("neha@grubbrr.com")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='credit_card_holder_name']").send_keys("neha")
driver.find_element(By.XPATH, "//input[@id='credit_card_number']").send_keys("5105105105105100")
driver.find_element(By.XPATH, "//input[@id='expiry_date']").send_keys("12/24")
driver.find_element(By.XPATH, "//input[@id='cvv']").send_keys("123")
driver.find_element(By.XPATH, "//input[@id='zipcode']").send_keys("90001")
a = driver.find_element(By.XPATH, "//span[@id='Subtotal']")
subtotal = a.get_attribute("innerHTML")
b = driver.find_element(By.XPATH, "//span[@id='DiscountAmount']")
discount = b.get_attribute("innerHTML")
print("Subtotal of all items", subtotal)
print("Discount applied on Subtotal", discount)
c = driver.find_element(By.XPATH, "//span[@id='ExtraFee']")
fee = c.get_attribute("innerHTML")
e = driver.find_element(By.XPATH,"//span[@id='Total']")
total1 = e.get_attribute("innerHTML")
print("Actual Total:",float(total1))

class test():
  total2=''
  def total(self, subtotal, discount, fee):
    global total2
    tax = ((float(subtotal) - float(discount) )* 10) / 100
    total2 = float()
    total2 = subtotal + fee + tax
    return total2

d=test()
d.total(float(subtotal), float(discount), float(fee))
print ("Expected Total", total2)
asserts.assert_equal(float(total1), float(total2))
print("Calculation working fine")
driver.find_element(By.XPATH, "//button[@id='CompleteOrder']").click()
time.sleep(2)
print(driver.title)
time.sleep(5)
assert 'Online Ordering - Grubbrr', driver.title
print("Pickup later passed")
driver.quit()

