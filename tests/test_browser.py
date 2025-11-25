def test_browser_starts(driver):
    assert driver is not None
    assert driver.capabilities is not None


def test_site_loads(driver):
    driver.get("https://example.com")
    assert "Example" in driver.title
