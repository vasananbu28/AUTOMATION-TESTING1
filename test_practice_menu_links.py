import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@allure.title("Menu Link Redirect Test - Practice Test Automation")
@allure.description("Validate that the Blog and Contact menu links redirect to the correct pages.")
@allure.severity(allure.severity_level.CRITICAL)
def test_menu_links_redirect():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        with allure.step("Open Practice Test Automation homepage"):
            driver.get("https://practicetestautomation.com/")
            time.sleep(2)

        menu_items = {
            "Blog": ("a[href*='blog']", "blog"),
            "Contact": ("a[href*='contact']", "contact")
        }

        for name, (css_selector, expected_url_part) in menu_items.items():
            with allure.step(f"Click on '{name}' menu and validate URL"):
                link = driver.find_element(By.CSS_SELECTOR, css_selector)
                link.click()
                time.sleep(2)

                current_url = driver.current_url
                allure.attach(current_url, name=f"{name} URL", attachment_type=allure.attachment_type.TEXT)

                if expected_url_part in current_url:
                    assert True, f"{name} redirects correctly"
                else:
                    allure.attach(driver.get_screenshot_as_png(), name=f"{name} Redirect Error", attachment_type=allure.attachment_type.PNG)
                    pytest.fail(f"{name} does NOT redirect correctly. Expected part: '{expected_url_part}'")

            with allure.step("Return to homepage before next link test"):
                driver.get("https://practicetestautomation.com/")
                time.sleep(2)

    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(), name="Unhandled Error", attachment_type=allure.attachment_type.PNG)
        raise e

    finally:
        driver.quit()
