import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@allure.title("Hover Menu Test on DemoQA")
@allure.description("Test hovering over menu items and sub-items on the DemoQA Menu page.")
@allure.severity(allure.severity_level.NORMAL)
def test_hover_menu_demoqa():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    try:
        with allure.step("Open DemoQA Menu page"):
            driver.get("https://demoqa.com/menu")

        with allure.step("Hover over 'Main Item 2'"):
            main_item2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Main Item 2']")))
            driver.execute_script("arguments[0].scrollIntoView(true)", main_item2)
            ActionChains(driver).move_to_element(main_item2).perform()
            time.sleep(1)

        with allure.step("Hover over 'SUB SUB LIST »'"):
            sub_sub_list = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='SUB SUB LIST »']")))
            ActionChains(driver).move_to_element(sub_sub_list).perform()
            time.sleep(1)

        with allure.step("Hover over 'Sub Sub Item 2'"):
            sub_sub_item2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Sub Sub Item 2']")))
            ActionChains(driver).move_to_element(sub_sub_item2).perform()
            time.sleep(1)

        with allure.step("Attach hover screenshot"):
            allure.attach(driver.get_screenshot_as_png(), name="Hover Screenshot", attachment_type=allure.attachment_type.PNG)

        print("Hovering completed successfully")
        assert True, "Hover actions completed successfully"

    except Exception as e:
        # Attach screenshot on failure
        allure.attach(driver.get_screenshot_as_png(), name="Error Screenshot", attachment_type=allure.attachment_type.PNG)
        raise e
