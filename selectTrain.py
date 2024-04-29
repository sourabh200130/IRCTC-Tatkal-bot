import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def selectTrain(driver, Train):
    # Find the element containing "Panchaganga Express" text
    train_xpath = "//*[contains(text(), '{}')]".format(Train.trainName)
    train = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, train_xpath))
    )

    # Search coach Under train
    coach_xpath = "following::*/text()[contains(., '{}')]/parent::*".format(Train.coach)
    coach_option = train.find_element(By.XPATH, coach_xpath)
    coach_option.click()
    time.sleep(1)
    date = train.find_element(By.XPATH, "following::div[contains(@class, 'pre-avl')][1]")
    date.click()

    time.sleep(0.5)
    book = train.find_element(By.XPATH, "following::*/text()[contains(., 'Book Now')]/parent::*")
    book.click()
