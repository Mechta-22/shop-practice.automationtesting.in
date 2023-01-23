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
# b = driver.find_element_by_id("username")
# b.send_keys("kia-2003@mail.ru")
# c = driver.find_element_by_id("password")
# c.send_keys("m4.UIp.32007")
# d = driver.find_element_by_css_selector("[name='login']")
# d.click()
# e = driver.find_element_by_css_selector("li#menu-item-40>a")
# e.click()
# s = driver.find_element_by_css_selector("[title='Mastering HTML5 Forms']")
# s.click()
# book_title = driver.find_element_by_tag_name("h1")
# book_title_text = book_title.text
# assert book_title_text == "HTML5 Forms"
#


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
# b = driver.find_element_by_id("username")
# b.send_keys("kia-2003@mail.ru")
# c = driver.find_element_by_id("password")
# c.send_keys("m4.UIp.32007")
# d = driver.find_element_by_css_selector("[name='login']")
# d.click()
# e = driver.find_element_by_css_selector("li#menu-item-40>a")
# e.click()
# HTML = driver.find_element_by_css_selector("a[href='https://practice.automationtesting.in/product-category/html/']")
# HTML.click()
# HTML_count = driver.find_elements_by_css_selector("[height='300']")
# if len(HTML_count) == 3:
#     print("В категории HTML 3 товара")
# else:
#     print("Ошибка. Количество товаров в категории HTML:" + str(len(HTML_count)))
#

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
# b = driver.find_element_by_id("username")
# b.send_keys("kia-2003@mail.ru")
# c = driver.find_element_by_id("password")
# c.send_keys("m4.UIp.32007")
# d = driver.find_element_by_css_selector("[name='login']")
# d.click()
# e = driver.find_element_by_css_selector("li#menu-item-40>a")
# e.click()
# status_selector = driver.find_element_by_css_selector("select[name='orderby']")
# select = Select(status_selector)
# select.select_by_visible_text("Default sorting")
# status_selector_default = status_selector.get_attribute("value")
# if status_selector_default == "menu_order":
#     print("Выбрано значение по умолчанию")
# else:
#     print("Выбрано другое значение:", status_selector_default)
# status_selector = driver.find_element_by_css_selector("select[name='orderby']")
# select = Select(status_selector)
# select.select_by_index(5)
# status_selector = driver.find_element_by_css_selector("select[name='orderby']")
# select = Select(status_selector)
# status_selector_high = status_selector.get_attribute("value")
# if status_selector_high == "price-desc":
#     print("Выбрана сортировка по убыванию цены")
# else:
#     print("Выбрано другое значение:", status_selector_high)
#


# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# driver.maximize_window()
# from selenium.webdriver.support.ui import WebDriverWait
# driver.implicitly_wait(5)
# driver.get("http://practice.automationtesting.in/")
# a = driver.find_element_by_css_selector("li#menu-item-50>a")
# a.click()
# b = driver.find_element_by_id("username")
# b.send_keys("kia-2003@mail.ru")
# c = driver.find_element_by_id("password")
# c.send_keys("m4.UIp.32007")
# d = driver.find_element_by_css_selector("[name='login']")
# d.click()
# e = driver.find_element_by_css_selector("li#menu-item-40>a")
# e.click()
# android = driver.find_element_by_css_selector("[data-product_id='169']")
# android.click()
# old_price = driver.find_element_by_css_selector("del > .woocommerce-Price-amount")
# old_price_text = old_price.text
# assert old_price_text == "₹600.00"
# new_price = driver.find_element_by_css_selector("ins > .woocommerce-Price-amount")
# new_price_text = new_price.text
# assert new_price_text == "₹450.00"
# run = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[ title='Android Quick Start Guide']")))
# run.click()
# XXX = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "fullResImage")))
# ggg = driver.find_element_by_css_selector("a.pp_close")
# ggg.click()


#
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# driver.maximize_window()
# from selenium.webdriver.support.ui import WebDriverWait
# driver.implicitly_wait(5)
# driver.get("http://practice.automationtesting.in/")
# e = driver.find_element_by_css_selector("li#menu-item-40>a")
# e.click()
# book = driver.find_element_by_css_selector("[data-product_id='182']")
# book.click()
# book_2 = driver.find_element_by_css_selector("[title='View Basket']")
# book_2.click()
# item_count = driver.find_element_by_css_selector("span.cartcontents")
# item_count_text = item_count.text
# assert item_count_text == "1 Item"
# item_count_2 = driver.find_element_by_css_selector("li > a >  span.amount")
# item_count_2_text = item_count_2.text
# assert item_count_2_text == "₹180.00"
# some_element = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title='Subtotal'] > span"), "₹180.00"))
# some_element_2 = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, "strong > span"), "₹183.60"))


# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# driver.maximize_window()
# from selenium.webdriver.support.ui import WebDriverWait
# driver.implicitly_wait(5)
# driver.get("http://practice.automationtesting.in/")
# e = driver.find_element_by_css_selector("li#menu-item-40>a")
# e.click()
# driver.execute_script("window.scrollBy(0, 300);")
# book = driver.find_element_by_css_selector("[data-product_id='182']")
# book.click()
# time.sleep(5)
# book_3 = driver.find_element_by_css_selector("[data-product_id='165']")
# book_3.click()
# book_2 = driver.find_element_by_css_selector("[title='View Basket']")
# book_2.click()
# delete_book = driver.find_element_by_css_selector("a.remove[data-product_id='182']")
# delete_book.click()
# time.sleep(10)
# book_4 = driver.find_element_by_css_selector(".woocommerce-message > a")
# book_4.click()
# time.sleep(10)
# oo = driver.find_element_by_css_selector("[max='7289']")
# oo.clear()
# time.sleep(10)
# cle = driver.find_element_by_css_selector(".quantity .input-text.qty.text[max='7289']")
# cle.send_keys("3")
# time.sleep(10)
# update = driver.find_element_by_css_selector("[name='update_cart']")
# update.click()
#
# count = driver.find_element_by_css_selector(".quantity .input-text.qty.text[max='7289']")
# count_check = count.get_attribute("value")
# assert count_check == "3"
# time.sleep(10)
# vvv = driver.find_element_by_css_selector("input[name='apply_coupon']")
# vvv.click()
# mmm = driver.find_element_by_css_selector("ul.woocommerce-error > li")
# mmm_text = mmm.text
# assert mmm_text == "Please enter a coupon code."
# driver.quit()
#




import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver.maximize_window()
from selenium.webdriver.support.ui import WebDriverWait
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
e = driver.find_element_by_css_selector("li#menu-item-40>a")
e.click()
driver.execute_script("window.scrollBy(0, 300);")
book = driver.find_element_by_css_selector("[data-product_id='182']")
book.click()
time.sleep(5)
book_2 = driver.find_element_by_css_selector("[title='View Basket']")
book_2.click()
XXX = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.checkout-button")))
XXX.click()
yyy = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "billing_first_name")))
yyy.send_keys("Polev")
zzz = driver.find_element_by_id("billing_last_name")
zzz.send_keys("Ivan")
nnn = driver.find_element_by_id("billing_email")
nnn.send_keys("kia-2003@mail.ru")
lll = driver.find_element_by_id("billing_phone")
lll.send_keys("+79085555555")
sss = driver.find_element_by_id("select2-chosen-1")
sss.click()
time.sleep(10)
ttt = driver.find_element_by_css_selector("input#s2id_autogen1_search.select2-input.select2-focused")
ttt.send_keys("Russia")
time.sleep(10)
jjj = driver.find_element_by_css_selector("div#select2-result-label-394.select2-result-label")
jjj.click()
qqq = driver.find_element_by_id("billing_address_1")
qqq.send_keys("улица Мира, дом 20, кв 50")
dd = driver.find_element_by_id("billing_city")
dd.send_keys("Москва")
ddd = driver.find_element_by_id("billing_state")
ddd.send_keys("Центральный Федеральный округ")
ww = driver.find_element_by_id("billing_postcode")
ww.send_keys("101000")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(10)
bbb = driver.find_element_by_id("payment_method_cheque")
bbb.click()
www = driver.find_element_by_id("place_order")
www.click()
some_element = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "p.woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
some_element_2 = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "li.method >strong"), "Check Payments"))
driver.quit()
