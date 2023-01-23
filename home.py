import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
from selenium.webdriver.support.select import Select
driver.maximize_window()
from selenium.webdriver.support.ui import WebDriverWait
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
a = driver.find_element_by_css_selector("[data-product_id='160']")
a.click()
b = driver.find_element_by_css_selector("a[href='#tab-reviews']")
b.click()
c = driver.find_element_by_css_selector("a.star-5")
c.click()
e = driver.find_element_by_css_selector("textarea[name='comment']")
e.send_keys("Nice book!")
ee = driver.find_element_by_id("author")
ee.send_keys("Inna")
cc = driver.find_element_by_id("email")
cc.send_keys("kia-2003@mail.ru")
dd = driver.find_element_by_id("submit")
dd.click()
driver.quit()
