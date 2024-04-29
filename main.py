from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import searchTrain
import login
import train

import paddleOCR
import selectTrain

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
login.login(driver)

Train = train.train()


# Search train
searchTrain.search(driver, Train)

# Select train and coach
selectTrain.selectTrain(driver, Train)