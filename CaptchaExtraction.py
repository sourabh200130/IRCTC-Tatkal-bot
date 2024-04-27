from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.irctc.co.in/nget/train-search")
login = driver.find_element(By.LINK_TEXT, "LOGIN")
login.click()
for i in range(1,100):
    image = driver.find_element(By.CLASS_NAME, "captcha-img")
    image.screenshot(f"images/{i}.png")
    refresh = driver.find_element(By.CLASS_NAME,"glyphicon-repeat")
    refresh.click()
    driver.implicitly_wait(2)

