import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("Google Search Box Visibility Test")
@allure.description("Verify that the search box is visible on Google's homepage.")
@allure.severity(allure.severity_level.CRITICAL)
def test_google_search_box_visible():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        with allure.step("Open Google homepage"):
            driver.get("https://www.google.com/")

        with allure.step("Wait for search box to be visible"):
            wait = WebDriverWait(driver, 10)
            searchbox = wait.until(EC.visibility_of_element_located((By.NAME, "q")))

        with allure.step("Validate search box is displayed"):
            assert searchbox.is_displayed(), "Search box should be displayed"
            allure.attach(driver.get_screenshot_as_png(), name="Search Box Visible Screenshot", attachment_type=allure.attachment_type.PNG)

    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(), name="Error Screenshot", attachment_type=allure.attachment_type.PNG)
        raise e

    finally:
        driver.quit()
