from selenium import webdriver
from selenium.webdriver.common.by import By
import paddleOCR
from dotenv import load_dotenv
import os

# Load my username and password securely. It will be removed when a gnu is created in future
load_dotenv()

# Selenium and webdriver setup
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# opening website
driver.get("https://www.irctc.co.in/nget/train-search")

# Logging in using my credentials
driver.find_element(By.LINK_TEXT, "LOGIN").click()
userName = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="User Name"]')
userName.send_keys(os.getenv("user"))
driver.implicitly_wait(1)
password = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Password"]')
password.send_keys(os.getenv("pass"))
driver.implicitly_wait(1)

# Downloading the capcha image
image = driver.find_element(By.CLASS_NAME, "captcha-img")
image.screenshot("image.png")

# Using Machine Learning to solve the capcha
result = paddleOCR.solve()
captcha_field = driver.find_element("id", "captcha")
captcha_field.send_keys(result)
submitBtn = driver.find_element(By.CSS_SELECTOR, "form[class='ng-valid ng-dirty ng-touched'] button[type='submit']")
submitBtn.click()
