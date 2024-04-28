from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def search(driver):
    boarding = driver.find_element(By.CSS_SELECTOR, '.ng-tns-c57-8.ui-inputtext.ui-widget.ui-state-default.ui-corner'
                                                    '-all.ui-autocomplete-input.ng-star-inserted')

    actions = ActionChains(driver)

    actions.send_keys_to_element(boarding, "YPR")
    actions.pause(1)
    actions.send_keys(Keys.RETURN)
    actions.perform()

    destination = driver.find_element(By.CSS_SELECTOR, ".ng-tns-c57-9.ui-inputtext.ui-widget.ui-state-default.ui-corner"
                                                       "-all.ui-autocomplete-input.ng-star-inserted")

    actions.send_keys_to_element(destination, "BKJ")
    actions.pause(1)
    actions.send_keys(Keys.RETURN)
    actions.perform()

    date = driver.find_element(By.CSS_SELECTOR, ".ng-tns-c58-10.ui-inputtext.ui-widget.ui-state-default.ui-corner-all.ng"
                                             "-star-inserted")
    date.click()
    for i in range(0,10):
        date.send_keys(Keys.BACKSPACE)
    date.send_keys("30/05/2024")
    date.send_keys(Keys.RETURN)

