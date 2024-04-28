import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import paddleOCR


def login(driver):
    driver.find_element(By.LINK_TEXT, "LOGIN").click()

    # Wait for the username field to be clickable
    userName = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/app-root[1]/app-home[1]/div[3]/app-login[1]/p-dialog['
                                              '1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/form['
                                              '1]/div[1]/input[1]')))
    userName.send_keys(os.getenv("user"))

    # Wait for the password field to be clickable
    password = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/app-root[1]/app-home[1]/div[3]/app-login[1]/p-dialog['
                                              '1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/form['
                                              '1]/div[2]/input[1]')))
    password.send_keys(os.getenv("pass"))


    driver.implicitly_wait(1)

    wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "captcha-img")))
    time.sleep(1)
    # Downloading the capcha image
    image = driver.find_element(By.CLASS_NAME, "captcha-img")
    image.screenshot("image.png")

    # Using Machine Learning to solve the capcha
    result = paddleOCR.solve()
    captcha_field = driver.find_element("id", "captcha")
    captcha_field.send_keys(result)
    submitBtn = driver.find_element(By.CSS_SELECTOR, "form[class='ng-valid ng-dirty ng-touched'] button[type='submit']")
    submitBtn.click()