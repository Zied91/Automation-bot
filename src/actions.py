from src.utilities import log
from selenium.webdriver.common.by import By
from config.settings import USERNAME, PASSWORD, BASE_URL


def login(driver):
    log("Opening page...")
    driver.get(BASE_URL)

    log("Entering username...")
    driver.find_element(By.ID, "user-name").send_keys(USERNAME)

    log("Entering password...")
    driver.find_element(By.ID, "password").send_keys(PASSWORD)

    log("Submitting login...")
    driver.find_element(By.ID, "login-button").click()


def extract_titles(driver):
    log("Extracting item titles...")
    titles = driver.find_elements(By.CLASS_NAME, "inventory_item")

    return [t.text for t in titles]
