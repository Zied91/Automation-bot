from src.browser import create_browser
from src.actions import login, extract_titles
from src.utilities import log


def main():
    log("Starting bot...")

    driver = create_browser()

    try:
        login(driver)
        titles = extract_titles(driver)

        log(f"Found {len(titles)} items:")
        for t in titles:
            log(f" - {t}")

    except Exception as e:
        log(f"Error occurred: {e}")

    finally:
        driver.quit()
        log("Bot finished.")


if __name__ == "__main__":
    main()
