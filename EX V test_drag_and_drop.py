import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

@allure.title("Drag and Drop Test on jQuery UI")
@allure.description("Test drag and drop functionality on jQuery UI and validate the dropped text.")
@allure.severity(allure.severity_level.CRITICAL)
def test_drag_and_drop():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        with allure.step("Open jQuery UI droppable page"):
            driver.get("https://jqueryui.com/droppable/")

        with allure.step("Switch to demo iframe"):
            iframe = driver.find_element(By.CSS_SELECTOR, ".demo-frame")
            driver.switch_to.frame(iframe)

        with allure.step("Find source and target elements"):
            source = driver.find_element(By.ID, "draggable")
            target = driver.find_element(By.ID, "droppable")

        with allure.step("Perform drag and drop"):
            actions = ActionChains(driver)
            actions.drag_and_drop(source, target).perform()

        with allure.step("Validate dropped text"):
            dropped_text = target.text
            allure.attach(dropped_text, name="Dropped Text", attachment_type=allure.attachment_type.TEXT)
            assert dropped_text == "Dropped!", "Drag and drop not successful"

        with allure.step("Switch back to default content"):
            driver.switch_to.default_content()

    except Exception as e:
        # Make sure we attempt screenshot before quitting
        try:
            allure.attach(driver.get_screenshot_as_png(), name="Error Screenshot", attachment_type=allure.attachment_type.PNG)
        except:
            pass  # Ignore screenshot errors

        raise e

    finally:
        driver.quit()
