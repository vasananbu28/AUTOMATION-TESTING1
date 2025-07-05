import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@allure.title("Navigate to Elements card on DemoQA")
@allure.description("Test navigation to the Elements section and validate the URL.")
@allure.severity(allure.severity_level.NORMAL)
def test_navigate_elements_card():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    try:
        with allure.step("Open DemoQA homepage"):
            driver.get("https://demoqa.com/")

        with allure.step("Find and click the Elements card"):
            card_xpath = "//h5[text()='Elements']/ancestor::div[@class='card mt-4 top-card']"
            menu_card = wait.until(EC.element_to_be_clickable((By.XPATH, card_xpath)))
            driver.execute_script("arguments[0].scrollIntoView(true);", menu_card)
            ActionChains(driver).move_to_element(menu_card).perform()
            menu_card.click()

        with allure.step("Validate that URL redirects correctly"):
            current_url = driver.current_url
            allure.attach(current_url, name="Current URL", attachment_type=allure.attachment_type.TEXT)
            assert "elements" in current_url.lower(), "URL did not contain 'elements'"

    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(), name="Error Screenshot", attachment_type=allure.attachment_type.PNG)
        raise e

    finally:
        driver.quit()
