import pytest
from src.browser import create_browser


@pytest.fixture(scope="session")
def driver():
    driver = create_browser()
    yield driver
    driver.quit()
