from src.utilities import log
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import USERNAME, PASSWORD, BASE_URL, IMPLICIT_WAIT


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
    log("Waiting for titles to appear...")

    wait = WebDriverWait(driver, IMPLICIT_WAIT)
    wait.until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name"))
    )
    titles = driver.find_elements(By.CLASS_NAME, "inventory_item_name")

    return [t.text for t in titles]
