# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# from selenium.webdriver.support.select import Select
# driver.maximize_window()
# from selenium.webdriver.support.ui import WebDriverWait
# driver.implicitly_wait(5)
# driver.get("http://practice.automationtesting.in/")
# a = driver.find_element_by_css_selector("li#menu-item-50>a")
# a.click()
# b = driver.find_element_by_id("reg_email")
# b.send_keys("kia-2003@mail.ru")
# c = driver.find_element_by_id("reg_password")
# c.send_keys("m4.UIp.32007")
# d = driver.find_element_by_css_selector("[name='register']")
# d.click()
# driver.quit()




import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
from selenium.webdriver.support.select import Select
driver.maximize_window()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
a = driver.find_element_by_css_selector("li#menu-item-50>a")
a.click()
b = driver.find_element_by_id("username")
b.send_keys("kia-2003@mail.ru")
c = driver.find_element_by_id("password")
c.send_keys("m4.UIp.32007")
d = driver.find_element_by_css_selector("[name='login']")
d.click()
run = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li a[href='https://practice.automationtesting.in/my-account/customer-logout/']")))
driver.quit()
