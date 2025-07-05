import pytest
import allure
from selenium import webdriver

@allure.title("Browser Navigation Test")
@allure.description("Test basic browser navigation: open, back, forward, refresh, and print current URL.")
@allure.severity(allure.severity_level.NORMAL)
def test_browser_navigation():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        with allure.step("Open Google"):
            driver.get("https://www.google.com")
            allure.attach(driver.title, name="Google Page Title", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Open Wikipedia"):
            driver.get("https://www.wikipedia.org")
            allure.attach(driver.title, name="Wikipedia Page Title", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Go back to Google"):
            driver.back()
            allure.attach(driver.title, name="Back Page Title", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Go forward to Wikipedia"):
            driver.forward()
            allure.attach(driver.title, name="Forward Page Title", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Refresh current page"):
            driver.refresh()
            allure.attach(driver.title, name="Refreshed Page Title", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Attach current URL"):
            current_url = driver.current_url
            allure.attach(current_url, name="Current URL", attachment_type=allure.attachment_type.TEXT)

    except Exception as e:
        try:
            allure.attach(driver.get_screenshot_as_png(), name="Error Screenshot", attachment_type=allure.attachment_type.PNG)
        except:
            pass
        raise e

    finally:
        driver.quit()
