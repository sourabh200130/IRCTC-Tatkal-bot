import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def selectTrain(driver):
    # Find the element containing "Panchaganga Express" text
    panchaganga_express = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'PANCHAGANGA EXP (16595)')]"))
    )

    # Find the "Sleeper" option within the same div
    coach_option = panchaganga_express.find_element(By.XPATH, "following::*/text()[contains(., 'Sleeper')]/parent::*")
    coach_option.click()

    time.sleep(2)
    date = coach_option.find_element(By.XPATH, "following::*/text()[contains(., '30')]/parent::*")
    date.click()


