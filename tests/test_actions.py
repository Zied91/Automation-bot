from src.actions import login, extract_titles
from config.settings import BASE_URL
from selenium.webdriver.common.by import By


def test_login(driver):
    login(driver)

    # After login, user is redirected to inventory page
    assert "inventory" in driver.current_url


def test_extract_titles(driver):
    driver.get(BASE_URL)
    login(driver)

    titles = extract_titles(driver)

    assert isinstance(titles, list)
    assert len(titles) > 0
    assert all(isinstance(t, str) for t in titles)
