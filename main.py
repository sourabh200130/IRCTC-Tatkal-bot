from selenium import webdriver
from selenium.webdriver.common.by import By
import paddleOCR
import passwords

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.irctc.co.in/nget/train-search")

driver.find_element(By.LINK_TEXT, "LOGIN").click()
driver.find_element(By.CSS_SELECTOR, 'input[placeholder="User Name"]').send_keys(passwords.username)
driver.implicitly_wait(1)
driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Password"]').send_keys(passwords.password)
driver.implicitly_wait(1)
image = driver.find_element(By.CLASS_NAME, "captcha-img")
image.screenshot("image.png")
result = paddleOCR.solve()
captcha_field = driver.find_element("id", "captcha")
captcha_field.send_keys(result)
driver.find_element(By.CSS_SELECTOR, "form[class='ng-valid ng-dirty ng-touched'] button[type='submit']").click()
