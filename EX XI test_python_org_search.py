import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@allure.title("Python.org Search Test")
@allure.description("Test to search for 'pycon' on python.org and validate that results are shown.")
@allure.severity(allure.severity_level.CRITICAL)
def test_python_org_search():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        with allure.step("Open Python.org homepage"):
            driver.get("https://www.python.org/")

        with allure.step("Locate search box and perform search for 'pycon'"):
            search_box = driver.find_element(By.NAME, "q")
            search_box.send_keys("pycon")
            search_box.send_keys(Keys.RETURN)

        with allure.step("Check if results exist"):
            # Wait implicitly using page source check
            driver.implicitly_wait(3)
            if "No results found." not in driver.page_source:
                allure.attach(driver.page_source, name="Search Results Page Source", attachment_type=allure.attachment_type.HTML)
                assert True, "Searched results for 'pycon' found."
            else:
                allure.attach(driver.get_screenshot_as_png(), name="No Results Screenshot", attachment_type=allure.attachment_type.PNG)
                pytest.fail("'pycon' does not exist in search results.")

    except Exception as e:
        # Attach screenshot before quitting
        try:
            allure.attach(driver.get_screenshot_as_png(), name="Error Screenshot", attachment_type=allure.attachment_type.PNG)
        except:
            pass
        raise e

    finally:
        driver.quit()
